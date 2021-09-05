from selenium import webdriver
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

today_date = date.today()

database_EUR = open(r"database_EUR.txt", "a+")
database_USD = open(r"database_USD.txt", "a+")
database_RUB = open(r"database_RUB.txt", "a+")

options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path=r'C:\geckodriver\chromedriver.exe')

driver.get("https://minfin.com.ua/ua/currency/")


def get_USD_exchange_rate():
    USD_exchange_rate = [["PrivatBank"], ["Oschadbank"], ["Raiffeisen Bank"]]

    USD_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[1]/td[3]').text
    )
    USD_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[1]/td[5]').text
    )

    USD_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[2]/td[3]').text
    )
    USD_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[2]/td[5]').text
    )

    USD_exchange_rate[2].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[4]/td[3]').text
    )
    USD_exchange_rate[2].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[4]/td[5]').text
    )

    return USD_exchange_rate


def get_EUR_exchange_rate():
    driver.find_element_by_css_selector(\
        'body > main > div.mfz-container > div > div.mfz-col-content > div > \
        section.currency-main.currency-main--content > div > div.mfm-tab-menu.js-change-tab > a:nth-child(2)'\
        ).click()

    EUR_exchange_rate = [["PrivatBank"], ["Oschadbank"], ["Raiffeisen Bank"]]

    EUR_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[2]').text
    )
    EUR_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[4]').text
    )

    EUR_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[2]/td[2]').text
    )
    EUR_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[2]/td[4]').text
    )

    EUR_exchange_rate[2].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[4]/td[2]').text
    )
    EUR_exchange_rate[2].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[4]/td[4]').text
    )

    return EUR_exchange_rate


def get_RUB_exchange_rate():
    RUB_exchange_rate = [["PrivatBank"], ["Oschadbank"], ["Raiffeisen Bank"]]
    driver.find_element_by_css_selector(\
        'body > main > div.mfz-container > div > div.mfz-col-content > div > \
        section.currency-main.currency-main--content > div > div.mfm-tab-menu.js-change-tab > a:nth-child(3)'\
        ).click()
    RUB_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[1]/td[2]').text
    )
    RUB_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[1]/td[4]').text
    )

    RUB_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[2]/td[2]').text
    )
    RUB_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[2]/td[4]').text
    )

    RUB_exchange_rate[2].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[4]/td[2]').text
    )
    RUB_exchange_rate[2].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[4]/td[4]').text
    )

    return RUB_exchange_rate


def print_data_to_file(data, file):
    file.write(today_date.strftime("%d/%m/%Y") + '\n')
    for L in data:
        for line in L:
            file.write(line + '\t')
        file.write('\n')


print_data_to_file(get_USD_exchange_rate(), database_USD)
get_EUR_exchange_rate()
get_RUB_exchange_rate()

database_USD.close()
database_EUR.close()
database_RUB.close()
