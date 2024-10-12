import requests
import base64
import json


def get_data(config):
    print(config)
    url = f"https://data.mixpanel.com/api/2.0/export?project_id={config['project_id']}&from_date={config['from_date']}&to_date={config['to_date']}"
    
    if 'where' in config and config['where']:
        url += f"&where={config['where']}"

    if 'limit' in config and config['limit']:
        url += f"&limit={config['limit']}"


    headers = {
        "accept": "text/plain",
        "authorization": "Basic " + base64.b64encode(f"{config['authorization']['username']}:{config['authorization']['password']}".encode()).decode()
    }

    if 'event' in config:
        payload = {"event": json.dumps(config['event'])}
        response = requests.get(url, headers=headers, params=payload)
    else:
        response = requests.get(url, headers=headers)

    return response.text


if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    result = get_data(config)

    print(result)
