import json
import sys

from app import App


def main():
    settings_path = "./server.json"
    if len(sys.argv) >= 2:
        settings_path = sys.argv[1]

    try:
        with open(settings_path, "r") as fistream:
            data = json.load(fistream)
        App(
            saddr=(data["server"]["ip"], data["server"]["port"]),
            caddr=data["client"]
        ).run()

    except FileNotFoundError:
        with open(settings_path, "w") as fostream:
            json.dump({"server": {"ip": "127.0.0.1", "port": 8080}, "client": "127.0.0.1"}, fostream)
    except KeyError as err:
        print(f"Parameter '{str(err)}' unfilled in settings file")


if __name__ == '__main__':
    main()
