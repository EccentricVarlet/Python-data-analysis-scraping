from django.shortcuts import render
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.

bd_url = "https://corona.gov.bd/lang/en"
page = requests.get(bd_url)
soup = BeautifulSoup(page.content, "html.parser")
counts = soup.select(".live-update-box-wrap-h1>b")
for i in range(len(counts)):
    counts[i] = int(counts[i].text)


# data_dict = {
#     "positive_24": counts[0],
#     "positive_total": counts[1],
#     "death_24": counts[2],
#     "total_death": counts[3],
#     "recovered_24": counts[4],
#     "total_recover": counts[5],
#     "test_24": counts[6],
#     "test_total": counts[7],
# }

def index(req):
    return render(req, 'covid/index.html', {'data':counts})