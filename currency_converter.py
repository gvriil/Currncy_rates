import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

# Соответствие цифр и буквенных кодов валют
CURRENCY_MAPPING = {
    '1': 'USD',
    '2': 'EUR',
    '3': 'JPY',
    '4': 'GBP',
    '5': 'AUD',
    '6': 'CAD',
    '7': 'CHF',
    '8': 'CNY',
    '9': 'XAU',  # Золото
    '0': 'BTC'   # Биткойн
}

def get_currency_rate(currency: str) -> float:
    api_key = os.getenv('API_KEY')  # Получение API ключа из переменных окружения
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency.upper()}"
    headers = {
        "apikey": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # print("API Response:", data)  # Добавьте эту строку для отладки
        if 'rates' in data and 'RUB' in data['rates']:
            return round(data['rates']['RUB'], 2)
        else:
            raise ValueError("Курс валюты к рублю не найден")
    else:
        # print("API Error Response:", response.text)  # Добавьте эту строку для отладки
        raise ValueError("Ошибка при получении данных от API")

def save_to_json(currency: str, rate: float):
    data = {
        'time': datetime.now().isoformat(),
        'currency': currency.upper(),
        'rate': rate
    }
    with open('currency.json', 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print("Введите код валюты (цифры от 1 до 9 или буквенное сокращение) или 'x' для выхода:")
    print("Соответствие цифр и валют:")
    for key, value in CURRENCY_MAPPING.items():
        print(f"{key}: {value}")

    while True:
        currency_input = input("Введите код валюты: ").strip().upper()
        if currency_input == 'X':
            break
        if currency_input in CURRENCY_MAPPING:
            currency = CURRENCY_MAPPING[currency_input]
        else:
            currency = currency_input
        try:
            rate = get_currency_rate(currency)
            print(f"Курс {currency} к рублю: {rate:.2f}")
            save_to_json(currency, rate)
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()
