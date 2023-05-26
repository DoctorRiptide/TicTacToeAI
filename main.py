
# imports #

import os
import random
import time

# globals #
row1 = ['#1', '#2', '#3']
row2 = ['#4', '#5', '#6']
row3 = ['#7', '#8', '#9']
board = [row1, row2, row3]

' Instance '

class Game:
  def __init__(self, board):
    self.row1 = board[0]
    self.row2 = board[1]
    self.row3 = board[2]
    self.board = board


  def render(self):
    for row in self.board:
      for place in row:

        if int(row.index(place))  != (2):  
          print(place.strip('#'), end='')
          print(' | ', end='')

        else:
          print(place.strip('#'), end='')

      if int(self.board.index(row)) != 2:
        print('\n----------')

  def menu(self):
    while True:
      print('Hello! Welcome to the....')
      time.sleep(2)
      print('\nULTIMATE TIC TAC TOE')
  
      time.sleep(2)
  
      print('\nSelect an option:\n1) CPU\n2) PVP')
      selection = input('\nType Here > ')
  
      if 'v' in selection.lower() or '2' in selection.lower():
        print('PVP MODE SELECTED')
        time.sleep(2)
        return False
  
      elif 'c' in selection.lower() or '1' in selection.lower():
        print('AI MODE SELECTED')
        time.sleep(2)
        return True

      else:
        print('invalid option')
        continue

  def play(self, ai):
    turnsx = 1
    index = 0
    letter = 'x'
    hh = False
    hl = False
    hr = False
    vh = False
    vb = False
    vt = False
    dtl = False
    dtr = False
    dbl = False
    dbr = False
    dhr = False
    dhl = False
    all = [hh, hl, hr, vh, vb, vt, dtl, dtr, dbl, dbr, dhr, dhl]
    while True:
      if turnsx == 10:
        os.system('clear')
        print('Tie')
        time.sleep(5)
      os.system('clear')

      if ai:
        mode = 'Against AI Mode'

      if not ai:
        if (index % 2) == 0:
          letter = 'x'
          mode = 'PVP Mode'

        else:
          letter = 'o'

      index+=1
        
      self.render()
      tile = input(f'\n\n> {mode} > You are {letter} >, choose a square > ')
      tile = int(tile)


      if tile < 4 and tile != 4:
        if row1[int(tile - 1)] in ('x', 'o'):
          print('Already selected')
          time.sleep(2)
          index-=1
          continue

        self.row1[int(tile - 1)] = letter

      elif (3 < tile < 7):
        if row2[int(tile - 4)] in ('x', 'o'):
          print('Already selected')
          time.sleep(2)
          index-=1
          continue
          
        self.row2[int(tile - 4)] = letter

      elif (6 < tile < 10):
        if row3[int(tile - 7)] in ('x', 'o'):
          print('Already selected')
          time.sleep(2)
          index-=1
          continue
          
        self.row3[int(tile - 7)] = letter

      else:
        index-=1
        print('incorrect value')
        time.sleep(2)
        continue

      if self.win(letter) == True:
        os.system('clear')
        self.render()
        print(f'\n{letter} has won')
        time.sleep(2)
        return

      if ai:
        if self.win('o') == True:
          os.system('clear')
          self.render()
          print(f'\n{letter} has won')
          time.sleep(2)
          return
      turnsx+=1

      if ai:
        self.CPU(all)

  def win(self, letter):
    self.r1 = self.row1
    self.r2 = self.row2
    self.r3 = self.row3
    # Horizontal Check
    if self.r1[0] == letter and self.r1[1] == letter and self.r1[2] == letter:
      return True

    if self.r2[0] == letter and self.r2[1] == letter and self.r2[2] == letter:
      return True

    if self.r3[0] == letter and self.r3[1] == letter and self.r3[2] == letter:
      return True

    # Vertical Check
    if self.r1[0] == letter and self.r2[0] == letter and self.r3[0] == letter:
      return True

    if self.r1[1] == letter and self.r2[1] == letter and self.r3[1] == letter:
      return True

    if self.r1[2] == letter and self.r2[2] == letter and self.r3[2] == letter:
      return True


    # Diagonal Check

    if self.r1[0] == letter and self.r2[1] == letter and self.r3[2] == letter:
      return True

    if self.r1[2] == letter and self.r2[1] == letter and self.r3[0] == letter:
      return True


  def CPU(self, all):
    cordPlace = [0, 0]
    prob = 0.0
    ''' Attack Check '''
    ''' Horizontals  '''
    for row in self.board:
      rowcord = int(self.board.index(row)) + 1
      # Hidden Horizontal
      if not all[0]:
        if row[0] == 'o' and row[2] == 'o':
          if prob < 0.45:
            cordPlace = [rowcord, 1]
            prob = 0.49 # High priority horizontal
            all[0] = True
            break

      # Horizontal Left
      if all[1] == False:
        if row[0] == 'o' and row[1] == 'o':
          if row[2] == 'x' or row[2] == 'o':
            pass
          else:
            if prob < 0.46:
              cordPlace = [rowcord, 2]
              prob = 0.46 
              all[1] = True
              break

      # Horizontal right
      if all[2]== False:
        if row[1] == 'o' and row[2] == 'o':
          if row[0] == 'x' or row[0] == 'o':
            pass
          else:
            if prob < 0.45:
              cordPlace = [rowcord, 0]
              prob = 0.45
              all[2] = True
              break

    ''' Verticals '''
    for index in range(0, 3):
      if all[3] == False:
        # Hidden Vertical
        if row1[index] == 'o' and row3[index] == 'o':
          if row2[index] == 'x' or row2[index] == 'o':
            pass
          else:
            if prob < 0.5:
              cordPlace = [2, index]
              prob = 0.55 # High priority vertical
              all[3] = True
              break

      # Vertical Top
      if all[5] == False:
        if row1[index] == 'o' and row2[index] == 'o':
          if row3[index] == 'x' or row3[index] == 'o':
            pass
          else:
            if prob < 0.5:
              cordPlace = [3, index]
              prob = 0.5
              all[5] = True
              break

      # Vertical Bottom
      if all[4] == False:
        if row3[index] == 'o' and row2[index] == 'o':
          if row1[index] == 'x' or row1[index] == 'o':
            pass
          else:
            if prob < 0.53:
              cordPlace = [1, index]
              prob = 0.53
              all[4] = True
              break

    ''' Diagonals '''
    # Hidden Diagonal Left
    if all[11] == False:
      if row1[0] == 'o' and row3[2] == 'o':
        if row2[1] == 'x' or row2[1] == 'o':
            pass
        else:
          if prob < 0.63:
              cordPlace = [2, 1]
              prob = 0.63 # High Priority
              all[11] = True

    # Hidden Diagonal Right
    if all[10] == False:
      if row1[2] == 'o' and row3[0] == 'o':
        if row2[1] == 'x' or row2[1] == 'o':
            pass
        else:
          if prob < 0.61:
              cordPlace = [2, 1]
              prob = 0.61
              all[10] = True

    # Diagonal Left - Top
    if all[6] == False:
      if row1[0] == 'o' and row2[1] == 'o':
        if row3[2] == 'x' or row3[2] == 'o':
            pass
        else:
          if prob < 0.59:
              cordPlace = [3, 2]
              prob = 0.59 
              all[6] = True

    # Diagonal Left - Bottom
    if all[8] == False:
      if row3[2] == 'o' and row2[1] == 'o':
        if row1[0] == 'x' or row1[0] == 'o':
            pass
        else:
            if prob < 0.57:
                cordPlace = [1, 0]
                prob = 0.57 
                all[8] = True

    # Diagonal Right - Bottom
    if all[9] == False:
      if row3[0] == 'o' and row2[1] == 'o':
        if row1[2] == 'x' or row1[2] == 'o':
            pass
        else:
          if prob < 0.58:
              cordPlace = [1, 2]
              prob = 0.58
              all[9] = True

    # Diagonal Right - Top
    if all[7] == False:
      if row1[2] == 'o' and row2[1] == 'o':
        if row[0] == 'x' or row3[0] == 'o':
            pass
        else:
          if prob < 0.56:
              cordPlace = [3, 0]
              prob = 0.56
              all[7] = True
      
    ''' Defence '''
    ''' Horizontal '''
    for row in self.board:
      rowcord = int(self.board.index(row)) + 1
      # Hidden Horizontal
      if row[0] == 'x' and row[2] == 'x':
        if row[1] == 'x' or row[1] == 'o':
            pass
        else:
          if prob < 0.25:
            cordPlace = [rowcord, 1]
            prob = 0.25 # High priority horizontal
            break

      # Horizontal Left
      if row[0] == 'x' and row[1] == 'x':
        if row[2] == 'x' or row[2] == 'o':
            pass
        else:
          if prob < 0.24:
            cordPlace = [rowcord, 2]
            prob = 0.24 
            break

      # Horizontal right
      if row[1] == 'x' and row[2] == 'x':
        if row[0] == 'x' or row[0] == 'o':
            pass
        else:
          if prob < 0.23:
            cordPlace = [rowcord, 0]
            prob = 0.23
            break

    ''' Verticals '''
    for index in range(0, 3):
      # Hidden Vertical
      if row1[index] == 'x' and row3[index] == 'x':
        if row2[index] == 'x' or row2[index] == 'o':
            pass
        else:
          if prob < 0.35:
            cordPlace = [2, index]
            prob = 0.35 # High priority vertical
            break

      # Vertical Top
      if row1[index] == 'x' and row2[index] == 'x':
        if row3[index] == 'x' or row3[index] == 'o':
            pass
        else:
          if prob < 0.34:
            cordPlace = [3, index]
            prob = 0.34
            break

      # Vertical Bottom
      if row3[index] == 'x' and row2[index] == 'x':
        if row1[index] == 'x' or row1[index] == 'o':
            pass
        else:
          if prob < 0.33:
            cordPlace = [1, index]
            prob = 0.33
            break

    ''' Diagonals '''
    # Hidden Diagonal Left
    if row1[0] == 'x' and row3[2] == 'x':
      if row2[1] == 'x' or row2[1] == 'o':
          pass
      else:
        if prob < 0.44:
          cordPlace = [2, 1]
          prob = 0.44 # High Priority

    # Hidden Diagonal Right
    if row1[2] == 'x' and row3[0] == 'x':
      if row2[1] == 'x' or row2[1] == 'o':
            pass
      else:
        if prob < 0.43:
            cordPlace = [2, 1]
            prob = 0.43

    # Diagonal Left - Top
    if row1[0] == 'x' and row2[1] == 'x':
      if row3[2] == 'x' or row3[2] == 'o':
            pass
      else:
        if prob < 0.42:
            cordPlace = [3, 2]
            prob = 0.42 

    # Diagonal Left - Bottom
    if row3[2] == 'x' and row2[1] == 'x':
      if row1[0] == 'x' or row1[0] == 'o':
            pass
      else:
        if prob < 0.41:
            cordPlace = [1, 0]
            prob = 0.41

    # Diagonal Right - Bottom
    if row3[0] == 'x' and row2[1] == 'x':
      if row1[2] == 'x' or row1[2] == 'o':
            pass
      else:
        if prob < 0.40:
            cordPlace = [1, 2]
            prob = 0.40

    # Diagonal Right - Top
    if row1[2] == 'x' and row2[1] == 'x':
      if row1[0] == 'x' or row1[0] == 'o':
            pass
      else:
        if prob < 0.409:
            cordPlace = [3, 0]
            prob = 0.409

    print(prob)
    print(cordPlace)
    time.sleep(2)

    if cordPlace[0] != 0:
      if int(cordPlace[0]) == 1:
        if row1[cordPlace[1]] == 'x' or row1[cordPlace[1]] == 'o':
          cordPlace = 0
        else:
          row1[cordPlace[1]] = 'o'
          return

      if int(cordPlace[0]) == 2:
        if row2[cordPlace[1]] == 'x' or row2[cordPlace[1]] == 'o':
          cordPlace = 0
        else:
          row2[cordPlace[1]] = 'o'
          return

      if int(cordPlace[0]) == 3:
        if row3[cordPlace[1]] == 'x' or row3[cordPlace[1]] == 'o':
          cordPlace = 0
        else:
          row3[cordPlace[1]] = 'o'
          return
    
    if cordPlace[0] == 0:
      found = False
      while True:
        for row in self.board:
          index = random.randint(0,2)
          if row[index] != 'x' and row[index] != 'o':
            row[index] = 'o'
            found = True
            break
            
          else:
            continue

        if found:
          break

      return
      

    
# Exec #

def run(board):
  game = Game(board)
  ai = game.menu()
  game.play(ai)

if __name__ == '__main__':
  run(board)
