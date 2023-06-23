from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from forex_python.bitcoin import BtcConverter

b = BtcConverter()
c = CurrencyRates()
d = CurrencyCodes()

print("USD/TRY Rate:")
print(d.get_symbol('USD'),"/",d.get_symbol('TRY'))
print(c.get_rate('USD', 'TRY'))

print("Bitcoin/USD Rate:")
print(b.get_latest_price('USD'))

print("Bitcoin/TRY Rate:")
print(b.get_latest_price('TRY'))





