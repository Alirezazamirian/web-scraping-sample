import requests
from bs4 import BeautifulSoup

base_url = 'https://rmgsm.ir'


def main():
    r = requests.get(base_url + '/sitemap_index.xml')
    result = []
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'xml')
        urls = soup.find_all('loc')
        product_url = []

        i = 1
        for url in [loc.text for loc in urls]:
            if url == base_url + f'/product-sitemap{i}.xml':
                product_url.append(url)
                i += 1
        for url in product_url:
            product_req = requests.get(url)
            product_soup = BeautifulSoup(product_req.text, 'xml')
            product_urls = product_soup.find_all('loc')
            for new_loc in [loc.text for loc in product_urls]:
                new_loc_url = requests.get(new_loc)
                soup = BeautifulSoup(new_loc_url.text, 'html.parser')
                title = soup.select_one('h1.product_title').get_text(strip=True) if soup.select_one(
                    'h1.product_title') else None
                result.append(title)
                print(title)
    else:
        print(f"Failed to retrieve the sitemap. Status code: {r.status_code}")

    with open('./product_data.txt', 'w', encoding='utf-8') as f:
        for data in result:
            f.write(data)


if __name__ == '__main__':
    main()
