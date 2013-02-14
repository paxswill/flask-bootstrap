from __future__ import unicode_literals, absolute_import

from wtforms import widgets

from . import public, require_class

class RequireableInput(widgets.Input):
    def __call__(self, field, **kwargs):
        if field.flags.required:
            kwargs.setdefault('required', '')
        return super(RequireableInput, self).__call__(field, **kwargs)


@public
class TextInput(RequireableInput, widgets.TextInput):
    pass


@public
class PasswordInput(RequireableInput, widgets.PasswordInput):
    pass


@public
class CheckboxInput(RequireableInput, widgets.CheckboxInput):
    pass


class TextArea(RequireableInput, widgets.TextArea):
    pass


@public
class RadioInput(RequireableInput, widgets.RadioInput):
    pass


@public
class DateTimeInput(RequireableInput):
    input_type = 'datetime'


@public
class DateInput(RequireableInput):
    input_type = 'date'


class MonthInput(RequireableInput):
    input_type = 'month'


class WeekInput(RequireableInput):
    input_type = 'week'


@public
class TimeInput(RequireableInput):
    input_type = 'time'


@public
class EmailInput(RequireableInput):
    input_type = 'email'


class RangeInput(RequireableInput):
    input_type = 'range'


@public
class SearchInput(RequireableInput):
    input_type = 'search'


@public
class TelephoneInput(RequireableInput):
    input_type = 'tel'


@public
class URLInput(RequireableInput):
    input_type = 'url'


@public
class NumberInput(RequireableInput):
    input_type = 'number'


@public
class RadioListWidget(widgets.ListWidget):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        require_class('radio', kwargs)

        html = []
        for subfield in field:
            html.append(subfield.label(text=(subfield()+subfield.label.text),
                **kwargs))
        return widgets.HTMLString(''.join(html))


@public
class Button(object):
    button_type = 'button'
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.button_type)
        require_class('btn', kwargs)
        kwargs['name'] = field.name

        return widgets.HTMLString('<button %s>%s</button>' %
                         (widgets.html_params(**kwargs), field.label.text))


@public
class SubmitButton(Button):
    button_type = 'submit'

    def __call__(self, field, **kwargs):
        require_class('btn-primary', kwargs)
        return super(SubmitButton, self).__call__(field, **kwargs)


@public
class ButtonInput(widgets.SubmitInput):
    input_type = 'button'

    def __call__(self, field, **kwargs):
        require_class('btn', kwargs)
        return super(ButtonInput, self).__call__(field, **kwargs)


@public
class SubmitInput(ButtonInput):
    input_type = 'submit'

    def __call__(self, field, **kwargs):
        require_class('btn-primary', kwargs)
        return super(SubmitInput, self).__call__(field, **kwargs)

