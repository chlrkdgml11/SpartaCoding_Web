import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')

rjson = r.json()

rows = rjson['RealtimeCityAir']['row']

for rows in rows:
    gu_name = rows['MSRSTE_NM']
    gu_mise = rows['IDEX_MVL']
    
    if(gu_mise < 60):
        print(gu_name, gu_mise)

