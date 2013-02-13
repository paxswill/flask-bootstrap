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

