#Methode 1
# headers ={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
# }

#Methode 2
from fake_useragent import UserAgent
ua = UserAgent()
headers ={
    "User-Agent": f"{ua.random}"
}
