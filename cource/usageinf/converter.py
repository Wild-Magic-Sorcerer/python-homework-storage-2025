from cource.usageinf.exchange import ExchangeRate


class Converter:
    def __init__(self, exchange_rate: ExchangeRate, commission_rate: float):
        self.exchange_rate = exchange_rate
        self.commission_rate = commission_rate

    def convert(self, amount: float, from_code: str, to_code: str) -> float:
        if from_code not in self.exchange_rate.currencies or to_code not in self.exchange_rate.currencies:
            raise ValueError("Одна из валют не найдена.")

        from_currency = self.exchange_rate.currencies[from_code]
        to_currency = self.exchange_rate.currencies[to_code]

        amount_in_base = amount / from_currency.rate
        converted_amount = amount_in_base * to_currency.rate

        commission = converted_amount * (self.commission_rate / 100)
        return converted_amount - commission