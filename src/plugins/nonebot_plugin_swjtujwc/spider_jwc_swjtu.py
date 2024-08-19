# 爬取某个网站的所有图片
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 爬取西南交通大学教务处的通知
def SWJTU_scrape_notices():

    # 获取 HTML 内容
    def get_html_content(url, headers):
        response = requests.get(url=url, headers=headers)
        html_content = response.text
        return html_content

    # 提取所有通知的标题、时间和链接
    def extract_all_notices(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        notices = soup.find_all("div", {"class": "littleResultDiv"})
        result = []
        for notice in notices:
            title = notice.find("h3").text.strip()
            time = notice.find("span").text.strip()
            link = notice.find("a")["href"]
            result.append((title, time, link))
        return result

    # 提取第一个通知的标题、时间和链接
    def extract_first_notice(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        notice = soup.find("div", {"class": "littleResultDiv"})
        title = notice.find("h3").text.strip()
        time = notice.find("span").text.strip()
        link = notice.find("a")["href"]
        return (title, time, link)

    # url
    url = 'http://jwc.swjtu.edu.cn/vatuu/WebAction?setAction=newsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
    }

    # 获取 HTML
    html_content = get_html_content(url, headers)

    # 提取第一个通知的标题、时间和链接
    (title, time, link) = extract_first_notice(html_content)

    full_url = urljoin(url, link)

    return (title, time, full_url)

# print(SWJTU_scrape_notices())