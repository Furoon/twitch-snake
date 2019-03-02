from twitch import TwitchHelix
from itertools import islice
import time
import json
import os
import datetime
import time


channel_user_id = ""	    #Platzhaltervariable
channel_user_name = ""      #Platzhaltervariable
channel_game_id = ""        #Platzhaltervariable
channel_community = ""      #Platzhaltervariable
channel_type =  ""          #Platzhaltervariable
channel_title =  ""         #Platzhaltervariable
channel_viewer_count = ""   #Platzhaltervariable
channel_started_at = ""     #Platzhaltervariable
channel_language = ""       #Platzhaltervariable
channel_thumbnail_url = ""  #Platzhaltervariable
channel_tag_ids = ""        #Platzhaltervariable

path = '" YOUR_OWN_PATH'

date = datetime.datetime.now().strftime("%y_%m_%d_%H_%M")
twitch = ' "https://www.twitch.tv/'
Dateiname = date + ".mpg"

# channel_user_login = "larsfest" #Gibt an welcher Channel ?berpr?ft werden soll

def get_stream_data(n):
	client = TwitchHelix(client_id='YOUR_OWN_CLIENTID_FROM_TWITCH') #ClientID vom Script f?r Twitch (Auth)
	streams_iterator = client.get_streams(page_size=100, user_logins=n) #Reqeust aller Streamdaten als iterator (Zeiger)
	for stream in islice(streams_iterator, 0, 500):			#islice spaltet den iterator in die Variablen auf
		global channel_user_id                                  #ruft erst die globale Variable auf um diese dann zu beschreiben
		channel_user_id = stream["user_id"]                     #ruft erst die globale Variable auf um diese dann zu beschreiben
		global channel_user_name                                #ruft erst die globale Variable auf um diese dann zu beschreiben
		channel_user_name = stream["user_name"]                 #ruft erst die globale Variable auf um diese dann zu beschreiben
		global channel_game_id                                  #ruft erst die globale Variable auf um diese dann zu beschreiben
		channel_game_id		= stream["game_id"]             #ruft erst die globale Variable auf um diese dann zu beschreiben
		global channel_community                                #ruft erst die globale Variable auf um diese dann zu beschreiben
		channel_community = stream["community_ids"]             #ruft erst die globale Variable auf um diese dann zu beschreiben
		global channel_type                                     #ruft erst die globale Variable auf um diese dann zu beschreiben
		channel_type = stream["type"]                           #ruft erst die globale Variable auf um diese dann zu beschreiben
		global channel_title                                    #ruft erst die globale Variable auf um diese dann zu beschreiben
		channel_title= stream["title"]                          #ruft erst die globale Variable auf um diese dann zu beschreiben
		global channel_viewer_count                             #ruft erst die globale Variable auf um diese dann zu beschreiben
		channel_viewer_count = stream["viewer_count"]         	#ruft erst die globale Variable auf um diese dann zu beschreiben
		global channel_started_at                               #ruft erst die globale Variable auf um diese dann zu beschreiben
		channel_started_at = stream["started_at"]               #ruft erst die globale Variable auf um diese dann zu beschreiben
		global channel_language                                 #ruft erst die globale Variable auf um diese dann zu beschreiben
		channel_language = stream["language"]                   #ruft erst die globale Variable auf um diese dann zu beschreiben
		global channel_thumbnail_url                            #ruft erst die globale Variable auf um diese dann zu beschreiben
		channel_thumbnail_url = stream["thumbnail_url"]         #ruft erst die globale Variable auf um diese dann zu beschreiben
		global channel_tag_ids                                  #ruft erst die globale Variable auf um diese dann zu beschreiben
		channel_tag_ids = stream["tag_ids"]                     #ruft erst die globale Variable auf um diese dann zu beschreiben
	return 0                                                        #ruft erst die globale Variable auf um diese dann zu beschreiben





def record(n):
	print(date+":"+ n + " is live and will be recorded")
	os.system("livestreamer"+twitch+n+path+n+"/"+" --http-ignore-env")

def main():
	n = input("Welchen Streamer möchtest du aufnehmen? ")
	get_stream_data(n)

	if channel_type == "live":
		record(n)
	else:
		print(date + ": " + channel_user_name + " isn't live... next check in five minutes")
		while channel_type == " ":
			time.sleep(300)
		else:
			record(n)


main()
