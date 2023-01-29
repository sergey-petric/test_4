import requests
import re


def get_ip_address():
    url = 'https://ifconfig.me/'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/108.0.0.0 YaBrowser/23.1.1.1135 Yowser/2.5 Safari/537.36'}

    request = requests.get(url, headers=header)
    print(f'Результат выполнения Get запроса: {request.ok}')

    pattern = r'(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((2[0-4]\d)|(25[0-5])|(1\d{2})|(\d{1,2}))'

    print(f'Текущий IP-адрес компьютера: {re.search(pattern, request.text).group()}')


get_ip_address()
