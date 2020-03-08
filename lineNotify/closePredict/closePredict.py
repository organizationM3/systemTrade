import requests
import configparser

def lambda_handler(event, context):
    url, access_token = init()
    payload = createMessage()
    headers = {'Authorization': 'Bearer ' + access_token}
    requests.post(url, headers=headers, params=payload,)


def init():
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')
    url = config_ini['LINE_NOTIFY']['URL']

    credential_ini = configparser.ConfigParser()
    credential_ini.read('credential.ini', encoding='utf-8')
    access_token = credential_ini['TOKEN']['LINE_ACCESS_TOKEN']

    return url, access_token


def createMessage():
    message = '''
これはテストです。'''
    payload = {'message': message}

    return payload


if __name__ == "__main__":
    lambda_handler(1, 1)