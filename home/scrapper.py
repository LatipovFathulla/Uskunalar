import requests
from bs4 import BeautifulSoup


def request_github_trending(url):
    return requests.get(url)


def extract(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup.find_all("td")[2].text


def _main():
    url = 'https://nbu.uz/uz/exchange-rates/'
    page = request_github_trending(url)
    html_repos = extract(page)
    return format(html_repos)


_main()
