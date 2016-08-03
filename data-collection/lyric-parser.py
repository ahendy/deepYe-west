
import requests
import xml
import urllib


"""
With http://www.chartlyrics.com/api.aspx
Retrive all songs.
SearchLyric input <- kanye west and SONG
EG: SearchLyric?artist=kanye%20west&song=power
then, use XML parser to retrive LyricId, LyricChecksum.
Now call GetLyric api with 
GetLyric?lyricId=<LyricID>&lyricCheckSum=<LyricCheckSum>
"""

params = {'artist': 'Kanye West'}
import pdb;pdb.set_trace()
