# -*- coding: utf-8 -*-

import requests
import re
import json
from bs4 import BeautifulSoup
from App.models import LinkSaver


linkToSite = "https://pythondigest.ru/"

class Parser:    
    r = requests.get(linkToSite)
    text = r.text    
    soup = BeautifulSoup(text, "html.parser")
    soup = soup.select('.items-group-container')
    linkList = []
    for i in soup:
        for j in i.select('a[href^="http"]'):
            a = j.text
            b = j.get('href')
            linkList.append([a,b])    
    stroka = ''
    for i in linkList:
        stroka += i[0]
        stroka += i[1]
        stroka += "<br>"

    def ReturnText(self):
        return self.stroka

    def ReturnList(self):
        return self.linkList

    def SaveToDb(self):
        #customList = []
        for link in self.linkList:
            entity = LinkSaver(title = link[0], href = link[1])
            entity.save()

    def RetrieveFromDb(self):
        a = LinkSaver.objects.all()
        stroka = 'Something'
        for i in a:
            stroka += i.title
            stroka += i.href
            stroka += '<br><br>'
        return stroka

    def ExtractDbToFile(self):
        a = LinkSaver.objects.all()
        comb = []
        for i in a:            
            comb.append({i.title: i.href})

        f = open('Test.json', 'w')
        js = json.dumps(comb,ensure_ascii=False)
        f.write(js.encode('utf-8'))
        f.close
        