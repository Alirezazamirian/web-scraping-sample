import requests

url = "https://mobile-phones2.p.rapidapi.com/brands"
headers = {
    'x-rapidapi-host': "mobile-phones2.p.rapidapi.com",
    'x-rapidapi-key': "e8a82b41c2msh324eb4c4a1cabe3p185edajsn2973e4abbf34"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    brands = response.json()

    with open('all_brands.txt', 'w') as file:
        for brand in brands:
            file.write(brand['name'] + '\n')

    print("Brand names have been written successfully.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
