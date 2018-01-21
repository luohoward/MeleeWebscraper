from bs4 import BeautifulSoup
import requests
import codecs

def parseSite(href):
    link = 'https://www.ssbwiki.com' + href
    r = requests.get(link)
    htmlData = r.text
    parseString = ""

    if '<span class="mw-headline" id="Super_Smash_Bros._Melee_singles">' in htmlData:
        parseString = '<span class="mw-headline" id="Super_Smash_Bros._Melee_singles">'
    elif '<span class="mw-headline" id="Melee_singles">' in htmlData:
        parseString = '<span class="mw-headline" id="Melee_singles">'
    elif '<span class="mw-headline" id="Singles">':
        parseString = '<span class="mw-headline" id="Singles">'
    else:
        parseString = '<table class="wikitable collapsible" style="text-align:center">'


    i = htmlData.split(parseString)
    retString = ""

    try:
        meleeSoup = BeautifulSoup(i[1])
    except IndexError:
        # Legit only to handle the EVO West Case
        meleeSoup = BeautifulSoup(i[0])

    trs = meleeSoup.find_all("tr")
    firstPlace = ""
    for tds in trs:
        if '1st' in str(tds):
            firstPlace = tds
            break

    for subItem in firstPlace.find_all("td"):
        if len(subItem.find_all('a')) != 0:
            seenSmasher = False
            for link in subItem.find_all('a'):
                title = link.get('title')
                if title == None:
                    continue
                elif 'Smasher:' in title or '(SSBM)' in title:
                    if 'Smasher:' in title and seenSmasher and '(SSBM)' in retString:
                        return retString
                    elif 'Smasher:' in title and seenSmasher:
                        continue
                    else:
                        retString += title + "\t"
                        if 'Smasher:' in title:
                            seenSmasher = True



    return retString


r = requests.get('https://www.ssbwiki.com/List_of_national_tournaments')
data = r.text

#got the text above. Was easier to use brawl for melee data
meleeText = data.split("Super Smash Bros. Brawl")[1].split("/h2")[2][1:] + "\"</h2>"
meleeSoup = BeautifulSoup(meleeText)

rows = meleeSoup.find_all("tr")

saveString = ""
year = 2002

for item in rows:
    if len(item.find_all("th")) != 0:
        year += 1
        if year == 2019:
            break

        saveString += str(year) + "\n"
    else:
        value = ""
        if "TBD" in item.find_all("td")[-1].get_text():
            break 
        else:
            for subItem in item.find_all("td"):
                if len(subItem.find_all('a')) != 0:
                    for link in subItem.find_all('a'):
                        href = link.get('href')
                        title = link.get('title')
                        if ".png" in href or "/Smasher:" in href:
                            continue
                        else:
                            s = parseSite(href).strip()
                            if "(SSBM)" in s and 'Smasher:' in s:
                                saveString += title + "\t" + parseSite(href).strip() + "\n"

saveString = saveString.replace("Dr. PeePee", "PPMD") 

f = codecs.open("tournamentResults.txt", 'w', encoding='utf8')
f.write(saveString)
