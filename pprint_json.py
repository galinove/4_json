import json
import sys


def load_data(filepath):
    with open(filepath, encoding="utf8") as json_file_utf8:
        json_file_utf8_content = json.loads(json_file_utf8.read())
    return json_file_utf8_content


def pretty_print_json(json_file_utf8_content):
    print(json.dumps(json_file_utf8_content, indent=4, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = (sys.argv[1].replace("'", "")).replace("\|", "/")
    else:
        filepath = (input('Введите путь к файлу .json: ').replace("'", "")).replace("\|", "/")
    try:
        pretty_print_json(load_data(filepath))
    except:
        print('File not found or does not exist')
