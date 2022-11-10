import requests
import pandas as pd


def prod_fetch_data():
    URL = "https://api.apilayer.com/exchangerates_data/latest"
    API_KEY = "Pyw0ruossZ93mWZmrFvaGlvIUgb9XUZD"
    MAX_RATE = 10

    payload = {}
    headers = {
        "apikey": API_KEY
    }

    response = requests.request("GET", URL, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    df = pd.json_normalize(response.json()['rates']).transpose()
    newDF = df[df[0] < MAX_RATE]
    return newDF.index

