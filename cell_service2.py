import requests
from bs4 import BeautifulSoup
import openpyxl

base_url = 'https://gpgsm.ir'


def main():
    r = requests.get(base_url + '/sitemap_index.xml')
    r.encoding = 'utf-8'
    titles = []
    brands = []
    models = []
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'xml')
        urls = soup.find_all('loc')
        product_url = []

        i = ''
        for url in [loc.text for loc in urls]:
            if url == base_url + f'/product-sitemap{i}.xml':
                product_url.append(url)
                if i == '':
                    i = 1
                i += 1
        for url in product_url:
            product_req = requests.get(url)
            product_soup = BeautifulSoup(product_req.text, 'xml')
            product_urls = product_soup.find_all('loc')
            for new_loc in [loc.text for loc in product_urls]:
                try:
                    new_loc_url = requests.get(new_loc)
                    if '.jpg' in new_loc or '.png' in new_loc:
                        continue
                    soup = BeautifulSoup(new_loc_url.text, 'xml')
                    print(url)
                    print(new_loc)
                    title = soup.select_one('h1.product_title').get_text(strip=True) if soup.select_one(
                        'h1.product_title') else None
                    brand = None
                    model = None
                    for li in soup.find_all('li'):
                        title_span = li.find('span', class_='title')
                        if title_span and 'برند' in title_span.text:
                            brand = li.text.replace(title_span.text, "").strip()
                        if title_span and 'مدل' in title_span.text:
                            model = li.text.replace(title_span.text, "").strip()

                    print(title)
                    print(brand)
                    print(model)

                    titles.append(title)
                    brands.append(brand)
                    models.append(model)
                except:
                    pass
    else:
        print(f"Failed to retrieve the sitemap. Status code: {r.status_code}")

    with open('./product_data2.txt', 'w', encoding='utf-8') as f:
        for i in range(len(titles)):
            if titles[i] == None:
                titles[i] = 'None'
            if brands[i] == None:
                brands[i] = 'None'
            if models[i] == None:
                models[i] = 'None'
            f.write(titles[i] + '\n')
            f.write(brands[i] + '\n')
            f.write(models[i] + '\n')

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'Data'
    sheet.append(['title', 'brand', 'model'])

    num_rows = min(len(titles), len(brands), len(models))
    for i in range(num_rows):
        row_data = [titles[i], brands[i], models[i]]
        sheet.append(row_data)

    file_path = 'created_data2.xlsx'
    wb.save(file_path)


if __name__ == '__main__':
    main()
