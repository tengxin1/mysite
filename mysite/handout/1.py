# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    response = request.urlopen("http://example.python-scraping.com/places/default/view/United-States-234")
    html = response.read()
    print(html)
