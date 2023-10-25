#importing libraries
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
from os.path import join, dirname, realpath

#function for toasting notification
def notifyus(title, message):
	notification.notify(
		title = title,
		message = message,
		app_icon = join(dirname(realpath(__file__)),
         'icons8_Virus.ico',),
		timeout = 10,
	)

#function for downloading updated data from government of india website (https://www.mohfw.gov.in/)
def getdata(url):
	r = requests.get(url)
	return r.text


#programm starting
if __name__ == '__main__':
	#exception handling
	try:
		#analysing gathered data 
		data = getdata("https://www.mohfw.gov.in/")
		soup = BeautifulSoup(data,"html.parser")
	    # soup.prettifying data 
		data_str = ""
		for tr in soup.find_all("tbody")[1].find_all("tr"):
			data_str += tr.get_text()
		states = ['Uttar Pradesh','Delhi','Maharashtra','Punjab','Rajasthan']
		data_str = data_str[1:]
		item_1 = data_str.split("\n\n")
		#expressing data into readable toast notification format 
		for item in item_1[0:23]:
					data_list = item.split("\n")
					if data_list[1] in states:
						#print(data_list)
						title ="Covid-19 live status"
						text = f" State: {data_list[1]}\nIndians: {data_list[2]} & Forigners: {data_list[3]}\nCured: {data_list[4]}\nDeaths: {data_list[5]}"
						notifyus(title,text)
						time.sleep(10)
		notifyus("Covid-19 live status","Helpline Number Toll free: 1075:\n+91-11-23978046\nHelpline Email ID :\nncov2019@gov.in")
	except :
		notifyus("Covid-19 live status","Could not connect to the server.\n Please connect to a better internet service")
