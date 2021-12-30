import requests
import google
from requests import get
from bs4 import BeautifulSoup
import sys
import tqdm
import time


mobile_model = ''
# f1 = open("details.txt", "a")


def get_mobile_data_whatmobile(results):
	try:
		response = get(results)
		soup = BeautifulSoup(response.text,features="html.parser")
		content_list = soup.find_all('span', attrs={'class': 'hdng'})
		basic_info = []
		mobile_price = 0
		for item in content_list:
			basic_info.append(item.find_all('span', attrs={'class': 'hdng'}))
		for br in content_list[1].find_all('br'):
			mobile_price = br.previousSibling
			mobile_price = mobile_price.replace('Rs. ', '')
			mobile_price = mobile_price.replace(',','')
			break
		# print(content_list)
		if mobile_price == 0:
			return 'Search manually'
		else:
			return (mobile_price)
	except IndexError:
		error = 'Search manually'
		return error 

def get_mobile_data_priceoye(results):
	try:
		base_url2 = results
		# date = "No date found"
		response2 = get(base_url2)
		soup2 = BeautifulSoup(response2.text, features="html.parser")
		content_price = soup2.find_all('span', attrs={"class":"summary-price"})
		content_release = soup2.find_all('table', attrs={'class': 'p-spec-table card'})
		info = content_release[0].find_all('td')
		

		stripped = content_price[1].text
		return stripped
	except IndexError:
		error = 'Search manually'
		error_date = "No date found"
		return error

	# try:
	# 	info = content_release[0].find_all('td')
	# 	if "January" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "1/"+year
	# 	elif "Febuary" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "2/"+year
	# 	elif "March" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "3/"+year
	# 	elif "April" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "4/"+year
	# 	elif "May" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "5/"+year
	# 	elif "June" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "6/"+year
	# 	elif "July" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "7/"+year
	# 	elif "August" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "8/"+year
	# 	elif "September" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "9/"+year
	# 	elif "November" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "10/"+year
	# 	elif "October" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "11/"+year
	# 	elif "December" in rel_date:
	# 		year = rel_date[:4]
	# 		date = "12/"+year
	# 	else:
	# 		date = "No date found"
	# 	return stripped, date
	# except ValueError:
	# 	return stripped




def propakistani(query):
	try:
		response = get(query)
		soup = BeautifulSoup(response.text, features="html.parser")
		content = soup.find_all('div', attrs={"class":"price"})
		launch_date = soup.find_all('table', attrs={"class":"table mb-1"})
		try:
			i=0
			for row in launch_date[1].findAll("tr"):
				if i == 1:
					rel_date = row.findPrevious('td').text
					if "January" in rel_date:
						year = rel_date[:4]
						date = "1/"+year
					elif "Febuary" in rel_date:
						year = rel_date[:4]
						date = "2/"+year
					elif "March" in rel_date:
						year = rel_date[:4]
						date = "3/"+year
					elif "April" in rel_date:
						year = rel_date[:4]
						date = "4/"+year
					elif "May" in rel_date:
						year = rel_date[:4]
						date = "5/"+year
					elif "June" in rel_date:
						year = rel_date[:4]
						date = "6/"+year
					elif "July" in rel_date:
						year = rel_date[:4]
						date = "7/"+year
					elif "August" in rel_date:
						year = rel_date[:4]
						date = "8/"+year
					elif "September" in rel_date:
						year = rel_date[:4]
						date = "9/"+year
					elif "November" in rel_date:
						year = rel_date[:4]
						date = "10/"+year
					elif "October" in rel_date:
						year = rel_date[:4]
						date = "11/"+year
					elif "December" in rel_date:
						year = rel_date[:4]
						date = "12/"+year
					else:
						date = "No date found"
				i += 1
		except IndexError:
			date = "No date found"
		price = content[0].find_all('span')
		stripped = price[0].text.replace('RS ', '')
		return stripped,date
	except Exception as e:
		return 'Search manually', 'No date found'
	
def homeshopping(query):
	try:
		response = get(query)
		soup = BeautifulSoup(response.text, features="html.parser")
		content_price = soup.find_all('div', attrs={"class":"ActualPrice"})
		stripped = content_price[0].text.strip()
		stripped = stripped.replace('Rs ', '')
		# print(stripped)
		return stripped
	except:
		return "Search manually"


def main():

	f=open("b1.txt", "r")
	f1 = open("TFS_PHONEPRICES_5JAN2021_B2.txt", "a")
	contents =f.readlines()

	for line in tqdm.tqdm(contents):
		total_sum = 0
		counter = 0
		date = ''
		inp1 = line +'price in Pakistan whatmobile'
		inp2 = line + 'price in Pakistan propakistani'
		inp3 = line + 'price in Pakistan priceoye'
		inp4 = line + 'price in Pakistan homeshopping'

		price1 = 0
		price2 = 0
		price3 = 0

		try: 
			from googlesearch import search 
			import re
		except ImportError:  
			print("No module named 'google' found") 
		results=[]
		for j in search(inp1, tld="com", num=10, stop=5, pause=2): 
			price = get_mobile_data_whatmobile(j)
			if price == 'Search manually' or price == 'Accessories':
				s =  (price)
			else:
				try:
					price = int(price)
					total_sum += price
					counter += 1
				except ValueError:
					error =('Search manually')
			break

		for j in search(inp3, tld="com", num=10, stop=5, pause=2): 
			price = get_mobile_data_priceoye(j)
			if price == 'Search manually':
				s = (price)
			elif price != 'Search manually':
				try:
					price = price.replace(',','')
					price = price.replace('Rs. ', '')
					price1 = int(price)
					total_sum += price1
					counter += 1
					# print(price1)
				except ValueError:
					error = ('Search manually')
			break

		for j in search(inp2, tld="com", num=10, stop=5, pause=2): 
			price, l_date = propakistani(j)
			if price == 'Search manually':
				s =  (price)
			elif price != 'Search manually':
				price = price.replace(',','')
				price = price.replace('Rs. ', '')
				try:
					price = price.replace('RS. ', '')
					price = price.replace('RS ', '')
					price2 = int(price)
					total_sum += price2
					counter += 1
				except ValueError:
					error = ('Search manually')
				
				# print(price2)
			break


		for j in search(inp4, tld="com", num=10, stop=5, pause=2): 
			price = homeshopping(j)
			if price == 'Search manually':
				s = (price)
			elif price != 'Search manually':
				try:
					price = price.replace(',','')
					price3 = int(price)
					total_sum += price3
					counter += 1
					# print(price3)
				except ValueError:
					error = ('Search manually')
			break
		if counter == 0:
			f1.write(''.join('{} {} {}'.format(line , ';', "Search manually")))
			f1.write('\n')
		else:
			f1.write(''.join('{} {} {} {} {}'.format(line.strip(),';', int(total_sum/counter),';',l_date)))
			f1.write('\n')

			

		# print(line), 
		# print(int(total_sum/counter))
		# print("Release Data =", l_date)
		

	# get_google_searches(inp)
		


	# # print(inp)

	

if __name__ == '__main__':
	main()