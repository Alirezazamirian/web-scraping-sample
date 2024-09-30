import requests
from bs4 import BeautifulSoup
import openpyxl

base_url = 'https://www.safiir.com'


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com/',
        'Connection': 'keep-alive',
        'DNT': '1',  # Do Not Track
        'Cache-Control': 'no-cache',  # Prevent caching
        'Upgrade-Insecure-Requests': '1',  # Prefer secure versions
    }
    r = requests.get(base_url + '/sitemap_index.xml', headers=headers)
    r.encoding = 'utf-8'
    titles = []
    models = []

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
            product_req = requests.get(url, headers=headers)
            product_soup = BeautifulSoup(product_req.text, 'xml')
            product_urls = product_soup.find_all('loc')
            for new_loc in [loc.text for loc in product_urls]:
                new_loc_url = requests.get(new_loc,  headers=headers)
                if '.jpg' in new_loc or '.png' in new_loc:
                    continue
                soup = BeautifulSoup(new_loc_url.text, 'html.parser')

                title = soup.select_one('h1.product_title.entry-title').get_text(strip=True) if soup.select_one(
                    'h1.product_title.entry-title') else None

                category = None
                category_span = soup.select_one('span.posted_in')
                if category_span:
                    category_link = category_span.find('a')
                    if category_link:
                        category = category_link.get_text(strip=True)

                print(url)
                print(new_loc)
                print(title)
                print(category)

                titles.append(title)
                models.append(category)
    else:
        print(f"Failed to retrieve the sitemap. Status code: {r.status_code}")

    with open('./product_data5.txt', 'w', encoding='utf-8') as f:
        for i in range(len(titles)):
            f.write(titles[i] + '\n')
            f.write(models[i] + '\n')

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'Data'
    sheet.append(['title', 'model'])

    num_rows = min(len(titles), len(models))
    for i in range(num_rows):
        row_data = [titles[i], models[i]]
        sheet.append(row_data)

    file_path = 'created_data5.xlsx'
    wb.save(file_path)


if __name__ == '__main__':
    main()