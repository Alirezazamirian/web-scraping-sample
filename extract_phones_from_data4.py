import re
from openpyxl import Workbook

def brand_list_func():
    return []



print('started ......')

farsi_pattern = r'[\u0600-\u06FF\s]+'
english_pattern = r'[A-Za-z0-9\s]+'
i = 0
j = 0
x = 0
n = 0
l = 0
b = 0
h = 0
a = 0
ia = 0
m = 0
leno = 0
sonyx = 0
sonye = 0

samsung = 'سامسونگ'
galaxy = 'گلکسی'
samsung_galaxy = 'سامسونگ گلکسی'
xiaomi = 'شیائومی'
huawei = 'هواوی'
huawei2 = 'هوآوی'
nokia = 'نوکیا'
LG = 'ال جی'
blackberry = 'بلک بری'
HTC = 'اچ تی سی'
asus = 'ایسوس'
iphone = 'آیفون'
microsoft = 'مایکروسافت'
lenovo = 'لنوو'
sony_ericson = 'سونی اریکسون'
sony_xperia = 'سونی اکسپریا'

brand_list = []
model_list = []
part_list = []
sony_xperia_part_list = []
sony_xperia_model_list = []
sony_ericson_part_list = []
sony_ericson_model_list = []
samsung_part_list = []
samsung_model_list = []
xiaomi_part_list = []
xiaomi_model_list = []
huawei_part_list = []
huawei_model_list = []
nokia_part_list = []
nokia_model_list = []
LG_part_list = []
LG_model_list = []
blackberry_part_list = []
blackberry_model_list = []
HTC_part_list = []
HTC_model_list = []
asus_part_list = []
asus_model_list = []
iphone_part_list = []
iphone_model_list = []
microsoft_part_list = []
microsoft_model_list = []
lenovo_part_list = []
lenovo_model_list = []
process_list = []
all_brands = []

wb = Workbook()
ws = wb.active
ws.title = "Phone Data"
ws.append(["Part Title", "Model", "Brand"])

with open('data/product_data4.txt', 'r') as brands:
    for brand in brands:
        all_brands.append(brand)
        if samsung in brand or galaxy in brand or samsung_galaxy in brand:
            if samsung_galaxy in brand:
                samsung_part = brand.split(samsung_galaxy, 1)[0].strip()
                samsung_model = brand.split(samsung_galaxy, 1)[1].strip()
            elif samsung in brand:
                samsung_part = brand.split(samsung, 1)[0].strip()
                samsung_model = brand.split(samsung, 1)[1].strip()
            elif galaxy in brand:
                samsung_part = brand.split(galaxy, 1)[0].strip()
                samsung_model = brand.split(galaxy, 1)[1].strip()
            samsung_part_list.append(samsung_part)
            samsung_model_list.append(samsung_model)
            ws.append([samsung_part, samsung_model, samsung_galaxy])
            process_list.append(brand)
            i += 1

        if xiaomi in brand:
            xiaomi_part = brand.split(xiaomi, 1)[0].strip()
            xiaomi_model = brand.split(xiaomi, 1)[1].strip()
            xiaomi_part_list.append(xiaomi_part)
            xiaomi_model_list.append(xiaomi_model)
            ws.append([xiaomi_part, xiaomi_model, xiaomi])
            process_list.append(brand)
            j += 1

        if huawei in brand or huawei2 in brand:
            if huawei in brand:
                huawei_part = brand.split(huawei, 1)[0].strip()
                huawei_model = brand.split(huawei, 1)[1].strip()
            if huawei2 in brand:
                huawei_part = brand.split(huawei2, 1)[0].strip()
                huawei_model = brand.split(huawei2, 1)[1].strip()
            huawei_part_list.append(huawei_part)
            huawei_model_list.append(huawei_model)
            ws.append([huawei_part, huawei_model, huawei])
            process_list.append(brand)
            x += 1

        if nokia in brand:
            nokia_part = brand.split(nokia, 1)[0].strip()
            nokia_model = brand.split(nokia, 1)[1].strip()
            nokia_part_list.append(nokia_part)
            nokia_model_list.append(nokia_model)
            ws.append([nokia_part, nokia_model, nokia])
            process_list.append(brand)
            n += 1

        if LG in brand:
            LG_part = brand.split(LG, 1)[0].strip()
            LG_model = brand.split(LG, 1)[1].strip()
            LG_part_list.append(LG_part)
            LG_model_list.append(LG_model)
            ws.append([LG_part, LG_model, LG])
            process_list.append(brand)
            l += 1

        if blackberry in brand:
            blackberry_part = brand.split(blackberry, 1)[0].strip()
            blackberry_model = brand.split(blackberry, 1)[1].strip()
            blackberry_part_list.append(blackberry_part)
            blackberry_model_list.append(blackberry_model)
            ws.append([blackberry_part, blackberry_model, blackberry])
            process_list.append(brand)
            b += 1

        if HTC in brand:
            HTC_part = brand.split(HTC, 1)[0].strip()
            HTC_model = brand.split(HTC, 1)[1].strip()
            HTC_part_list.append(HTC_part)
            HTC_model_list.append(HTC_model)
            ws.append([HTC_part, HTC_model, HTC])
            process_list.append(brand)
            h += 1

        if asus in brand:
            asus_part = brand.split(asus, 1)[0].strip()
            asus_model = brand.split(asus, 1)[1].strip()
            asus_part_list.append(asus_part)
            asus_model_list.append(asus_model)
            ws.append([asus_part, asus_model, asus])
            process_list.append(brand)
            a += 1

        if iphone in brand:
            iphone_part = brand.split(iphone, 1)[0].strip()
            iphone_model = brand.split(iphone, 1)[1].strip()
            iphone_part_list.append(iphone_part)
            iphone_model_list.append(iphone_model)
            ws.append([iphone_part, iphone_model, iphone])
            process_list.append(brand)
            ia += 1

        if microsoft in brand:
            microsoft_part = brand.split(microsoft, 1)[0].strip()
            microsoft_model = brand.split(microsoft, 1)[1].strip()
            microsoft_part_list.append(microsoft_part)
            microsoft_model_list.append(microsoft_model)
            ws.append([microsoft_part, microsoft_model, microsoft])
            process_list.append(brand)
            m += 1

        if lenovo in brand:
            lenovo_part = brand.split(lenovo, 1)[0].strip()
            lenovo_model = brand.split(lenovo, 1)[1].strip()
            lenovo_part_list.append(lenovo_part)
            lenovo_model_list.append(lenovo_model)
            ws.append([lenovo_part, lenovo_model, lenovo])
            process_list.append(brand)
            leno += 1

        if sony_ericson in brand:
            sony_ericson_part = brand.split(sony_ericson, 1)[0].strip()
            sony_ericson_model = brand.split(sony_ericson, 1)[1].strip()
            sony_ericson_part_list.append(sony_ericson_part)
            sony_ericson_model_list.append(sony_ericson_model)
            ws.append([sony_ericson_part, sony_ericson_model, sony_ericson])
            process_list.append(brand)
            sonye += 1

        if sony_xperia in brand:
            sony_xperia_part = brand.split(sony_xperia, 1)[0].strip()
            sony_xperia_model = brand.split(sony_xperia, 1)[1].strip()
            sony_xperia_part_list.append(sony_xperia_part)
            sony_xperia_model_list.append(sony_xperia_model)
            ws.append([sony_xperia_part, sony_xperia_model, sony_xperia])
            process_list.append(brand)
            sonyx += 1

        # farsi_text = re.findall(farsi_pattern, brand)
        # english_text = re.findall(english_pattern, brand)
        #
        # farsi_result = ''.join(farsi_text).strip()
        # english_result = ''.join(english_text).strip()

part_list = (samsung_part_list + xiaomi_part_list + LG_part_list + microsoft_part_list + lenovo_part_list +
             iphone_part_list + blackberry_part_list + asus_part_list + HTC_part_list + huawei_part_list +
             nokia_part_list + sony_ericson_part_list + sony_xperia_part_list)

model_list = (samsung_model_list + xiaomi_model_list + LG_model_list + HTC_model_list + iphone_model_list +
              lenovo_model_list + nokia_model_list + microsoft_model_list + asus_model_list +
              blackberry_model_list + huawei_model_list + sony_xperia_model_list + sony_ericson_model_list)

total_count = i + j + x + n + l + b + h + a + ia + m + leno

result = list(set(all_brands) - set(process_list))
with open('features_of_product_data4.txt', 'w', encoding='utf-8') as file:
    file.writelines(result)

excel_file_name = "phones_data.xlsx"
wb.save(excel_file_name)

# print(f'samsung relatives : {i}')
# print(f'xiaomi relatives : {j}')
# print(f'Huawei relatives : {x}')
# print(f'nokia relatives : {n}')
# print(f'LG relatives : {l}')
# print(f'BlackBerry relatives : {b}')
# print(f'HTC relatives : {h}')
# print(f'Asus relatives : {a}')
# print(f'Iphone relatives : {ia}')
# print(f'Microsoft relatives : {m}')
# print(f'Lenovo relatives : {leno}')
# print(f'total is : {i + j + x + n + l + b + h + a + ia + m + leno}')

print('finished ......')

