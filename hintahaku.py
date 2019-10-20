import re
import requests
import sys
from bs4 import BeautifulSoup # beautiful soup nelonen
from csv import writer        # tää kirjottaa csv-tiedostoihin

print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))

for a in sys.argv:
  print(a)

#response = requests.get('https://senseisdiviningshop.fi/search?q=swords+to+plowshares')
#soup = BeautifulSoup(response.text, 'html.parser')
#response = requests.get('https://senseisdiviningshop.fi/search?q=celestial+archon')
#soup = BeautifulSoup(response.text, 'html.parser')

# string
# "https://senseisdiviningshop.fi/search?q=" + string.replace(" ", "_")

try:
  with open('hintahaku.txt', 'r') as file:
    data = file.readlines()
except:
  print('ERROR. error. ERROR. error. \nHintahaku.txt puuttuu.')
  file = open('hintahaku.txt', 'w') 
  file.write("Kirjoita kortit tähän yks per rivi. Tyyliin: \nSwords to Plowshares\nCraw Wurm")
  file.close()
  quit()

for line in data:
  print("https://senseisdiviningshop.fi/search?q=" + line.replace(' ', '+'))

# toimivalla sivulla:
soup = BeautifulSoup(open('C://Users/kayttaja/Documents/koodaus/python/hintahaku/sivu.html'), 'html.parser')
# tyhjällä sivulla: 
#soup = BeautifulSoup(open('C://Users/kayttaja/Documents/koodaus/python/hintahaku/sivu2.html'), 'html.parser')

print_to_file = True

#get all cards on the page
content = soup.find(class_='col-sm-12')
content_column = content.find_all(class_="col-xs-3") #[2]
rows = soup.find(class_='col-sm-12').find_all(class_='row')

#toimiva proto tyyppi
try:
  card_name = content.find('h4', string=True).get_text()
except:
  print('ERROR. error. ERROR. error. \nOnko sivu tyhjä?')
  quit()
card_edition = content('p')
card_stock_amount = content_column[2].find_all('li')[1].get_text()

# alota tästä:
##############

row = []

for num, r in enumerate(rows, start=0):
  if len(r) > 3:
    row.append(r)

print (card_name)
for num, r in enumerate(row, start=1):
  print('{}. {} - {} € - {} kpl'.format(num, r.find('p').get_text(), r(class_='col-xs-3')[3].find_all('li')[1].get_text(), r(class_='col-xs-3')[2].find_all('li')[1].get_text() ))

if (print_to_file == True):
  file = open('sensei.txt', 'w') 

  file.write(card_name)
  for num, r in enumerate(row, start=1):
    file.write('\n{}. {} - {} € - {} kpl'.format(num, r.find('p').get_text(), r(class_='col-xs-3')[3].find_all('li')[1].get_text(), r(class_='col-xs-3')[2].find_all('li')[1].get_text() ))
  
  file.close()
  print("\nFile created.")
else:
  print("\nNo file created.")


## kirjota nää funktioiksi

# TODO:
# mitä skriptin pitäs tehdä:
# 1. avaa ja lukee tekstitiedoston
# 2. muuntaa sieltä kaikki rivit muotoon sana+toinen+sana
# 3. palauttaa sen listana takaisin
# 4. avaa yksi kerrallaan kaikki listassa olevat kortit sieltä kaupasta,
## siten että lisää ne sinne linkin perään: "shop.fi/search?q=" + string
# 5. käyttää sen avatun sivun sen parserin tai jäsentäjän läpi
# 6. jäsentäjä jäsentää sieltä sivulta kortin setin, hinnan ja montako
## niitä on jäljellä mitäkin
# 7. läpi käydyt kortit lisätään tekstitiedoston loppuun
## (missä vois lukee kyllä päiväyskin)

## TODO:
 #sisään tulee file
  #return: lista missä on ne plussat+sisään+leivottuna
  # sitä voi sit käyttää sillee, että sinne syötetään se lista, missä on siis kortit riveittäin ja se antaa ulos sen listan nimistä, minkä voi sit laittaa linkin lopuks tyylillä: for d in data: 'www.linkki.com/' + d
  # nii ja jos sitä filettä ei laita tai jotai, nii se antaa ton testisivun
##
def initiate_data_file( file ):
  try:
    with open(f +'.txt', 'r') as file:
      data = file.readlines()
  except:
    print('ERROR. error. ERROR. error. \nHintahaku.txt puuttuu.')
    file = open('hintahaku.txt', 'w') 
    file.write("Kirjoita kortit tähän yks per rivi. Tyyliin: \nSwords to Plowshares\nCraw Wurm")
    file.close()

  for line in data:
    print("https://senseisdiviningshop.fi/search?q=" + line.replace(' ', '+'))

  file.close()

def output_to_file():
  for num, r in enumerate(row, start=1):
    file.write('\n{}. {} - {} € - {} kpl'.format(num, r.find('p').get_text(), r(class_='col-xs-3')[3].find_all('li')[1].get_text(), r(class_='col-xs-3')[2].find_all('li')[1].get_text() ))


  #  num,                                                  # index
  #  r.find('p').get_text(),                               # set
  #  r(class_='col-xs-3')[3].find_all('li')[1].get_text(), # stock
  #  r(class_='col-xs-3')[2].find_all('li')[1].get_text()  # price