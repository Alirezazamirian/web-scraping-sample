import requests
from bs4 import BeautifulSoup
import openpyxl

base_url = 'https://parstellshop.com/fa/sitemap/product/1.xml'


def main():
    r = requests.get(base_url)
    r.encoding = 'utf-8'
    titles_list = []

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'xml')
        titles = soup.find_all('image:title')
        for title in titles:
            titles_list.append(title.get_text(strip=True))
            print(title)
    else:
        print(f"Failed to retrieve the sitemap. Status code: {r.status_code}")

    with open('./product_data4.txt', 'w', encoding='utf-8') as f:
        for i in range(len(titles_list)):
            f.write(titles_list[i] + '\n')

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'Data'
    sheet.append(['title'])

    num_rows = len(titles_list)
    for i in range(num_rows):
        row_data = [titles_list[i]]
        sheet.append(row_data)

    file_path = 'created_data4.xlsx'
    wb.save(file_path)


if __name__ == '__main__':
    main()
