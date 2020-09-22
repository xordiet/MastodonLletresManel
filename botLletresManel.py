from mastodon import Mastodon
import random
import csv

# Set up Mastodon
mastodon = Mastodon(
	access_token = 'tokenManel.secret',
	api_base_url = 'https://mastodont.cat/'
)


rand = random.randint(0,6)
if rand == 3:
	lletres = []
	with open('frases.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		i=0
		for row in spamreader:
			i += 1
			lletres.append(row)
		randn = random.randint(1, i)
		#print (rand)
		#print ("🎤 "+lletres[rand][0]+" 🎶 "+lletres[rand][1]+" 💿 "+lletres[rand][2])
		mastodon.status_post("🎤 "+lletres[randn][0]+"  🎶 "+lletres[randn][1]+"  💿 "+lletres[randn][2])
