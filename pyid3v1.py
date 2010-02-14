#!/usr/bin/env python
#pyid3v1.py
#Simple python ID3v1 reading library implementation
#Released under BSD License

import sys

genres= [ "Blues","Classic Rock","Country","Dance","Disco","Funk","Grunge","Hip-Hop"
        ,"Jazz","Metal","New Age","Oldies","Other","Pop","R&B","Rap","Reggae","Rock"
        ,"Techno","Industrial","Alternative","Ska","Death Metal","Pranks","Soundtrack"
        ,"Euro-Techno","Ambient","Trip-Hop","Vocal","Jazz+Funk","Fusion","Trance","Classical"
        ,"Instrumental","Acid","House","Game","Sound Clip","Gospel","Noise","Alternative Rock"
        ,"Bass","Punk","Space","Meditative","Instrumental Pop","Instrumental Rock","Ethnic"
        ,"Gothic","Darkwave","Techno-Industrial","Electronic","Pop-Folk","Eurodance","Dream"
        ,"Southern Rock","Comedy","Cult","Gangsta","Top 40","Christian Rap","Pop/Funk","Jungle"
        ,"Native US","Cabaret","New Wave","Psychedelic","Rave","Showtunes","Trailer","Lo-Fi"
        ,"Tribal","Acid Punk","Acid Jazz","Polka","Retro","Musical","Rock&Roll","Hard Rock"
        ,"Folk","Folk-Rock","National Folk","Swing","Fast Fusion","Bebop","Latin","Revival"
        ,"Celtic","Bluegrass","Avantgarde","Gothic Rock","Progressive Rock","Psychedelic Rock"
        ,"Symphonic Rock","Slow Rock","Big Band","Chorus","Easy Listening","Acoustic","Humour"
        ,"Speech","Chanson","Opera","Chamber Music","Sonata","Symphony","Booty Bass","Primus"
        ,"Porn Groove","Satire","Slow Jam","Club","Tango","Samba","Folklore","Ballad","Power Ballad"
        ,"Rhytmic Soul","Freestyle","Duet","Punk-Rock","Drum Solo","Acappella","Euro-House"
        ,"Dance Hall","Goa","Drum&Bass","Club-House","Hardcore","Terror","Indie","BritPop"
        ,"NegerPunk","Polsk Punk","Beat","Christian Gangsta","Heavy Metal","Black Metal","Crossover"
        ,"Contemporary","Christian Rock","Merengue","Salsa","Thrash Metal","Anime","JPop","SynthPop" ]

class ID3InitError(Exception):
    pass
    
class ID3info:
    def __init__(self,path):
        self.path=path
        f=file(path,"rb")
        f.seek(-128, 2)
        self.data=f.read(128)
        self.id3=[]
        if(self.data[0:3])!='TAG':
            raise ID3InitError
	self.songtitle=((self.data[3:33]).replace("\00"," ")).strip()
	self.id3.append(self.songtitle)
	self.artist=((self.data[33:63]).replace("\00"," ")).strip()
	self.id3.append(self.artist)
	self.album=((self.data[63:93]).replace("\00"," ")).strip()
	self.id3.append(self.album)
	self.year=((self.data[93:97]).replace("\00"," ")).strip()
	self.id3.append(self.year)
	self.comment=((self.data[97:127]).replace("\00"," ")).strip()
	self.id3.append(self.comment)
	if(ord(self.data[-1]))>=147:
            self.genre="Unknown"
        else:
            self.genre=genres[(ord(self.data[-1]))]
	self.id3.append(self.genre)
    def retrieve_list(self):
        return self.id3
    def printdata(self):
	print "Title:",self.songtitle
	print "Artist:",self.artist
	print "Album:",self.album
	print "Year:",self.year
	print "Comment:",self.comment
	print "Genre:",self.genre

a=ID3info(sys.argv[1])
a.printdata()
print a.retrieve_list()
