from __future__ import unicode_literals

import datetime

from wtforms import fields, widgets


# HTML5 input types
class PlaceholderMixin(object):
    def __init__(self, *varargs, **kwargs):
        self.placeholder = kwargs.pop('placeholder', None)
        super(PlaceholderMixin, self).__init__(*varargs, **kwargs)

    def __call__(self, **kwargs):
        if self.placeholder:
            kwargs.setdefault('placeholder', self.placeholder)
        return super(PlaceholderMixin, self).__call__(**kwargs)


class DateTimeInput(widgets.Input):
    input = 'datetime'


class DateInput(widgets.Input):
    input = 'date'


class MonthInput(widgets.Input):
    input = 'month'


class WeekInput(widgets.Input):
    input = 'week'


class TimeInput(widgets.Input):
    input = 'time'


class EmailInput(widgets.Input):
    input = 'email'


class RangeInput(widgets.Input):
    input = 'range'


class SearchInput(widgets.Input):
    input = 'search'


class TelephoneInput(widgets.Input):
    input = 'tel'


class URLInput(widgets.Input):
    input = 'url'


class DateTimeField(fields.DateTimeField):
    widget = DateTimeInput()


class DateField(fields.DateField):
    widget = DateInput()


class TimeField(DateTimeField):
    widget = TimeInput()

    def __init__(self, label=None, validators=None, format='%H:%M:%S',
            **kwargs):
        super(TimeField, self).__init__(label, validators, format, **kwargs)

    def process_formdate(self, valuelist):
        if valuelist:
            time_str = ' '.join(valuelist)
            try:
                self.data = datetime.strptime(date_str, self.format).time()
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid time value'))


class StringField(PlaceholderMixin, fields.StringField):
    pass


class TextField(PlaceholderMixin, fields.TextField):
    pass


class SearchField(StringField):
    widget = SearchInput()


class TelephoneField(StringField):
    widget = TelephoneInput()


class URLField(StringField):
    widget = URLInput()


class EmailField(StringField):
    widget = EmailInput()


# Helper class and function
class DummyLabel(fields.Label):
    def __init__(self, label):
        self.label = label
        self.text = self.label.text
        self.field_id = self.label.field_id

    def __call__(self, **kwargs):
        return ''


class DummyLabelMixin(object):
    def __init__(self, *varargs, **kwargs):
        super(DummyLabelMixin, self).__init__(*varargs, **kwargs)
        self.label = DummyLabel(self.label)


def _require_class(classes, kwargs):
    if 'class' in kwargs:
        kwargs['class'] += ' ' + classes
    else:
        kwargs['class'] = classes


# Fields that need the <input> within the <label> elements
class BooleanField(DummyLabelMixin, fields.BooleanField):
    def __call__(self, **kwargs):
        _require_class('checkbox', kwargs)
        return self.label.label(text=(self.widget(self)+self.label.text),
                                **kwargs)


class RadioListWidget(widgets.ListWidget):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        _require_class('radio', kwargs)

        html = []
        for subfield in field:
            html.append(subfield.label(text=(subfield()+subfield.label.text),
                **kwargs))
        return widgets.HTMLString(''.join(html))


class RadioField(fields.RadioField):
    widget = RadioListWidget()


# Buttons, both <button> and <input> varieties
class Button(object):
    button_type = 'button'
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.button_type)
        _require_class('btn', kwargs)
        kwargs['name'] = field.name

        return widgets.HTMLString('<button %s>%s</button>' %
                         (widgets.html_params(**kwargs), field.label.text))


class SubmitButton(Button):
    button_type = 'submit'

    def __call__(self, field, **kwargs):
        _require_class('btn-primary', kwargs)
        return super(SubmitButton, self).__call__(field, **kwargs)


class ButtonInput(widgets.SubmitInput):
    input_type = 'button'

    def __call__(self, field, **kwargs):
        _require_class('btn', kwargs)
        return super(ButtonInput, self).__call__(field, **kwargs)


class SubmitInput(ButtonInput):
    input_type = 'submit'

    def __call__(self, field, **kwargs):
        _require_class('btn-primary', kwargs)
        return super(SubmitInput, self).__call__(field, **kwargs)


class ButtonField(DummyLabelMixin, fields.Field):
    widget = Button()


class SubmitButtonField(ButtonField):
    widget = SubmitButton()


class ButtonInputField(DummyLabelMixin, fields.SubmitField):
    widget = ButtonInput()


class SubmitField(ButtonInputField):
    widget = SubmitInput()

