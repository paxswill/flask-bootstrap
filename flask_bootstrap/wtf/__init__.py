from __future__ import unicode_literals

import datetime

from wtforms import fields, widgets
from wtforms.fields import (Label, Field, DecimalField, FloatField,
        IntegerField, StringField, TextField, TextAreaField)
from wtforms.widgets import (TextInput, CheckboxInput, TextArea, Select, Input,
        HTMLString)


# HTML5 input types
class DateTimeInput(Input):
    input = 'datetime'


class DateInput(Input):
    input = 'date'


class MonthInput(Input):
    input = 'month'


class WeekInput(Input):
    input = 'week'


class TimeInput(Input):
    input = 'time'


class EmailInput(Input):
    input = 'email'


class RangeInput(Input):
    input = 'range'


class SearchInput(Input):
    input = 'search'


class TelephoneInput(Input):
    input = 'tel'


class URLInput(Input):
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


# Helper class and function
class DummyLabel(Label):
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
        return HTMLString(''.join(html))


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

        return HTMLString('<button %s>%s</button>' %
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

