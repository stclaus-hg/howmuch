from flask.ext.wtf import Form
from flask.ext.wtf.form import _is_hidden
from wtforms import DateField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf.html5 import IntegerField

class CalculatePriceForm(Form):
    source_year = IntegerField('In year', description='Between 2000 and 2015 years',
                               validators=[DataRequired(), NumberRange(min=2000,
                                                                       max=2015,
                                                                       message='Year must be between 2000 and 2015.')])
    source_price = DecimalField('it was cost', validators=[DataRequired()])

    result_year = IntegerField('In Year', description='Between 2000 and 2015 years',
                               validators=[DataRequired(), NumberRange(min=2000,
                                                                       max=2015,
                                                                       message='Year must be between 2000 and 2015.')])

    def bound_fields(self):
        return [f for f in self if not _is_hidden(f)]