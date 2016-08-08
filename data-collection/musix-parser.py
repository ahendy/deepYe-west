import xml.etree.ElementTree as ET
import requests
import xml
import urllib
import time

from conf import MUSIX

song_list_path = "data/kanye-songs.txt"
base_url = 'http://api.musixmatch.com/ws/1.1/%s'
artist = 'Kanye West'
lyric_path = "data/30lyrics.txt"


song_count = 0
unwritten_songs = []
# root = ET.Element("data")
# doc = ET.SubElement(root, "lyrics")

with open(lyric_path, 'w+') as lf:
    with open(song_list_path, 'r') as f:

        lines = f.readlines()
        num_songs = len(lines)

        for title in lines:

            lyric_url = base_url % ("matcher.lyrics.get")
            params = {
                'q_track': title,
                'q_artist': artist,
                'apikey': MUSIX,
            }
            
            try:      
                response = requests.get(lyric_url, params)
                print "Begin parsing ", title, "response, ", response.status_code
                import json 
                import os
                if response.status_code == 200:

                        lyric = json.loads(response.content)['message']['body']['lyrics']['lyrics_body']
                        lines = lyric.splitlines()[:-3]
                        for line in lines:
                            line = line.encode('ascii', 'ignore')
                            lf.write(line+'\n')

                        song_count += 1

                        continue
                
                print 'API error:'
                unwritten_songs.append(title)
           
            except Exception as e:
                # Safely recover just incase api call is killed with exception
                print e
                print "Request went bad, connection was killed"
                unwritten_songs.append(title)
            
            else:
                print "%d/%d songs songs have been written." % (song_count, num_songs)


print "Songs Completed"
print "Number of songs written: %d" % (song_count,)
print "Number of songs missed: %d" % (len(unwritten_songs))
print "They are:\n %s" % (", ".join(unwritten_songs))
# tree = ET.ElementTree(root)
# tree.write(lyric_path)

