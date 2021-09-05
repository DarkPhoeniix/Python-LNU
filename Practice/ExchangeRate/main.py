from selenium import webdriver
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# saving date to write in databases
today_date = date.today()

# opening different files for different currency
database_EUR = open(r"database_EUR.txt", "a+")
database_USD = open(r"database_USD.txt", "a+")
database_RUB = open(r"database_RUB.txt", "a+")

# using Google Chrome as webdriver
options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path=r'C:\geckodriver\chromedriver.exe')

# site of Ministry of Finance
driver.get("https://minfin.com.ua/ua/currency/")


def get_USD_exchange_rate():
    USD_exchange_rate = [["PrivatBank"], ["Oschadbank"], ["Raiffeisen Bank"]]

    # get rate for PrivatBank by xpath
    USD_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[1]/td[3]').text
    )
    USD_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[1]/td[5]').text
    )

    # get rate for Oschadbank by xpath
    USD_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[2]/td[3]').text
    )
    USD_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[2]/td[5]').text
    )

    # get rate for Raiffeizen Bank by xpath
    USD_exchange_rate[2].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[4]/td[3]').text
    )
    USD_exchange_rate[2].append(
        driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[4]/td[5]').text
    )

    return USD_exchange_rate


def get_EUR_exchange_rate():
    # change table to make hidden elements visible for reading
    driver.find_element_by_css_selector(\
        'body > main > div.mfz-container > div > div.mfz-col-content > div > \
        section.currency-main.currency-main--content > div > div.mfm-tab-menu.js-change-tab > a:nth-child(2)'\
        ).click()

    EUR_exchange_rate = [["PrivatBank"], ["Oschadbank"], ["Raiffeisen Bank"]]

    # get rate for PrivatBank by xpath
    EUR_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[2]').text
    )
    EUR_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[4]').text
    )

    # get rate for Oschadbank by xpath
    EUR_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[2]/td[2]').text
    )
    EUR_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[2]/td[4]').text
    )

    # get rate for Raiffeizen Bank by xpath
    EUR_exchange_rate[2].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[4]/td[2]').text
    )
    EUR_exchange_rate[2].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[4]/td[4]').text
    )

    return EUR_exchange_rate


def get_RUB_exchange_rate():
    # change table to make hidden elements visible for reading
    driver.find_element_by_css_selector( \
        'body > main > div.mfz-container > div > div.mfz-col-content > div > \
        section.currency-main.currency-main--content > div > div.mfm-tab-menu.js-change-tab > a:nth-child(3)' \
        ).click()

    RUB_exchange_rate = [["PrivatBank"], ["Oschadbank"], ["Raiffeisen Bank"]]

    # get rate for PrivatBank by xpath
    RUB_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[1]/td[2]').text
    )
    RUB_exchange_rate[0].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[1]/td[4]').text
    )

    # get rate for Oschadbank by xpath
    RUB_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[2]/td[2]').text
    )
    RUB_exchange_rate[1].append(
        driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[2]/td[4]').text
    )

    # get rate for Raiffeizen Bank by xpath
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
print_data_to_file(get_EUR_exchange_rate(), database_EUR)
print_data_to_file(get_RUB_exchange_rate(), database_RUB)

database_USD.close()
database_EUR.close()
database_RUB.close()
