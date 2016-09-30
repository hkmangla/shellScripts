import sys
import os
import wget
import webbrowser
#print "Playing.... " + name
#webbrowser.open("https://www.youtube.com/results?search_query="+name)
def youtube_search(name):
	file_name=wget.download("https://www.youtube.com/results?search_query="+name)
	searchids = []
	with open("results") as file:
		for line in file:
			searchId = "data-context-item-id="
			if searchId in line:
				index = line.find(searchId) + len(searchId)
				l = line[index+1:index+25].find('"')
				searchids.append(line[index:index+l+2])
	print searchids
	webbrowser.open("https://www.youtube.com/watch?v="+searchids[1][1:-1])
	os.remove("results")
def facebook_search(name):
	webbrowser.open("https://www.facebook.com/search/top/?q="+name)
def google_search(name):
	webbrowser.open("https://www.google.co.in/search?q="+name)

print "What type of search do you want?"
print "1) Google"
print "2) Facebook"
print "3) Youtube"
opt = raw_input()
print "\n What do you want to search"
name = raw_input()
if opt in ['1','Google','google']:
	google_search(name)
if opt in ['2','Facebook','facebook']:
	facebook_search(name)
if opt in ['3','Youtube','youtube']:
	youtube_search(name)


