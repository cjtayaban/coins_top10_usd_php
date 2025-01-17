from project import generate_filename, coins_usd, coins_php, parse_json, generate_csv, generate_bar_graph
import pytest
from datetime import date
from unittest.mock import patch
import os

def test_generate_filename():
    current_date = date.today()
    expected_filename = "coins_top10_usd_php_" + current_date.strftime("%Y%m%d")
    assert generate_filename() == expected_filename, f"Expected {expected_filename} but got {generate_filename()}"

@patch('project.requests.get')
def test_coins_usd(mock_get):
    mock_response_data = [
        {'id': 'bitcoin', 'name': 'Bitcoin', 'symbol': 'btc', 'current_price': 1},
        {'id': 'ethereum', 'name': 'Ethereum', 'symbol': 'eth', 'current_price': 1},
        {'id': 'ripple', 'name': 'XRP', 'symbol': 'xrp', 'current_price': 1},
        {'id': 'tether', 'name': 'Tether', 'symbol': 'usdt', 'current_price': 1},
        {'id': 'binancecoin', 'name': 'BNB', 'symbol': 'bnb', 'current_price': 1},
        {'id': 'solana', 'name': 'Solana', 'symbol': 'sol', 'current_price': 1},
        {'id': 'dogecoin', 'name': 'Dogecoin', 'symbol': 'doge', 'current_price': 1},
        {'id': 'usd-coin', 'name': 'USDC', 'symbol': 'usdc', 'current_price': 1},
        {'id': 'cardano', 'name': 'Cardano', 'symbol': 'ada', 'current_price': 1},
        {'id': 'staked-ether', 'name': 'Lido Staked Ether', 'symbol': 'steth', 'current_price': 1}
    ]

    mock_get.return_value.json.return_value = mock_response_data
    mock_get.return_value.status_code = 200
    result = coins_usd()

    assert result == mock_response_data
    assert len(result) == 10

@patch('project.requests.get')
def test_coins_php(mock_get):
    mock_response_data = [
        {'id': 'bitcoin', 'name': 'Bitcoin', 'symbol': 'btc', 'current_price': 1},
        {'id': 'ethereum', 'name': 'Ethereum', 'symbol': 'eth', 'current_price': 1},
        {'id': 'ripple', 'name': 'XRP', 'symbol': 'xrp', 'current_price': 1},
        {'id': 'tether', 'name': 'Tether', 'symbol': 'usdt', 'current_price': 1},
        {'id': 'binancecoin', 'name': 'BNB', 'symbol': 'bnb', 'current_price': 1},
        {'id': 'solana', 'name': 'Solana', 'symbol': 'sol', 'current_price': 1},
        {'id': 'dogecoin', 'name': 'Dogecoin', 'symbol': 'doge', 'current_price': 1},
        {'id': 'usd-coin', 'name': 'USDC', 'symbol': 'usdc', 'current_price': 1},
        {'id': 'cardano', 'name': 'Cardano', 'symbol': 'ada', 'current_price': 1},
        {'id': 'staked-ether', 'name': 'Lido Staked Ether', 'symbol': 'steth', 'current_price': 1}
    ]

    mock_get.return_value.json.return_value = mock_response_data
    mock_get.return_value.status_code = 200
    result = coins_php()

    assert result == mock_response_data
    assert len(result) == 10

def test_parse_json():
    assert len(parse_json()) == 10

def test_generate_csv():
    generate_csv()
    expected_filename = generate_filename() + ".csv"
    assert os.path.exists(expected_filename)

def test_generate_bar_graph():
    generate_bar_graph()
    expected_filename = generate_filename() + ".pdf"
    assert os.path.exists(expected_filename)