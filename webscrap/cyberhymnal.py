# url = 'http://cyberhymnal.org/htm/a/b/abidinme.htm'
url = 'http://cyberhymnal.org/htm/j/g/jgfbless.htm'
response = requests.get(url, headers=headers,auth=auth)
data = response.text
soup = BeautifulSoup(data,"lxml")

song_composers =  soup.body.table.find("td").findAll("p")
sc = []
for s in song_composers:
    sc.append(s.get_text().replace("&shy;",""))
    print(s.get_text().replace("&shy;",""))
# song_music =  soup.find('span',attrs={"class":"music"})
# print(song_music)

song_lyrics =  soup.find('div',attrs={"class":"lyrics"})
print(song_lyrics)

print(sc[0])
composer = re.findall("bio\(\"(.*)\",",sc[0])
year = re.findall("\d{4}",sc[0])
print("Composer is ",composer[0]," Year ",year[0])
final = re.sub("bio\(\"(.*)\",.*?\)",r"\1",sc[0])
print(final)

print(sc[1])
music = re.sub("bio\(\"(.*)\",.*?\)",r"\1",sc[1])
music = re.sub("lmn\(\".*","",music)
print(music)
