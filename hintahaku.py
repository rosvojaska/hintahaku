__author__ = 'jaska'

import re
import requests
from bs4 import BeautifulSoup # beautiful soup nelonen
from csv import writer        # tää kirjottaa csv-tiedostoihin

verbose = False

def report(string):
  if ( verbose ):
    return print(string)

def read_data_file( text ):
  "Opens the text file and parses it for card names"

  report( "Opening list: " + text )

  try:
    with open(text, 'r') as f:
      data = f.read().splitlines()
  except:
    report('ERROR: No such file.')
    quit()
  
  return data

def get_page_content( card ):
  "Takes in a string, opens the correct page and returns the content element"
  
  try:
    if (card == "local"):
      soup = BeautifulSoup(open('C://Users/kayttaja/Documents/koodaus/python/hintahaku/sivu.html'), 'html.parser')
      report("Opening page:\n" + card)
    else:
      link = "https://senseisdiviningshop.fi/search?q=" + card.replace(' ', '+')
      response = requests.get(link, verify=True)
      soup = BeautifulSoup(response.text, 'html.parser')
      report("Opening page:\n" + link)
  except:
    report("ERROR: No such page found")
    return False
  
  content = soup.find(class_='col-sm-12')

  return content

def get_card_data( content ):
  "Takes in the content element and returns values for the card. If no card is found returns False"

  try:
    card_name = content.find('h4', string=True).get_text()
  except:
    report('Could not find card data.')
    return False

  card_values = []
  row = []
  
  for num, r in enumerate(content.find_all(class_='row'), start=0):
    if len(r) > 3:
      row.append(r)

  report (card_name + ":")
  for num, r in enumerate(row, start=1):
    card_edition = r.find('p').get_text()
    card_stock = r.find_all(class_="col-xs-3")[2].find_all('li')[1].get_text()
    card_price = r.find_all(class_='col-xs-3')[3].find_all('li')[1].get_text()
    
    string = (" " + card_edition, card_stock, card_price)
    report(string)
    card_values.append('{}: {} € - {} left'.format(card_edition, card_price, card_stock))

  return card_name, card_values

### 🚀 🚀 🚀
# Actual script starts here:

data = read_data_file("hintahaku.txt")
file = open("output.txt", "w") 

for line in data:
  content = get_page_content( line )
  
  file.write(line + ":")

  if (get_card_data( content )):
    name, values = get_card_data(content)
    print("Looking up: " + name + "...")

    for i in values:
      file.write("\n " + i )

  else:
    file.write("\n Could not find card.")
  
  file.write("\n")

print(file.name + " created succesfully. I think.")
file.close()



# TODO time:
  # log the time when the output file was created
# TODO command lines:
  # import sys
  # import argparse

  # print ("This is the name of the script: ", sys.argv[0])
  # print ("Number of arguments: ", len(sys.argv))
  # print ("The arguments are: " , str(sys.argv))

  # for a in sys.argv:
  #   print(a)