# Генератор QR-кодов

Простое приложение на Python для создания QR-кодов из текстовых данных, введенных пользователем.
Использует библиотеки pyqrcode и png для генерации и сохранения QR-кодов в формате PNG.

## Установка

Для работы приложения необходимо установить Python и необходимые зависимости. Убедитесь, что у вас уже установлен
Python,
а затем выполните следующие команды в терминале или командной строке:

pip install pyqrcode
pip install pypng

## Использование

Запустите скрипт `zadacha.py` через командную строку или терминал, используя Python:

python qr_generator.py
После запуска откроется графический интерфейс приложения, где вы сможете ввести текст или URL, который необходимо
преобразовать в QR-код. Введите нужные данные в текстовое поле и нажмите кнопку "Создать код". QR-код будет
автоматически
сгенерирован и сохранен в той же директории, где находится скрипт, под именем `code.png`.

## Зависимости

- Python (3.6 или выше)
- pyqrcode
- pypng
