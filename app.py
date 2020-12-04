from flask import Flask, render_template, request, redirect, session
# import forex objects
# from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError
from forex_python.converter import CurrencyRates, RatesNotAvailableError
# from forex_python.converter import CurrencyCodes
# from forex_python.bitcoin import BtcConverter


app = Flask(__name__)

# set a fake 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'USAFA1993-CS-29_Black_Panthers'

# rate = CurrencyRates()
# code = CurrencyCodes()


@app.route('/')
def hello_world():
    return 'Hello, Forex4!'
