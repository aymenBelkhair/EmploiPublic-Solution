from app.config import headers
from requests_html import HTMLSession

s= HTMLSession()

url = "https://www.emploi-public.ma/fr/concours-liste"
resp = s.get(url=url,headers=headers,verify=False)

body = resp.html.find("div#listing-switcher",first=True)
elements = body.find("div.s-item")

items=[]
#Data

for ele in elements :
    job_link=list(ele.absolute_links)[0]
    job_title=ele.find("h2",first=True).text.strip()
    job_gov=ele.find("div.card-text",first=True).text.strip()
    notification_type=ele.find("div.card-type",first=True).text.strip()
    annonce_or_result=ele.find("div.bg-blue",first=True).text.strip()
    if ele.find("div.btn-sm",first=True):
        candidature_methode=ele.find("div.btn-sm",first=True).text.strip()
    nbr_place=ele.find("div.card-footer",first=True).find('div')[1].text.strip()
    last_date_ofcandidature=ele.find("div.card-footer",first=True).find('div')[2].text.strip()
    exam_day=ele.find("div.card-footer",first=True).find('div')[3].text.strip()
    items.append({"job_title":job_title,"job_gov":job_gov,"job_link":job_link,"candidature_methode":candidature_methode})
    print(candidature_methode)

#show result    
for it in items:
    print()
    print(it)
    print()
    