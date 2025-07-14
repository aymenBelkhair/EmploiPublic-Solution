from requests_html import HTMLSession
from dataclasses import dataclass

@dataclass
class Info:
        notification_type:str
        job_title:str
        job_gov:str
        job_link:str
        nbr_place:str
        last_chance:str
        day_of_exam:str

class Sub_info:
        date_ofShare:str
        dowanload_avis:str
        domain_ofStudy:str
        profil_position:str
        recruitment_type:str

def get_elements(s:HTMLSession,url:str,headers:dict) -> list|None:
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
        nbr_place=ele.find("div.card-footer",first=True).find('div')[1].text.strip()
        last_date_ofcandidature=ele.find("div.card-footer",first=True).find('div')[2].text.strip().split(": ")[1].strip()
        exam_day=ele.find("div.card-footer",first=True).find('div')[3].text.strip().split(":")[1].strip()
        items.append({
                    "notification_type":notification_type,
                    "job_title":job_title,
                    "job_gov":job_gov,
                    "job_link":job_link,
                    "nbr_place":nbr_place,
                    "last_chance":last_date_ofcandidature,
                    "day_of_exam":exam_day
                      })
        #check if the list isn't empty
    if len(items)!=0:
        return items
    else :
        return None
    

def get_sub_element(s:HTMLSession,url:str,headers:dict) -> list|None:
    job_card = s.get(url=url,headers=headers,verify=False)
    left_requiremnts=job_card.html.find("div.col-md-4",first=True)
    right_requiremnts=job_card.html.find("div.col-md-8",first=True)
    job_details=[]
    date_ofShare=list(left_requiremnts.find("h3"))[-1].text.split("Date de publication")[1].strip()
    dowanload_avis=list(left_requiremnts.absolute_links)[0]
    domain_ofStudy=right_requiremnts.find('li')[0].text.strip().split(" :")[1]
    profil_position=right_requiremnts.find('li')[1].text.strip().split(" :")[1]
    recruitment_type=right_requiremnts.find('li')[3].text.strip().split(" :")[1]
    job_details.append(
        {
            "date_of_share":date_ofShare,
            "download_avis":dowanload_avis,
            "domain":domain_ofStudy,
            "profil_position":profil_position,
            "recruitment_type":recruitment_type
        }
    )

    if len(job_details)!=0:
        return job_details
    else :
        return None



