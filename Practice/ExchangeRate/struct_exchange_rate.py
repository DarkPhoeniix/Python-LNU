
from datetime import date


class ExchangeRateForDay:
    def __init__(self, currency: str):
        self.currency = currency
        self.exchange_rates = {"PrivatBank": [0, 0], "Oschadbank": [0, 0], "Raiffeisen Bank": [0, 0]}

    def set_today_date(self, today_date: date):
        self.today = today_date.strftime("%d/%m/%Y")

    def set_buy_rate(self, bank_name: str, buy_rate: float):
        self.exchange_rates[bank_name][0] = buy_rate

    def set_sell_rate(self, bank_name: str, sell_rate: float):
        self.exchange_rates[bank_name][1] = sell_rate
