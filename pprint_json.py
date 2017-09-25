import json


def load_data(filepath):

    json_file_utf8 = open(filepath, encoding="utf8")
    json_file_utf8_content = json.loads(json_file_utf8.read())
    json_file_utf8.close()
    return json_file_utf8_content


def pretty_print_json(json_file_utf8_content):
    print(json.dumps(json_file_utf8_content, indent=4, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    print("this script can't be executed as non-imported")
