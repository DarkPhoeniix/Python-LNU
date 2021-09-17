
class ExchangeRateForDay:
    def __init__(self, currency):
        self.currency = currency
        self.exchange_rates = {"PrivatBank": [0, 0], "Oschadbank": [0, 0], "Raiffeisen Bank": [0, 0]}

    def set_buy_rate(self, bank_name, buy_rate):
        self.exchange_rates[bank_name][0] = buy_rate

    def set_sell_rate(self, bank_name, sell_rate):
        self.exchange_rates[bank_name][1] = sell_rate
