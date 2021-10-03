import requests
from bs4 import BeautifulSoup as bs
from functions import *
import re
import sys

def main():
    if sys.argv[1].lower() == "movie":
        search = input(">>")
        linksDict = f2m_search(search)
        
        n = 0
        for link in linksDict:
            print(f"[{n+1}] {link}")
            n += 1
        
        # links = movie_search(search = search)
        # number = int(input(">"))
        # res = movie_links(url = links[number-1])
        # dl_links = []
        # for sth in res:
        #     dl_links.append(sth.attrs["href"])

        # print("-------------------------------------------")
        # for dl_link in dl_links:
        #     print("\n")
        #     print(dl_link)
        # print("\n-------------------------------------------")
        print("---------------------- subtitle ----------------------")
        subtitle_links = subtitle_search(search = search)
        # subtitle_links = find_subtitle_links(text = raw_text)
        n = 0
        for link in subtitle_links:
            print(f"[{n+1}] {link}")
            n += 1

        sub_number = input(">")
        
        subtitle_page_link = list(subtitle_links.values())[int(sub_number) - 1]
        
        print("-------------------------------------------")
        for link in get_subtitle_dl_links(url = subtitle_page_link):
            print(link)

        print("-------------------------------------------")


if __name__ == "__main__":
    main()
