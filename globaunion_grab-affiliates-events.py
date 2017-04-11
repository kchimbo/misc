#!/usr/bin/env python

__author__ = "Osamu Fujimoto"
__version__ = "1.0"
__email__ = "oaf7862@rit.edu"

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import re

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

## Club Missing: Wells Project
CLUBS = [
	'https://thelink.rit.edu/organization/AsianCulture/events',
	'https://thelink.rit.edu/organization/AsianDeaf/events',
	'https://thelink.rit.edu/organization/Capoeira/events',
	'https://thelink.rit.edu/organization/CSA/events',
	'https://thelink.rit.edu/organization/Chinese/events',
	'https://thelink.rit.edu/organization/DISA/events',
	'https://thelink.rit.edu/organization/Ebony/events',
	'https://thelink.rit.edu/organization/french/events',
	'https://thelink.rit.edu/organization/I-House/events',
	'https://thelink.rit.edu/organization/lsualkimia/events',
	'https://thelink.rit.edu/organization/Pi_Chi/events',
	'https://thelink.rit.edu/organization/lambdas/events',
	'https://thelink.rit.edu/organization/LADeaf/events',
	'https://thelink.rit.edu/organization/LRDC/events',
	'https://thelink.rit.edu/organization/Malaysia/events',
	'https://thelink.rit.edu/organization/MSA/events',
	'https://thelink.rit.edu/organization/LAStudents/events',
	'https://thelink.rit.edu/organization/NativeAmStuAssc/events',
	'https://thelink.rit.edu/organization/OASIS/events',
	'https://thelink.rit.edu/organization/OAS/events',
	'https://thelink.rit.edu/organization/PiazzaItaliana/events',
	'https://thelink.rit.edu/organization/Bhangra/events',
	'https://thelink.rit.edu/organization/Story/events',
	'https://thelink.rit.edu/organization/UNICEF/events',
	'https://thelink.rit.edu/organization/russian/events',
	'https://thelink.rit.edu/organization/TaiwaneseCultureAssociation/events',
	'https://thelink.rit.edu/organization/Unity_House/events'
	]

class TheLink:
	## Some events are not public thus, we need to login. Check if we have the RIT username and
	## password on the environments variables or login manually if they're not available.
	def __init__(self):
		self.driver = webdriver.Chrome(chromedriver)
		self.wait = WebDriverWait(self.driver, 10)
		self.driver.get('https://thelink.rit.edu/account/logon')
		
		#username = os.environ.get('RITUSERNAME')
		#password = os.environ.get('RITPASSWORD')
		
		##
		## PUT YOUR RIT USERNAME AND PASSWORD HERE
		## TODO: Find a more secure way to store the user and password. Maybe using an external file?
		##
		#username = ''
		#password = ''
		if username is None and password is None:
			input('Enter your username and password and press [Enter]')
		else:
			self.login(username, password)
		
	def login(self, username, password):
		usr = self.driver.find_element_by_xpath('//*[@id="username"]')
		psw = self.driver.find_element_by_xpath('//*[@id="password"]')
		
		usr.send_keys(username)
		psw.send_keys(password)

		login = self.driver.find_element_by_xpath('//*[@id="userInput"]/form/button')

		login.click()
	
	def close(self):
		self.driver.close()
		
class Event():
	def __init__(self, club, name, start, end):
		self.club = club
		self.name = name
		self.start = start
		self.end = end
	def __str__(self):
		if (self.end.tm_year == 1900):
			start_time = time.strftime("%a %b %d %H:%M:%S", self.start)
			end_time = time.strftime("%H:%M:%S", self.end)
			year = time.strftime("%Y", self.start)
			return "%s: %s (%s - %s %s)" % (self.club, self.name, start_time, end_time, year)
		else:
			return "%s: %s (%s to %s)" % (self.club, self.name, time.strftime("%c", self.start), time.strftime("%c", self.end))
class GrabEvents(TheLink):
	events = []
	def __init__(self, sleep=0):
		super().__init__()
		self.d = self.driver
		self.w = self.wait
		for club in CLUBS:
			self.grab(club)
			if sleep > 0:
				time.sleep(sleep)
		
		self.events.sort(key=lambda r: r.start)

		print("\n%d events found:\n" % len(self.events))

		for e in self.events:
			print(str(e))
			
		super().close()
			 
	def grab(self, url):
		self.d.get(url)
		## TODO: 	Instead of applying a Regular Expression to the URL, grab the club name from the
		##			body of the page
		re_club = re.match("^.*\/([^-]*)\/.*$", url, re.M)
		club_name = re_club.group(1)
		try:
			upcoming_events = self.d.find_element_by_class_name('container-upcomingevents')
		except Exception:
			print("ERROR on %s: Missing /events on the url")
			upcoming_events == 'No events.'
		if (upcoming_events.text != "No events."):
			## TODO: Check if we have more than one page of events and grab them.
			events = upcoming_events.find_elements_by_tag_name('ul')
			print("Grabbing events from %s: %d event(s) found" % (re_club.group(1), len(events)))
			for event in events:
				en = event.find_element_by_tag_name('h4').text
				dt = event.find_element_by_tag_name('p').text
				dts = dt.split(" to ")
				try:
					start = time.strptime(dts[0], "%m/%d/%Y, %I:%M %p")
					end = time.strptime(dts[1], "%m/%d/%Y, %I:%M %p")
				except Exception:
					end = time.strptime(dts[1], "%I:%M %p")
				self.events.append(Event(club_name, en, start, end))
		else:
			print("Grabbing events from %s: No events" % re_club.group(1))

if __name__ == '__main__':
	GrabEvents()
