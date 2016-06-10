from splinter import Browser
import time

#open the file and make an list out of it
with open("jline_targets.txt") as b:
	lines = b.readlines()
	
#declare the counter variable
counter = 0

for i in range (0, 100):
	with Browser() as browser:
		mail = lines[counter]
		browser.visit("http://www.jlinemusic.com/go/members/download/track/903145")
		try:
			browser.fill("member[email]", mail)
			browser.find_by_name("save").click
		except ElementDoesNotExist:
			pass
		
		counter = counter + 1
