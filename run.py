from bs4 import BeautifulSoup
import re
import sys


def get_message_in_quote(html):
    soup = BeautifulSoup(html, 'lxml')
    message = re.sub(r'\s+', " ", soup.blockquote.text)
    return message


if __name__ == "__main__":
    html = str(sys.argv[1])
    message = get_message_in_quote(html)
    print(f"\n{message}")
