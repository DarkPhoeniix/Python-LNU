
from struct_exchange_rate import ExchangeRateForDay


def parse_data(exchange_rate: [ExchangeRateForDay]):
    parsed_data = [[[], []], [[], []], [[], []]]
    for i in exchange_rate:
        parsed_data[0][0].append(i.exchange_rates.get('PrivatBank')[0])
        parsed_data[0][1].append(i.exchange_rates.get('PrivatBank')[1])
        parsed_data[1][0].append(i.exchange_rates.get('Oschadbank')[0])
        parsed_data[1][1].append(i.exchange_rates.get('Oschadbank')[1])
        parsed_data[2][0].append(i.exchange_rates.get('Raiffeisen Bank')[0])
        parsed_data[2][1].append(i.exchange_rates.get('Raiffeisen Bank')[1])
    return parsed_data

