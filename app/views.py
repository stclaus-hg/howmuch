from app import app
from app.forms import CalculatePriceForm
from flask import request, render_template
from decimal import Decimal, getcontext

getcontext().prec = 2

inflation = {
    2000: Decimal(1.258),
    2001: Decimal(1.061),
    2002: Decimal(0.994),
    2003: Decimal(1.082),
    2004: Decimal(1.123),
    2005: Decimal(1.103),
    2006: Decimal(1.116),
    2007: Decimal(1.166),
    2008: Decimal(1.223),
    2009: Decimal(1.123),
    2010: Decimal(1.091),
    2011: Decimal(1.046),
    2012: Decimal(0.998),
    2013: Decimal(1.005),
    2014: Decimal(1.249),
}

def calculate_price(source_year, source_price, result_year):
    res = source_price
    if source_year < result_year:
        for year in range(source_year, result_year):
            res *= inflation[year]
            print Decimal(res)
    else:
        for year in range(result_year, source_year):
            res /= inflation[year]
            print Decimal(res)
    return res


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CalculatePriceForm()
    result = None
    if form.validate_on_submit():
        result = calculate_price(source_year=form.source_year.data,
                                  source_price=form.source_price.data,
                                  result_year=form.result_year.data)

    return render_template('index.html', form=form, result=result)