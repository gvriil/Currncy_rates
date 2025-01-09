import requests
import json
from datetime import datetime

def get_currency_rate(currency: str) -> float:
    api_key = '7kyvJ00R8oAgUz1w64q5PsAJ9JTWm44c'  # Ваш новый API ключ
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
    print("Введите название валюты, металла или биткойна (например, USD, EUR, XAU, BTC):")
    while True:
        currency = input("Введите название валюты, металла или биткойна: ").strip().upper()
        try:
            rate = get_currency_rate(currency)
            print(f"Курс {currency} к рублю: {rate:.2f}")
            save_to_json(currency, rate)
        except ValueError as e:
            print(e)

        action = input("Введите 'продолжить' для продолжения или 'выйти' для выхода: ").strip().lower()
        if action == 'выйти':
            break

if __name__ == '__main__':
    main()
