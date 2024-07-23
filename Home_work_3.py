import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.divan.ru/vladivostok/category/divany-i-kresla'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

divans = soup.find_all('div', class_='lsooF')  # Уточните класс, если он другой
data = []
for divan in divans:
    try:
        price = divan.find('span', class_='ui-LD-ZU').text.strip().replace('руб', '').replace(' ', '')
        data.append([float(price)])
    except AttributeError:

        continue


df = pd.DataFrame(data, columns=['Price'])

df.to_csv('divan_prices.csv', index=False)


average_price = df['Price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} ₽')


plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=20, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
