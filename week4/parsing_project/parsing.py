import requests
from bs4 import BeautifulSoup
import ssl
print(ssl.get_default_verify_paths().openssl_cafile) 

def get_html(url):
    # headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, verify=False)
    print(response.status_code)



def main():
    notebooks_url = 'https://www.sulpak.kg/f/noutbuki'
    pages = '?page='
    get_html(notebooks_url)

main()