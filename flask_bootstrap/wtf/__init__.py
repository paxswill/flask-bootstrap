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
class CheckboxLabel(Label):
    def __init__(self, field_id, text, field):
        super(CheckboxLabel, self).__init__(field_id, text)
        self.field = field

    def __call__(self, text=None, **kwargs):
        if 'for_' in kwargs:
            kwargs['for'] = kwargs.pop('for_')
        else:
            kwargs.setdefault('for', self.field_id)

        if 'class' in kwargs:
            kwargs['class'] = 'checkbox ' + kwargs['class']

        attributes = widgets.html_params(**kwargs)
        return HTMLString('<label %s>%s %s</label>' % (attributes,
            self.field(), text or self.text))


class BooleanField(fields.BooleanField):
    def __init__(self, label=None, validators=None, **kwargs):
        super(BooleanField, self).__init__(label, validators, **kwargs)
        self.label = CheckboxLabel(self.id, self.label.text, self)

    def __call__(self, **kwargs):
        return self.label(**kwargs)

