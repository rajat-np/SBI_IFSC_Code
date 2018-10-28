import requests
import bs4
import sys
from fuzzywuzzy import fuzz


class Ifsc():
	def __init__(self,query):
		self.query = query
		self.headers = {
			"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
		} 

	def get_code(self):
		query = self.query.split('+')
		STATE = query[0]
		DISTRICT = query[1]
		BRANCH = query[2]
		print("Original Query: ",STATE,DISTRICT, BRANCH)
		STATE, DISTRICT, BRANCH = self.normalize(STATE,DISTRICT,BRANCH)
		print("Normalized Query: ",STATE,DISTRICT, BRANCH)
		url = "https://bankifsccode.com/STATE_BANK_OF_INDIA/{}/{}/{}/".format(STATE.strip(),DISTRICT.strip(),BRANCH.strip())
		print("Full URL: " , url)
		r = requests.get(url, headers = self.headers)
		anchors = bs4.BeautifulSoup(r.content, 'lxml').find_all('a')
		for anchor in anchors:
			if "https://ifsc.bankifsccode.com/SBI" in anchor['href']:
				IFSC = anchor.text
				return IFSC


	def normalize(self,s,d,b):
		ls = []
		s = s.replace(' ','_').upper()
		d = d.replace(' ','_').upper()
		b = b.upper()
		u = "https://bankifsccode.com/STATE_BANK_OF_INDIA/{}/{}/".format(s.strip(),d.strip())
		req = requests.get(u,headers = self.headers)
		if req.status_code == 200:
			soup = bs4.BeautifulSoup(req.content,'lxml')
			links = soup.find_all('a')
			for link in links:
				if u in link['href']:
					ls.append(link.text)
		max = 0
		Nb = ''
		for l in ls:
			if fuzz.ratio(b,l) > max:
				max = fuzz.ratio(b,l)
				Nb = l
		if max<50:
			print('No Matching Found to query, Try again!')
			sys.exit()
		return  s,d,Nb.replace(' ', '_')

