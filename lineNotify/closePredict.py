import requests
import configparser
from boto3.session import Session
import os

def lambda_handler(event, context):
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')
    print(os.getcwd())
    url = config_ini['LINE_NOTIFY']['URL']

    credential_ini = configparser.ConfigParser()
    credential_ini.read('credential.ini', encoding='utf-8')
    line_access_token = credential_ini['TOKEN']['LINE_ACCESS_TOKEN']
    aws_accress_key_id = \
        credential_ini['AWS']['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = \
        credential_ini['AWS']['AWS_SECRET_ACCESS_KEY']

    closePredictValue = getClosePredict(aws_accress_key_id,
                                        aws_secret_access_key)
    payload = createMessage(closePredictValue)
    headers = {'Authorization': 'Bearer ' + line_access_token}
    requests.post(url, headers=headers, params=payload,)


def getClosePredict(args_aws_accress_key_id, args_aws_secret_access_key):
    session = Session(aws_access_key_id=args_aws_accress_key_id,
                      aws_secret_access_key=args_aws_secret_access_key,
                      region_name='ap-northeast-1')
    s3 = session.client('s3')
    forecast = s3.get_object(Bucket='bucket-m3', Key='forecast.txt')
    return forecast['Body'].read().decode()


def createMessage(value):
    message = '予測値：' + value + ' USD/JPY'
    payload = {'message': message}
    return payload

