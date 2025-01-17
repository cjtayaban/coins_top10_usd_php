import csv
from datetime import date
import requests
import matplotlib.pyplot as plt

coins = []

def main():
    parse_json()
    generate_csv()
    generate_bar_graph()
    
def generate_filename():
    current_date = date.today()
    return "coins_top10_usd_php_" + current_date.strftime("%Y%m%d")

def coins_usd():
    url_usd = 'https://api.coingecko.com/api/v3/coins/markets'
    params_usd = {
        'sort': 'market_cap_desc',
        'vs_currency': 'usd',
        'per_page': 10
    }
    response_usd = requests.get(url_usd, params=params_usd)
    if response_usd.status_code == 200:
        return response_usd.json()
    else:
        raise requests.RequestException("Error occurred while making the API request")

def coins_php():
    url_php = 'https://api.coingecko.com/api/v3/coins/markets'
    params_php = {
        'sort': 'market_cap_desc',
        'vs_currency': 'php',
        'per_page': 10
    }
    response_php = requests.get(url_php, params=params_php)
    if response_php.status_code == 200:
        return response_php.json()
    else:
        raise requests.RequestException("Error occurred while making the API request")

def parse_json():
    for coin_usd, coin_php in zip(coins_usd(), coins_php()):
        coins.append({
            "ID": coin_usd['id'],
            "Name": coin_usd['name'],
            "Symbol": coin_usd['symbol'],
            "USD Price": coin_usd['current_price'],
            "PHP Price": coin_php['current_price']
        })
    return coins

def generate_csv():
    with open(generate_filename() + ".csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Symbol", "USD Price", "PHP Price"])
        writer.writeheader()
        for coin in coins:
            writer.writerow(coin)

def generate_bar_graph():
    categories = [coin["Symbol"] for coin in coins]
    php_values = [coin["PHP Price"] for coin in coins]
    plt.bar(categories, php_values)
    plt.title('Top 10 Coins Based on Market Cap')
    plt.xlabel('Coins')
    plt.ylabel('PHP Price')
    plt.savefig(generate_filename() + ".pdf")

if __name__ == "__main__":
    main()

