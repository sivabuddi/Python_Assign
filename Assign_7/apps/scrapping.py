from bs4 import BeautifulSoup
import requests


def scrap_web_page(url, output_file):
    source_code = requests.get(url)
    plain_text = source_code.text
    parse = BeautifulSoup(plain_text, "html.parser")
    p = parse.findAll('p')
    f = open(output_file, "w")
    for item in p:
        f.write(str(item.text))
