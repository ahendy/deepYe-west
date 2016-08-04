import xml.etree.ElementTree as ET
import requests
import xml
import urllib


song_list_path = "kanye-songs.txt"
base_url = 'http://api.chartlyrics.com/apiv1.asmx/%s'

"""
With http://www.chartlyrics.com/api.aspx
Retrive all songs.
SearchLyric input <- kanye west and SONG
EG: SearchLyric?artist=kanye%20west&song=power
then, use XML parser to retrive LyricId, LyricChecksum.
Now call GetLyric api with 
GetLyric?lyricId=<LyricID>&lyricCheckSum=<LyricCheckSum>
"""
with open(song_list_path, 'r') as f:

    lines = f.readlines()
    for title in lines:

        lyric_url = base_url % ("SearchLyricDirect")
        params = {
            'artist': 'Kanye West',
            'song': title
        }
        response = requests.get(lyric_url, params)
        print response.status_code

        if response.status_code == 200:

            song_xml = response.text
            e = ET.fromstring(song_xml)
            lyrics = e[-1].text

        else:
            print 'API error:', response.text
