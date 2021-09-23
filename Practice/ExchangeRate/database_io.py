
from struct_exchange_rate import ExchangeRateForDay
from datetime import date, datetime

# saving date to write in databases
today_date = date.today()


# get struct of exchange rate and file to write to
# format:
# <date>
# <bank_1>  <buy_rate>  <sell_rate>
# <bank_2>  <buy_rate>  <sell_rate>
# <bank_3>  <buy_rate>  <sell_rate>
def print_data_to_file(data: ExchangeRateForDay, file_name: str):
    file = open(file_name, 'a+')
    file.write(today_date.strftime("%d/%m/%Y") + '\n')
    for k in data.exchange_rates:
        file.write(str(k) + '\t')
        for v in data.exchange_rates.get(k):
            file.write(str(f"{v:.{3}f}") + '\t')
        file.write('\n')
    file.close()


# read data about currency from specified file
# return list of struct_exchange_rate
def read_data_from_file(currency_name: str, file_name: str):
    file = open(file_name, 'r')
    content = file.readlines()
    data_list = []
    for i in range(0, len(content), 4):
        currency = ExchangeRateForDay(currency_name)
        currency.set_today_date(datetime.strptime(content[i][0:10], "%d/%m/%Y"))
        currency.set_buy_rate(content[i + 1][0:10], float(content[i + 1][11:17]))
        currency.set_sell_rate(content[i + 1][0:10], float(content[i + 1][18:24]))
        currency.set_buy_rate(content[i + 2][0:10], float(content[i + 2][11:17]))
        currency.set_sell_rate(content[i + 2][0:10], float(content[i + 2][18:24]))
        currency.set_buy_rate(content[i + 3][0:15], float(content[i + 3][16:22]))
        currency.set_sell_rate(content[i + 3][0:15], float(content[i + 3][23:29]))
        data_list.append(currency)

    return data_list
