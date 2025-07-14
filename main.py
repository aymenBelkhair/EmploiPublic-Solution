from app.config import headers
from requests_html import HTMLSession
from app.helper import get_elements,get_sub_element,Info
from dataclasses import dataclass
from typing import List




s= HTMLSession()

url = "https://www.emploi-public.ma/fr/concours-liste?page=2"
items = get_elements(s=s,url=url,headers=headers)
info:List[Info] = [Info(**item) for item in items]

for inf in info:
    sub_items=get_sub_element(s=s,url=info.job_link,headers=headers)
    print()
    print(sub_items)
    print()
    

    