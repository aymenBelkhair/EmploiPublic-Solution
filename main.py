from app.config import headers
from requests_html import HTMLSession

s= HTMLSession()

url = "https://www.emploi-public.ma/fr/concours-liste"
resp = s.get(url=url,headers=headers,cert=False)

body = resp.html.find("div.s-item",first=True)

print(body)