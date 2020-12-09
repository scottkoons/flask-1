from unittest import TestCase
from app import app, rates, codes
from flask import session


class ConverterTest(TestCase):
    """ Tests for the Currency Converter app.py """

    def test_home(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('Converting to', html)
            self.assertIn('Converting from', html)
            self.assertIn('Amount', html)

    def test_error(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['msg'] = 'This amount is not valid.'
            res = client.get('/error')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('This amount is not valid', html)

    def test_convert(self):
        with app.test_client() as client:
            res = client.post(
                '/convert', data={'from-curr': 'USD', 'to-curr': 'USD', 'amount': '100'})

            self.assertEqual(res.status_code, 302)
            self.assertEqual(session['result'], 100.00)
            self.assertEqual(session['symbol'], 'US$')

    def test_result(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['result'] = 123.547565
                change_session['symbol'] = '$'
            res = client.get('/result')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('$ 123.55', html)
