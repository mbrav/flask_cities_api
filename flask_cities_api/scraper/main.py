import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_data_file(path: str):
    file=open(BASE_DIR + '/' + path, 'r')
    data=json.load(file)
    file.close()
    return data


if __name__ == '__main__':
    import requests
    from bs4 import BeautifulSoup

    url='https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'
    r=requests.get(url)

    soup=BeautifulSoup(r.text, 'html.parser')
    table=soup.find('table', attrs={'class': 'standard'})

    obj=[]
    num_reg=r'[0-9]+'
    for col in table.find_all('tr')[2:]:

        row=col.find_all('td')

        print(row[2].get_text())

        data={
            'city': row[2].get_text(),
            'state': row[3].get_text(),
            'region': row[4].get_text(),
            'population': re.findall(num_reg, row[5].get_text())[0],
            'year-founded': re.findall(num_reg, row[6].get_text())[0],
            # 'year-city': re.findall(num_reg, row[7].get_text())[0],
        }
        obj.append(data)

    print(obj[314])

    out_file=open('data/cities-rus.json', 'w')
    json.dump(obj, out_file, ensure_ascii=False)
    out_file.close()
