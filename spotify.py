
'''
This python script uses selenium.
It takes in two url's to spotify playlists. 
It goes through the first one and delete any songs that are already in the second one.
'''

playlist1 = "https://play.spotify.com/user/122685672/playlist/30Mg06NQXtaKzlt7XNtfpv"
playlist2 = "https://play.spotify.com/user/122685672/playlist/2rCm90tXbrcIVVzzFiGoZ7"
email = "rishub@gmail.com"
password = ""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.set_window_size(1804, 1096)
# driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
driver.get(playlist1)

driver.find_element_by_id('has-account').click()
driver.find_element_by_id('fb-login-btn').click()
time.sleep(2)
for handle in driver.window_handles:
    driver.switch_to_window(handle)
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("loginbutton").click()
for handle in driver.window_handles:
    driver.switch_to_window(handle)
time.sleep(10)
driver.switch_to_frame("app-player")
driver.find_element_by_id("play-pause").click()
driver.switch_to_default_content()
driver.switch_to_frame(10)

total = int(("").join(driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[1]/header/div/div/div[1]/span[3]").text.split(" ")[0].split(','))) - 1
while 1:
	count = -1
	for song in driver.find_elements_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr/td[3]/div"):
		count+=1
	driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(count + 1) + "]/td[3]/div").click()
	if count == total:
		break
	time.sleep(8)

first_songs, first_artists, second_songs, second_artists = [], [], [], []

for song in driver.find_elements_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr/td[3]/div"):
	first_songs.append(song.text)
	print song.text

for artist in driver.find_elements_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr/td[4]"):
	first_artists.append(artist.text)
	print artist.text
driver.close()








driver = webdriver.Firefox()
driver.set_window_size(1804, 1096)
driver.get(playlist2)
driver.find_element_by_id('has-account').click()
driver.find_element_by_id('fb-login-btn').click()
time.sleep(2)
for handle in driver.window_handles:
    driver.switch_to_window(handle)
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("loginbutton").click()
for handle in driver.window_handles:
    driver.switch_to_window(handle)
time.sleep(10)
driver.switch_to_frame("app-player")
driver.find_element_by_id("play-pause").click()
driver.switch_to_default_content()
driver.switch_to_frame(10)
total = int(("").join(driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[1]/header/div/div/div[1]/span[3]").text.split(" ")[0].split(','))) - 1
while 1:
	count = -1
	for song in driver.find_elements_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr/td[3]/div"):
		count+=1
	driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(count + 1) + "]/td[3]/div").click()
	if count == total:
		break
	time.sleep(8)

for song in driver.find_elements_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr/td[3]/div"):
	second_songs.append(song.text)
	print song.text

for artist in driver.find_elements_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr/td[4]"):
	second_artists.append(artist.text)
	print artist.text

i= 0
dups = []
while i < len(second_songs):
	j = 0
	while j < len(first_songs):
		if first_songs[j]==second_songs[i] and first_artists[j]==second_artists[i]:
			dups.append(j)
		j+=1
	i+=1

driver.close()








driver = webdriver.Firefox()
driver.set_window_size(1804, 1096)
# driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
driver.get(playlist1)
driver.find_element_by_id('has-account').click()
driver.find_element_by_id('fb-login-btn').click()
time.sleep(2)
for handle in driver.window_handles:
    driver.switch_to_window(handle)
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("loginbutton").click()
for handle in driver.window_handles:
    driver.switch_to_window(handle)
time.sleep(10)
driver.switch_to_frame("app-player")
driver.find_element_by_id("play-pause").click()
driver.switch_to_default_content()
driver.switch_to_frame(10)

total = int(("").join(driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[1]/header/div/div/div[1]/span[3]").text.split(" ")[0].split(','))) - 1
while 1:
	count = -1
	for song in driver.find_elements_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr/td[3]/div"):
		count+=1
	driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(count + 1) + "]/td[3]/div").click()
	if count == total:
		break
	time.sleep(8)


delete_songs, delete_artists = [], []
for i in dups:
	delete_songs.append(driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(i+1) + "]/td[3]/div").text)
	delete_artists.append(driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(i+1) + "]/td[4]").text)

print delete_songs
print delete_artists

greyed_songs, greyed_artists = [], []

dont = []

i = 0
while i < len(dups):
	if driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(dups[i] + 1) + "]").get_attribute("class") == "tl-row unavailable":
		dont.append(i)
	i+=1

i = 0
while i < len(dups):
	if i in dont:
		i+=1
		continue
	j = i
	while j < len(dups):
		if dups[j]>dups[i]:
			dups[j] = dups[j] - 1
		j+=1
	i+=1

i=0
for dup in dups:
	if driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(dup + 1) + "]").get_attribute("class") == "tl-row unavailable":
		greyed_songs.append(driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(dup + 1) + "]/td[3]/div").text)
		greyed_artists.append(driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(dup + 1) + "]/td[4]").text)
		print driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(dup + 1) + "]/td[3]/div").text + " greyed"
		i+=1
		continue
	driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(dup + 1) + "]/td[3]/div").click()
	driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(dup + 1) + "]/td[6]/button").click()
	print driver.find_element_by_xpath("//*[@id='pf-playlist-view']/div[1]/div[2]/table/tbody/tr[" + str(dup + 1) + "]/td[3]/div").text
	driver.switch_to_default_content()
	driver.switch_to_frame("context-actions")
	driver.find_element_by_id("delete-playlist-track").click()
	driver.switch_to_default_content()
	driver.switch_to_frame(10)
	time.sleep(2)
	i+=1


print greyed_songs
print greyed_artists



