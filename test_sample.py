from dev import mainDev
from prod import mainProd


# run -  pytest -q test_sample.py  - in terminal for testing


class TestClass:

    # pass
    def test_one(self):
        actual = mainDev.dev_fetch_data()
        expected = ['AED', 'ANG', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BGN', 'BHD', 'BMD',
                    'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BYN', 'BZD', 'CAD', 'CHF', 'CLF',
                    'CNY', 'CUC', 'DKK', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GIP',
                    'GTQ', 'HKD', 'HRK', 'ILS', 'IMP', 'JEP', 'JOD', 'KWD', 'KYD', 'LTL',
                    'LVL', 'LYD', 'MOP', 'MYR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PLN',
                    'QAR', 'RON', 'SAR', 'SBD', 'SGD', 'SHP', 'SVC', 'TMT', 'TND', 'TOP',
                    'TTD', 'USD', 'WST', 'XAG', 'XAU', 'XCD', 'XDR']

        assert all([a == b for a, b in zip(actual, expected)])

    # fails
    def test_two(self):
        actual = mainDev.dev_fetch_data()
        expected = [
            'CNY', 'CUC', 'DKK', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GIP',
            'GTQ', 'HKD', 'HRK', 'ILS', 'IMP', 'JEP', 'JOD', 'KWD', 'KYD', 'LTL',
            'LVL', 'LYD', 'MOP', 'MYR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PLN',
            'QAR', 'RON', 'SAR', 'SBD', 'SGD', 'SHP', 'SVC', 'TMT', 'TND', 'TOP',
            'TTD', 'USD', 'WST', 'XAG', 'XAU', 'XCD', 'XDR']

        assert all([a == b for a, b in zip(actual, expected)])
