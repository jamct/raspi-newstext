import feedparser
d = feedparser.parse('https://www.heise.de/newsticker/heise-atom.xml')

def writeNews(headline, oFile,position):
    line = position*3 + 9
    oFile.write("\nOL,"+str(line)+", "+headline[0:40])
    line = line+1
    oFile.write("\nOL,"+str(line)+", "+headline[40:80])

template = open("template.txt", "r") 
header = template.read()

outputfile = open("P100.tti", "w")

outputfile.write(header)
writeNews(d['entries'][0]['title'], outputfile, 0)
writeNews(d['entries'][1]['title'], outputfile, 1)
writeNews(d['entries'][2]['title'], outputfile, 2)
writeNews(d['entries'][3]['title'], outputfile, 3)
outputfile.close()

#copy to /home/pi/teletext
from shutil import copyfile
copyfile('P100.tti', '/home/pi/teletext/P100.tti')
