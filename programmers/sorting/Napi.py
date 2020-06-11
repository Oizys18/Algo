import requests
from decouple import config
from pprint import pprint
import os
import sys
url = "https://openapi.naver.com/v1/search/shop.json?query=protein"
headers = {
   #Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
   'X-Naver-Client-Id': "uELO_9dcM3xKLLkQCF2O",
   'X-Naver-Client-Secret': "Abo9yb6amT",
}
# data = {
#    'query':'protein',
# }
res = requests.get(url, headers=headers)
pprint(res.text)
# pprint(res.json())