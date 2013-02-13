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


# Bootstrap-specific widgets
class DummyLabel(Label):
    def __init__(self, **kwargs):
        pass

    def __call__(self, **kwargs):
        return ''


class BooleanField(fields.BooleanField):
    def __init__(self, label=None, validators=None, **kwargs):
        super(BooleanField, self).__init__(label, validators, **kwargs)
        self._label = self.label
        self.label = DummyLabel()

    def __call__(self, **kwargs):
        if 'class' in kwargs:
            kwargs['class'] = 'checkbox ' + kwargs['class']
        else:
            kwargs.setdefault('class', 'checkbox')

        return self._label(text=(self.widget(self)+self._label.text), **kwargs)


class RadioListWidget(widgets.ListWidget):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        if 'class' in kwargs:
            kwargs['class'] = 'radio ' + kwargs['class']
        else:
            kwargs.setdefault('class', 'radio')

        html = []
        for subfield in field:
            html.append(subfield.label(text=(subfield()+subfield.label.text),
                **kwargs))
        return HTMLString(''.join(html))


class RadioField(fields.RadioField):
    widget = RadioListWidget()

