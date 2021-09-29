
import datetime
from selenium import webdriver

from database_io import read_data_from_file, print_data_to_file
from plot_drawer import draw_plot
from datetime import date
from web_scrapper import get_eur_exchange_rate, get_rub_exchange_rate, get_usd_exchange_rate

print("print 'help' to read manual")
while True:
    command_line = input().split()
    if command_line[0] == "read" and command_line[1] == "data":
        file = open(r'database_USD.txt', 'r')
        if datetime.datetime.strptime(file.readlines()[-4][0:10], '%d/%m/%Y').date() != date.today():
            # using Google Chrome as webdriver
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            driver = webdriver.Chrome(options=options, executable_path=r'C:\geckodriver\chromedriver.exe')

            # site of Ministry of Finance
            driver.get("https://minfin.com.ua/ua/currency/")

            print_data_to_file(get_usd_exchange_rate(driver), r'database_USD.txt')
            print_data_to_file(get_eur_exchange_rate(driver), r'database_EUR.txt')
            print_data_to_file(get_rub_exchange_rate(driver), r'database_RUB.txt')

            driver.close()
        print("Data is up-to-date")
    elif command_line[0] == 'help':
        print('''Available commands:
    help - show this manual
    read data - read today's exchange rate and write to file
    show <currency> <start_date> <end_date> - show data table for specified dates
        available currency: USD, EUR, RUB
        date format: day/month/year
    exit - exit program''')
    elif command_line[0] == 'show':
        try:
            start_date = datetime.datetime.strptime(command_line[2], "%d/%m/%Y").date()
            end_date = datetime.datetime.strptime(command_line[3], "%d/%m/%Y").date()
            if command_line[1] == 'USD':
                draw_plot(start_date,
                          end_date,
                          read_data_from_file('USD', r'database_USD.txt'))
            elif command_line[1] == 'EUR':
                draw_plot(start_date,
                          end_date,
                          read_data_from_file('EUR', r'database_EUR.txt'))
            elif command_line[1] == 'RUB':
                draw_plot(start_date,
                          end_date,
                          read_data_from_file('RUB', r'database_RUB.txt'))
            else:
                print("Invalid currency name")
        except:
            print("Invalid dates: " + command_line[2] + ' ' + command_line[3])
    elif command_line[0] == 'exit':
        exit()
    else:
        print("Unknown command: ", end='')
        for i in command_line:
            print(i + ' ', end='')
        print()
