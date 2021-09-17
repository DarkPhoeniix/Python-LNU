
from selenium import webdriver
import web_scrapper
import database_io

# using Google Chrome as webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path=r'C:\geckodriver\chromedriver.exe')

# site of Ministry of Finance
driver.get("https://minfin.com.ua/ua/currency/")

database_io.print_data_to_file(web_scrapper.get_usd_exchange_rate(driver), r'database_USD.txt')
database_io.print_data_to_file(web_scrapper.get_eur_exchange_rate(driver), r'database_EUR.txt')
database_io.print_data_to_file(web_scrapper.get_rub_exchange_rate(driver), r'database_RUB.txt')

driver.close()
