import requests
import json
import qrcode
from PIL import Image

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
    'password': 'xxxxx',
    'phoneNumber': '06xxxxxx'
}

# 发送POST请求获取sessionToken
response = requests.post('https://appapi.simyo.nl/simyoapi/api/v1/sessions', headers=headers, data=json.dumps(data))
response_json = response.json()
sessionToken = response_json.get('result').get('sessionToken')

# 设置请求头，加入sessionToken
headers['X-Session-Token'] = sessionToken

# 发送GET请求获取activationCode
response = requests.get('https://appapi.simyo.nl/simyoapi/api/v1/esim/get-by-customer', headers=headers)
response_json = response.json()
activationCode = response_json.get('result').get('activationCode')

# 添加"LPA:"前缀
activationCode = 'LPA:' + activationCode

# 生成二维码
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(activationCode)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# 调整二维码大小
img.thumbnail((250, 250))

# 将二维码转换为字符画
width, height = img.size
scale = 1
if width > 80:
    scale = width // 80 + 1
    width //= scale
    height //= scale
img = img.resize((width, height))
pixels = img.load()
output = ""
for y in range(height):
    for x in range(width):
        output += " " if pixels[x, y] == 255 else "█"
    output += "\n"

# 输出结果
print('sessionToken:', sessionToken)
print('activationCode:', activationCode)
print('二维码已生成：')
print(output)

# 显示二维码
img.show()
