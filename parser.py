import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


class Parser():
    def __init__(self, args):

        chrome_options = Options()
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome(options=chrome_options) 

        if args.name:
            self.name = args.name
    def get_reviews(self, name="test"):
        self.driver.get("https://www.google.com/maps")
        time.sleep(5)

        # Например, выполнить поиск
        search_box = self.driver.find_element(By.ID, "searchboxinput")
        print(search_box)
        search_box.send_keys(name)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        # Ожидание
        self.driver.implicitly_wait(5)

        # Закрытие браузера


if __name__ == "__main__":
    arg = argparse.ArgumentParser()


    arg.add_argument(
            '--name',
            type = str,
            required = True,
            help = "type a place name for searching"
            )
    arg.add_argument(
            '--restaurant',
            type = str,
            required = False,
            help = "For search in list of restautants"
            )
    arg.add_argument(
            '--hotel',
            type = str,
            required = False,
            help = "For search in list of hotels"
            )
    arg.add_argument(
            '--todo',
            type = str,
            required = False,
            help = "For search in list of things to do"
            )
    arg.add_argument(
            '--museum',
            type = str,
            required = False,
            help = "For search in list of museum"
            )
    arg.add_argument(
            '--transit',
            type = str,
            required = False,
            help = "For search in list of transit"
            )
    arg.add_argument(
            '--pharma',
            type = str,
            required = False,
            help = "For search in list of pharmacies"
            )
    arg.add_argument(
            '--atm',
            type = str,
            required = False,
            help = "For search in list of ATMs"
            )
    args = arg.parse_args()
    parser = Parser(args)
    parser.get_reviews()
