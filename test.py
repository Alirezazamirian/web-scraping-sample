import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://rmgsm.ir/product/%d8%b4%db%8c%d8%b4%d9%87-%d8%af%d9%88%d8%b1%d8%a8%db%8c%d9%86-%d8%a2%db%8c%d9%81%d9%88%d9%86-12-pro-max/'
    url2 = 'https://rmgsm.ir/product/%da%af%d9%84%d8%b3-%d8%aa%d8%b9%d9%85%db%8c%d8%b1%d8%a7%d8%aa%db%8c-%d8%a8%d8%a7-oca-%d8%aa%d8%a8%d9%84%d8%aa-%d9%84%d9%86%d9%88%d9%88-m8-8505/'
    new_loc_url = requests.get(url2)
    soup = BeautifulSoup(new_loc_url.text, 'lxml')
    title = soup.select_one('h1.product_title').get_text(strip=True) if soup.select_one(
        'h1.product_title') else None
    print(url)
    print(title)

if __name__ == '__main__':
    main()
