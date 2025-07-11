from app.config import headers
from requests_html import HTMLSession

s= HTMLSession()

url = "https://www.emploi-public.ma/fr/concours-liste"
resp = s.get(url=url,headers=headers,verify=False)

body = resp.html.find("div#listing-switcher",first=True)
elements = body.find("div.s-item")

#Data
job_link=list(elements[0].absolute_links)[0]
job_title=elements[0].find("h2",first=True).text.strip()
job_gov=elements[0].find("div.card-text",first=True).text.strip()
notification_type=elements[0].find("div.card-type",first=True).text.strip()
candidature_type=elements[0].find("div.btn-sm",first=True).text.strip()
nbr_place=elements[0].find("div.card-footer",first=True).find('div')[1].text.strip()
last_date_ofcandidature=elements[0].find("div.card-footer",first=True).find('div')[2].text.strip()
exam_day=elements[0].find("div.card-footer",first=True).find('div')[3].text.strip()



print(elements[0].find("div.card-footer",first=True).find('div')[3].text.strip())