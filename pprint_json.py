import json


def load_data(filepath):

    f = open(filepath, encoding="utf8")
    d = json.loads(f.read())
    f.close()
    return d


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    print("this script can't be executed as non-imported")
