import xml.etree.ElementTree as ET

e = ET.parse('every-kanye-song.xml').getroot()

with open('kanye-songs.txt', 'w') as f:
	for li in e.findall('li'):
		song_title = li[0].text
		f.write(song_title + '\n')
	