import requests
from bs4 import BeautifulSoup as bs
from functions import *
import re

def main():
    search = input(">>")
    links = movie_search(search = search)
    number = int(input(">"))
    res = movie_links(url = links[number-1])
    dl_links = []
    for sth in res:
        dl_links.append(sth.attrs["href"])

    print("-------------------------------------------")
    for dl_link in dl_links:
        print("\n")
        print(dl_link)
    print("\n-------------------------------------------")
    raw_text = subtitle_search(search = search)
    subtitle_links = find_subtitle_links(text = raw_text)
    print("---------------------- subtitle ----------------------")
    n = 0
    for link in subtitle_links :
        n += 1
        print(f"[{n}]> {link}")
        print("------------------")
    sub_number = input(">")
    subtitle_dl_link = get_subtitle_dl(subtitle_links[number-1])
    print("-------------------------------------------")
    print(subtitle_dl_link)
    print("-------------------------------------------")


if __name__ == "__main__":
    main()
