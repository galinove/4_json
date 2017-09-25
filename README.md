# Prettify JSON

Скрипт используется для красивового вывода в коносли файлов .json
Скрипт в файле pprint_json.py

# Quickstart

Для работы со скриптом следует использовать pprint_json_test.py

windows 7 64b , Python 3.5:

```#!bash

import pprint_json

json_file = pprint_json.load_data(%path to file%)
pprint_json.pretty_print_json(json_file)
```
```
[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Кунцево",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
......
]
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
