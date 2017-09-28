import requests


def get_home_key(grant_type, client_id, username, password):
    url = 'http://login.test.homegate.io/auth/realms/homegate/protocol/openid-connect/token'
    payload = {
        'grant_type': grant_type,
        'client_id': client_id,
        'username': username,
        'password': password
    }

    response = requests.post(url=url, data=payload)

    if response.status_code is 200:
        return response.json()
    else:
        raise requests.exceptions.RequestException(response.json())


def get_home_info(access_token, home_id):
    url = 'http://home-test-api.datek.no/homes/' + home_id
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/hal+json'
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code is 200:
        return response.json()
    else:
        raise requests.exceptions.RequestException(response.json())


def do_device_command(access_token, home_id, device_id, endpoint, cluster, cmd, payload=None):
    url = 'http://home-test-api.datek.no/homes/' + str(home_id) + '/devices/' + str(device_id) + '/endpoints/' + str(endpoint) + '/clusters/' + str(cluster) + '/cmd/' + str(cmd)
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/hal+json'
    }

    response = requests.post(url=url, headers=headers, data=payload)

    if response.status_code is 200:
        return "done"
    else:
        raise requests.exceptions.RequestException(response.json())
