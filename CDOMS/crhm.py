import requests
from requests_ntlm2 import HttpNtlmAuth
import json


url = 'http://hrm.bmst-kz.borusan.com/'

doc_id_url = 'http://crcms.bmst-kz.borusan.com/CRHNew/GetCRHVMDocumentIds'

s = requests.Session()

s.auth = HttpNtlmAuth('dnurgozhin', '1997Ndg1997')

headers1 = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Host": "hrm.bmst-kz.borusan.com",
"Referer": "http://hrm.bmst-kz.borusan.com/Birthday",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

r = s.get(url=doc_id_url)
print(r.status_code)

ids = r.json()
print('id count:', len(ids))

i = 0
data = []
while ids[i:i+1000]:
    print('requesting 1000 from', i)
    r = s.post(
        'http://crcms.bmst-kz.borusan.com/CRHNew/GetCRHVM',
        json={'documentId': ids[i:i+1000]}
    )
    print(r.status_code)
    data.extend(r.json())
    i += 1000


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)
