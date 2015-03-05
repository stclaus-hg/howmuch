import sys
from app import app
from app.forms import CalculatePriceForm
from flask import request, render_template
from decimal import Decimal, getcontext
import csv
import os

getcontext().prec = 2

def load_inflation():
    path =  os.path.dirname(os.path.realpath(__file__))
    csv_path = os.path.join(path, '../inflation.csv')
    with open(csv_path) as inflation:
        reader = csv.reader(inflation, delimiter=',')
        return {int(row[0]):row[1] for row in reader}

inflation = load_inflation()
print inflation

def calculate_price(source_year, source_price, result_year):
    res = source_price
    if source_year < result_year:
        for year in range(source_year, result_year):
            res *= Decimal(inflation[year])
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