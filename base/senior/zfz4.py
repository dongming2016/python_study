#coding:utf-8
import json
import pandas as pd
import csv
import requests
from pyquery import PyQuery as pq
a=0
b=1
c=2014
d=2014
while a<=11 and b<=11:
	a=a+1
	b=b+1
	m=str(c)+"-"+str(a)+"-1"
	n=str(d)+"-"+str(b)+"-1"
	w="http://vip.stock.finance.sina.com.cn/q/view/vFutures_History.php?page=33&breed=NG&start="+m+"&end="+n+"&jys=NYME&pz=NG&hy=&type=global&name=%B4%F3%B6%B91109"
	abc=w
	print(w)
	def get_one_page_one(abc):
		headers={
		'Usre-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360EE'}
		story=requests.get(abc)
		story.encoding='utf-8'
		html=pq(story.content)
		htmm=html('.historyList')
		trs=htmm('tr').items()
		# num=0
		data = {'time': [], 'spj': [], 'kpj': [], 'zgj': [], 'zdj': [], 'cjl': []}
		for tr in trs:
			# za=[]
			data.get('time').append(tr('td:nth-child(0)').text())
			data.get('spj').append(tr('td:nth-child(1)').text())
			data.get('kpj').append(tr('td:nth-child(2)').text())
			data.get('zgj').append(tr('td:nth-child(3)').text())
			data.get('zdj').append(tr('td:nth-child(4)').text())
			data.get('cjl').append(tr('td:nth-child(5)').text())
			# zb=[]
			# zb=tr('td:nth-child(2)').text()
			# zc=[]
			# zc=tr('td:nth-child(3)').text()
			# zd=[]
			# zd=tr('td:nth-child(4)').text()
			# ze=[]
			# ze=tr('td:nth-child(5)').text()
			# zf=[]
			# zf=tr('td:nth-child(6)').text()

			# zz=str(za)+','+str(zb)+','+str(zc)+','+str(zd)+','+str(ze)+','+str(zf)
			# zzz=type(zz)
		print(data)
		DataFrame = pd.DataFrame(data)
		DataFrame.to_csv('data3.csv',encoding='gbk')
			# num+=1
			

	zfz=get_one_page_one(w)
	print(zfz)
	#abc=w

