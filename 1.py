import requests
import json

# 设置请求头
headers = {
    'X-Client-Token': 'e77b7e2f43db41bb95b17a2a11581a38',
    'X-Client-Platform': 'android',
    'X-Client-Version': '3.64.4',
    'User-Agent': 'MijnSimyo/3.64.4 (Linux; Android 13; Scale/2.75)',
    'Content-Type': 'application/json; charset=UTF-8',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
}

# 设置请求数据
data = {
    'password': '',
    'phoneNumber': ''
}

# 发送POST请求获取sessionToken
response = requests.post('https://appapi.simyo.nl/simyoapi/api/v1/sessions', headers=headers, data=json.dumps(data))
response_json = response.json()
print(response_json)  # 调试代码，打印API返回的JSON
sessionToken = response_json.get('result').get('sessionToken')

# 设置请求头，加入sessionToken
headers['X-Session-Token'] = sessionToken

# 发送GET请求获取activationCode
response = requests.get('https://appapi.simyo.nl/simyoapi/api/v1/esim/get-by-customer', headers=headers)
response_json = response.json()
print(response_json)  # 打印API返回的JSON

