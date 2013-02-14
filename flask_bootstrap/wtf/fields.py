from __future__ import unicode_literals, absolute_import

import datetime

from wtforms import fields

from . import public, require_class
from .widgets import *

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




class PlaceholderMixin(object):
    def __init__(self, *varargs, **kwargs):
        self.placeholder = kwargs.pop('placeholder', None)
        super(PlaceholderMixin, self).__init__(*varargs, **kwargs)

    def __call__(self, **kwargs):
        if self.placeholder:
            kwargs.setdefault('placeholder', self.placeholder)
        return super(PlaceholderMixin, self).__call__(**kwargs)


@public
class DateTimeField(fields.DateTimeField):
    widget = DateTimeInput()


@public
class DateField(fields.DateField):
    widget = DateInput()


@public
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


@public
class IntegerField(fields.IntegerField):
    widget = NumberInput()


@public
class FloatField(fields.FloatField):
    widget = NumberInput()


@public
class DecimalField(fields.DecimalField):
    widget = NumberInput()


@public
class StringField(PlaceholderMixin, fields.StringField):
    widget = TextInput()


@public
class TextField(PlaceholderMixin, fields.TextField):
    widget = TextInput()


@public
class SearchField(StringField):
    widget = SearchInput()


@public
class TelephoneField(StringField):
    widget = TelephoneInput()


@public
class URLField(StringField):
    widget = URLInput()


@public
class EmailField(StringField):
    widget = EmailInput()


@public
class PasswordField(PlaceholderMixin, fields.PasswordField):
    widget = PasswordInput()


@public
class BooleanField(DummyLabelMixin, fields.BooleanField):
    def __call__(self, **kwargs):
        require_class('checkbox', kwargs)
        return self.label.label(text=(self.widget(self)+self.label.text),
                                **kwargs)


@public
class RadioField(fields.RadioField):
    widget = RadioListWidget()
    option_widget = RadioInput()


@public
class ButtonField(DummyLabelMixin, fields.Field):
    widget = Button()


@public
class SubmitButtonField(ButtonField):
    widget = SubmitButton()


@public
class ButtonInputField(DummyLabelMixin, fields.SubmitField):
    widget = ButtonInput()


@public
class SubmitField(ButtonInputField):
    widget = SubmitInput()

