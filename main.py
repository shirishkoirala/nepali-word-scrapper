import requests
import re
from bs4 import BeautifulSoup

seed = "http://kantipur.ekantipur.com/"
stack = [seed]
stack_clone = stack
words = []
fout = open('dict.txt', 'w', encoding='utf8')


def main_spider():
    source_code = ''
    for url in stack:
        print('Pop Stack: ' + url)
        stack.pop()
        try:
            print('Requesting: ' + url)
            source_code = requests.get(url)
        except requests.exceptions.RequestException as e:
            pass

        plain_text = source_code.text

        soup = BeautifulSoup(plain_text, "html.parser")

        if '.html' in url:
            for p in soup.find_all('p'):
                for word in p.get_text().split():
                    pattern = re.compile("[$&+,:;=?@#|'<>.-^*()%!–।‘१२३४५६७८९०�?/\{\}()]")
                    if not re.search(pattern, word):
                        if word not in words:
                            words.append(word)
                            print('Word:' + word)
                            print(word, file=fout)

        for link in soup.find_all('a'):
            url = link.get('href')
            if url is not None:
                if 'http://' not in url:
                    url = seed[:-1] + url
                    if url not in stack_clone:
                        stack.append(url)
                        stack_clone.append(url)


main_spider()
