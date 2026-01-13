from exchange import ExchangeRate
from converter import Converter

exchange = ExchangeRate()

exchange.add_currency("USD", "Доллар США", 1.0)
exchange.add_currency("EUR", "Евро", 0.85)
exchange.add_currency("RUB", "Российский рубль", 85.0)

exchange.update_rate("EUR", 0.88)

print(exchange.get_rates())

converter = Converter()

result = converter.convert(100, "USD", "EUR")
print(f"100 USD в EUR: {result:.2f} EUR")