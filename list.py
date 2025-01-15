import requests
from bs4 import BeautifulSoup

# 目标URL
url = 'https://example.com'

# 发送HTTP请求获取网页内容
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 获取网页标题
    title = soup.title.string
    print(f"Title: {title}")

    # 获取所有链接
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href:
            print(href)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
