from bs4 import BeautifulSoup
import re
from urllib import request
s=[]
href=[]
with open('output_sum.html','r',encoding='utf-8') as f:
    cont=f.read()
    soup1=BeautifulSoup(cont,'html.parser')
    links=soup1.find_all(text=re.compile('http'))
    count=0
    for link in links:
        try:
            count=count+1
            href.append(link)
            with request.urlopen(link)as o:
                res=o.read()
                soup2=BeautifulSoup(res,'html.parser')
                node=soup2.find('span',class_='rightSpan').find('b')
                print(count,link,node.get_text())
                s.append(node.get_text())
        except:
            print(count,link)
    with open('result.txt','w',encoding='utf-8') as g:
        g.write('\n'.join(s))


