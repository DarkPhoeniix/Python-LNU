
from selenium import webdriver
from struct_exchange_rate import ExchangeRateForDay


def get_usd_exchange_rate(driver: webdriver):
    usd_exchange_rate = ExchangeRateForDay('USD')

    # get rate for PrivatBank by xpath
    usd_exchange_rate.set_buy_rate('PrivatBank',
        float(driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[1]/td[3]').text)
    )
    usd_exchange_rate.set_sell_rate('PrivatBank',
        float(driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[1]/td[5]').text)
    )

    # get rate for Oschadbank by xpath
    usd_exchange_rate.set_buy_rate('Oschadbank',
        float(driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[2]/td[3]').text)
    )
    usd_exchange_rate.set_sell_rate('Oschadbank',
        float(driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[2]/td[5]').text)
    )

    # get rate for Raiffeizen Bank by xpath
    usd_exchange_rate.set_buy_rate('Raiffeizen Bank',
        float(driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[4]/td[3]').text)
    )
    usd_exchange_rate.set_sell_rate('Raiffeizen Bank',
        float(driver.find_element_by_xpath('//*[@id="smTable"]/tbody/tr[4]/td[5]').text)
    )

    return usd_exchange_rate


def get_eur_exchange_rate(driver: webdriver):
    # change table to make hidden elements visible for reading
    driver.find_element_by_css_selector(
        'body > main > div.mfz-container > div > div.mfz-col-content > div > \
        section.currency-main.currency-main--content > div > div.mfm-tab-menu.js-change-tab > a:nth-child(2)'
        ).click()

    eur_exchange_rate = ExchangeRateForDay('EUR')

    # get rate for PrivatBank by xpath
    eur_exchange_rate.set_buy_rate('PrivatBank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[2]').text)
    )
    eur_exchange_rate.set_sell_rate('PrivatBank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[4]').text)
    )

    # get rate for Oschadbank by xpath
    eur_exchange_rate.set_buy_rate('Oschadbank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[2]/td[2]').text)
    )
    eur_exchange_rate.set_sell_rate('Oschadbank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[2]/td[4]').text)
    )

    # get rate for Raiffeizen Bank by xpath
    eur_exchange_rate.set_buy_rate('Raiffeizen Bank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[4]/td[2]').text)
    )
    eur_exchange_rate.set_sell_rate('Raiffeizen Bank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[4]/td[4]').text)
    )

    return eur_exchange_rate


def get_rub_exchange_rate(driver: webdriver):
    # change table to RUB currency to make hidden elements visible for reading
    driver.find_element_by_css_selector(
        'body > main > div.mfz-container > div > div.mfz-col-content > div > \
        section.currency-main.currency-main--content > div > div.mfm-tab-menu.js-change-tab > a:nth-child(3)'
        ).click()

    rub_exchange_rate = ExchangeRateForDay('RUB')

    # get rate for PrivatBank by xpath
    rub_exchange_rate.set_buy_rate('PrivatBank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[1]/td[2]').text)
    )
    rub_exchange_rate.set_sell_rate('PrivatBank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[1]/td[4]').text)
    )

    # get rate for Oschadbank by xpath
    rub_exchange_rate.set_buy_rate('Oschadbank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[2]/td[2]').text)
    )
    rub_exchange_rate.set_sell_rate('Oschadbank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[2]/td[4]').text)
    )

    # get rate for Raiffeizen Bank by xpath
    rub_exchange_rate.set_buy_rate('Raiffeizen Bank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[4]/td[2]').text)
    )
    rub_exchange_rate.set_sell_rate('Raiffeizen Bank',
        float(driver.find_element_by_xpath('//*[@id="DataTables_Table_1"]/tbody/tr[4]/td[4]').text)
    )

    return rub_exchange_rate
