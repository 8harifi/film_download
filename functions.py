import requests
from bs4 import BeautifulSoup as bs
import re

def movie_search (search):
    url = f"https://my-film.pw/?s={'+'.join(search.split())}"
    print("url:", url)
    print("\n\n\n")
    r = requests.get(url)

    soup = bs(r.text, "html.parser")
    items = soup.find_all("a", attrs = {"rel": "bookmark"})

    links = []
    n = 0
    for item in items:
        n += 1
        link = item.attrs['href']
        title = item.attrs['title']
        links.append(str(link))
        print(f"[{n}]> title: {title}\nlink: {link}\n-----------------------------\n")
    
    return links


def movie_links (url):
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    res = soup.find_all("a", attrs = {
        "class": "dl_file"
    })
    return res

def subtitle_search (search):
    data = {
        "action": "ajaxsearchlite_search",
        "aslp": f"{'+'.join(search.split())}",
        "options": "qtranslate_lang=0&asl_gen[]=title&asl_gen[]=content&customset[]=post"
    }
    r = requests.post(url = "https://subkade.ir/wp-admin/admin-ajax.php", data = data)
    return r.text

def find_subtitle_links (text):
    soup = bs(text, "html.parser")
    tags = soup.find_all('a', attrs = {
        "class": "asl_res_url"
    })
    links = []
    for tag in tags:
        links.append(tag.attrs['href'])
    return links

def get_subtitle_dl (url):
    r = requests.get(url = url)
    soup = bs(r.text, "html.parser")
    res = soup.find_all("a", attrs = {
        "class": "rounded-lg d-inline-block font-weight-bold sub_sgl_dl_btn"
    })
    dl_link = res[1]
    return dl_link.attrs['href']