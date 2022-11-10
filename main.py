import requests
import pandas as pd
from dev import mainDev
from prod import mainProd


def fetch_data(is_dev):
    print(mainDev.dev_fetch_data()) if is_dev is True else print(mainProd.prod_fetch_data())


if __name__ == '__main__':
    fetch_data(True)


