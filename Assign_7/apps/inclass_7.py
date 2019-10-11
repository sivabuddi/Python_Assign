from apps.scrapping import scrap_web_page
from apps.tokenizer import tokenize

scrap_web_page("https://en.wikipedia.org/wiki/Google", "input.txt")
tokenize("input.txt", "tokens.txt")
