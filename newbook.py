import requests

TTBKey = "ttbletyoursoulbefree1931001"
url = []
author = ['정연석', '강성민', '이정엽', '박도원']


for l in author:
    url.append("http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=" +
               TTBKey+"&Query="+l+"&RecentPublishFilter=1&MaxResults=1")

f = open('xml.xml', 'w')
f.write(requests.get(url[0]).text)
f.close()
