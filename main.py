####Yakub 2021
#### License: AGPLv3
##In summary you can copy and paste but your implementation must be free and open source. You must also reference the original project.

####import modules

import os
from random import choice
#brute force win conditions
####define constants

winconditions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

####define functions

#generate table
def generatetable(data):
  return (
    """
  {}|{}|{}
  -----
  {}|{}|{}
  -----
  {}|{}|{}""".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]))

#convert data into list
def convertdata(datadict):
  datalist = [1,2,3,4,5,6,7,8,9]
  for i in range(len(datalist)):
    datalist[i] = f"\033[32m{datalist[i]}\033[m"
  for i in datadict.get("Crosses"):
    datalist[i-1] = "\033[31mX\033[m"
  for i in datadict.get("Noughts"):
    datalist[i-1] = "\033[36m0\033[m"
  return datalist

def claim(playerdata,square):
  playerdata.get("Unclaimed").remove(square)
  playerdata.get(player).append(square)
  playerdata.get(player).sort()
  return playerdata

def computermove(playerdata):
  global winconditions, player
  moved=False
  unclaimed = playerdata.get("Unclaimed")
  if (len(playerdata.get(player))>=2) and not (moved):
    claimed = playerdata.get(player)
    for i in winconditions:
        matches = list(set(i)-set(claimed))
        matches.sort()
        if len(matches) == 1:
          if matches[0] in unclaimed:
            playerdata = claim(playerdata, matches[0])
            moved=True
  if len(playerdata.get("Noughts")) >= 2 and not (moved) and player != "Noughts":
    claimed = playerdata.get("Noughts")
    for i in winconditions:
        matches = list(set(i)-set(claimed))
        matches.sort()
        if len(matches) == 1 :
          if matches[0] in unclaimed:
            playerdata = claim(playerdata, matches[0])
            moved=True
  if len(playerdata.get("Crosses")) >= 2 and not (moved) and player != "Crosses":
    claimed = playerdata.get("Crosses")
    for i in winconditions:
        matches = list(set(i)-set(claimed))
        matches.sort()
        if len(matches) == 1 :
          if matches[0] in unclaimed:
            playerdata = claim(playerdata, matches[0])
            moved=True
  if 5 in playerdata.get("Unclaimed") and not (moved):
    playerdata = claim(playerdata, 5)
    moved = True
  if not moved:
    playerdata = claim(playerdata, choice(playerdata.get("Unclaimed")))
    moved = True
  return playerdata

#drawtable
def drawtable(table):
  #os.system("clear")
  print(table)
  print()

#define player data    
playerdata = {"Unclaimed":[1,2,3,4,5,6,7,8,9], "Crosses":[], "Noughts": []}
#define start player
player = "Noughts"
gamewon=False
square=1
firstmove=True

while not gamewon:
  data = convertdata(playerdata)
  table = generatetable(data)
  drawtable(table)
  if not firstmove:
    if square not in playerdata.get("Unclaimed"):
      print("Please choose a number that has not already been claimed")
  square = input(f"{player} what square would you like to claim: ")
  try:
    square = int(square)
  except:
    print("please enter a number")
    pass
  if square not in playerdata.get("Unclaimed"):
    firstmove=False
    pass
  else:
    firstmove=True
    playerdata = claim(playerdata,square)
    claimed = playerdata.get(player)
    if len(claimed) >= 3:
      for i in winconditions:
        matches = list(set(i) & set(claimed))
        matches.sort()
        if matches == i:
          data = convertdata(playerdata)
          table = generatetable(data)
          drawtable(table)
          print(f"{player} wins!")
          gamewon=True
          break
    if (len(playerdata.get("Unclaimed")) == 0) and (not gamewon):
      data = convertdata(playerdata)
      table = generatetable(data)
      drawtable(table)
      print("Draw!")
      gamewon=True
      break
    player = "Crosses"
    playerdata =computermove(playerdata)
    claimed = playerdata.get(player)
    if len(claimed) >= 3:
      for i in winconditions:
        matches = list(set(i) & set(claimed))
        matches.sort()
        if matches == i:
          data = convertdata(playerdata)
          table = generatetable(data)
          drawtable(table)
          print(f"{player} wins!")
          gamewon=True
          break
    player = "Noughts"