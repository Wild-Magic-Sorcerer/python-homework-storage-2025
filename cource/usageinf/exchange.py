from currency import Currency

class ExchangeRate:
    def __init__(self):
        self.currencies = {}

    def add_currency(self, code: str, name: str, rate: float):
        if code in self.currencies:
            raise ValueError("Валюта уже добавлена.")
        self.currencies[code] = Currency(code, name, rate)

    def update_rate(self, code: str, new_rate: float):
        if code not in self.currencies:
            raise ValueError("Валюта не найдена.")
        self.currencies[code].rate = new_rate

    def get_rates(self):
        return {code: currency.rate for code, currency in self.currencies.items()}