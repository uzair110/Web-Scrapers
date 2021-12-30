import requests
import google
from requests import get
from bs4 import BeautifulSoup
import sys

results = []
mobile_model = ''

def get_mobile_data():
	try:
		base_url = results[0]

		response = get(base_url)
		# response2 = get(base_url2)
		soup = BeautifulSoup(response.text,features="html.parser")
		# soup2 = BeautifulSoup(response2.text, features="html.parser")
		# content_price = soup2.find_all('span', attrs={"class":"summary-price"})
		# content_release = soup2.find_all('table', attrs={'class': 'p-spec-table card'})
		# try:
		# 	info = content_release[0].find_all('td')
		# except IndexError:
		# 	pass

		content_list = soup.find_all('span', attrs={'class': 'hdng'})
		basic_info = []
		for item in content_list:
			basic_info.append(item.find_all('span', attrs={'class': 'hdng'}))
		print(content_list[1].text)
		print("\n")
		# f1.write(''.join('{} {} {} {} {}'.format(sys.argv[1] , ';', content_price[1].text,';',info[0].text)))
		# f1.write('\n')
	except IndexError:
		error = 'Mobile not found'
		print(error)
	# 	mylist = []
	# 	mylist.append(mobile_model)
	# 	mylist.append(error)
	# 	f1.write(''.join('{} {}'.format(sys.argv[1],error)))
	# 	f1.write('\n')
	# 	# print(error)
	# f1.close()

def get_google_searches(query):
	try: 
		from googlesearch import search 
		import re
	except ImportError:  
		print("No module named 'google' found") 
 
	substring1 = 'whatmobile'
	substring2 = 'priceoye'
	for j in search(query, tld="com", num=10, stop=15, pause=2): 

		if substring1 in j:
			results.append(j)
			break				# if len(results) > 0:
			# 	for item in results:
			# 		if substring2 in item or substring1 in item:
			# 			continue
			# 		results.append(j)



def main(inp):
	mobile_model = inp

	# inp = input('Type the phone model e.g Samsung A20 \n')
	inp = inp + ' price in Pakistan'

	# print(inp)
	get_google_searches(inp)
	get_mobile_data()

if __name__ == '__main__':
	main(sys.argv[1])