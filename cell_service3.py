import requests
from bs4 import BeautifulSoup
import openpyxl

base_url = 'https://myphone.ir'


def main():
    r = requests.get(base_url + '/sitemap_index.xml')
    r.encoding = 'utf-8'
    titles = []
    brands = []
    models = []
    if r.status_code == 200:
        product_url = []
        product_url.append('https://myphone.ir/product-sitemap.xml')
        for url in product_url:
            product_req = requests.get(url)
            product_soup = BeautifulSoup(product_req.text, 'xml')
            product_urls = product_soup.find_all('loc')
            for new_loc in [loc.text for loc in product_urls]:
                new_loc_url = requests.get(new_loc)
                if '.jpg' in new_loc or '.png' in new_loc:
                    continue
                if new_loc == 'https://myphone.ir/shop/':
                    continue
                soup = BeautifulSoup(new_loc_url.text, 'xml')
                print(url)
                print(new_loc)
                title = soup.select_one('h1.product_title').get_text(strip=True) if soup.select_one(
                    'h1.product_title') else None

                brand = soup.select_one('span.brands')
                if brand:
                    brand = brand.find('a').get_text(strip=True)
                model = soup.select_one('span.posted_in')
                if model:
                    model = model.get_text(strip=True).replace('دسته: ', '', 1).strip()
                print(title)
                print(brand)
                print(model)
                titles.append(title)
                brands.append(brand)
                models.append(model)
    else:
        print(f"Failed to retrieve the sitemap. Status code: {r.status_code}")

    with open('./product_data3.txt', 'w', encoding='utf-8') as f:
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

    file_path = 'created_data3.xlsx'
    wb.save(file_path)


if __name__ == '__main__':
    main()
