from flask import Flask, render_template, request, redirect, session

# import forex classes
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError

app = Flask(__name__)

# set a fake 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'USAFA1993-CS-29_Black_Panthers'

# Variables for objects created from forex class methods
rate = CurrencyRates()
code = CurrencyCodes()


@app.route('/')
def start_page():
    """ This is the initial home page containing the currency form """

    return render_template('index.html')


@app.route('/error')
def get_error():
    """ Display the home page with error message """

    msg = session['msg']
    return render_template('error.html', msg=msg)


@app.route('/convert', methods=['POST'])
def convert_currency():
    """ Convert the currencies from the currency form """

    from_curr = request.form['from-curr'].upper()
    to_curr = request.form['to-curr'].upper()
    amount_form = request.form['amount']

    # Error handling if the amount is not a number
    try:
        amount = float(request.form['amount'])
    except ValueError:
        session['msg'] = f'{amount_form} is not a valid number.'
        return redirect('/error')

    # Error handling if country code does not exist
    try:
        result = rate.convert(from_curr, to_curr, amount)
    except RatesNotAvailableError:

        # get_symbol is a method in the CurrencyCodes class in converter.py
        if code.get_symbol(from_curr) is None:
            session['msg'] = f'{from_curr} is not a valid currency code'
        else:
            session['msg'] = f'{to_curr} is not a valid currency code'
        return redirect('/error')

    symbol = code.get_symbol(to_curr)
    session['result'] = result
    session['symbol'] = symbol
    return redirect('/result')


@app.route('/result')
def get_result():
    """ Display the result of the conversion """

    result = session['result']
    formatted_float = "{:.2f}".format(result)
    symbol = session['symbol']

    return render_template('result.html', result=formatted_float, symbol=symbol)
