
# Currency Converter

## Описание

Currency Converter — это простое приложение на Python, которое позволяет пользователям получать текущие курсы валют, металлов и биткойна. Программа использует API для получения данных и сохраняет результаты в JSON-файл.

## Установка

### Требования

- Python 3.11
- Poetry (менеджер зависимостей)

### Шаги установки

1. **Клонируйте репозиторий**:
   ```sh
   git clone https://github.com/gvriil/Currncy_rates.git
   cd Currncy_rates
   ```

2. **Установите зависимости**:
   ```sh
   poetry install
   ```

3. **Создайте файл `.env` в корневой директории проекта и добавьте ваш API ключ**:
   ```env
   API_KEY=your_api_key_here
   ```

## Запуск

### Запуск через Poetry

1. **Запустите программу**:
   ```sh
   poetry run python currency_converter.py
   ```

### Запуск через бинарный файл

1. **Создайте бинарный файл**:
   - В корневой директории проекта создайте файл `run_currency_converter.sh` со следующим содержимым:
     ```sh
     #!/bin/zsh
     cd /Users/G/PycharmProjects/Curancy/currency_covertor
     poetry run python currency_converter.py
     ```

2. **Сделайте файл исполняемым**:
   ```sh
   chmod +x ~/run_currency_converter.sh
   ```

3. **Запустите программу через бинарный файл**:
   ```sh
   ~/run_currency_converter.sh
   ```

### Создание alias для удобного запуска

1. **Откройте файл конфигурации оболочки**:
   - Для `zsh`, откройте файл `~/.zshrc`.

2. **Добавьте alias**:
   - Добавьте следующую строку в конец файла:
     ```sh
     alias currency_rates='~/run_currency_converter.sh'
     ```

3. **Примените изменения**:
   ```sh
   source ~/.zshrc
   ```

4. **Запустите программу с помощью alias**:
   ```sh
   currency_rates
   ```

## Использование

1. **Запустите программу**.
2. **Следуйте инструкциям на экране**:
   - Введите код валюты (цифры от 1 до 9 или буквенное сокращение) или 'x' для выхода.
   - Программа выведет текущий курс к рублю и сохранит результат в файл `currency.json`.

### Соответствие цифр и валют:
- 1: USD
- 2: EUR
- 3: JPY
- 4: GBP
- 5: AUD
- 6: CAD
- 7: CHF
- 8: CNY
- 9: XAU (Золото)
- 0: BTC (Биткойн)

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности смотрите в файле [LICENSE](LICENSE).

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с автором проекта:

- **GitHub**: [gvriil](https://github.com/gvriil)
- **Email**: [0020992@gmail.com](mailto:0020992@gmail.com)

## Благодарности

Спасибо за использование Currency Converter! Надеюсь, этот инструмент будет полезен для вас.


### Объяснение секций

1. **Описание**: Краткое описание проекта.
2. **Установка**: Инструкции по установке зависимостей и настройке проекта.
3. **Запуск**: Инструкции по запуску программы через Poetry и бинарный файл.
4. **Создание alias**: Инструкции по созданию alias для удобного запуска программы.
5. **Использование**: Инструкции по использованию программы, включая соответствие цифр и валют.
6. **Лицензия**: Информация о лицензии проекта.
7. **Контакты**: Контактная информация автора проекта.
8. **Благодарности**: Благодарности пользователям и сообществу.

