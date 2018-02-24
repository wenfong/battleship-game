import random

class BattleshipGame:
    def __init__(self):
        self.__userBoard=[]
        self.__computerBoard=[]
        for i in range(10):
            self.__userBoard.append([])
            self.__computerBoard.append([])
            for j in range(10):
                self.__userBoard[i].append(' ')
                self.__computerBoard[i].append(' ')    
        self.__rounds=0
        self.__computerShips={'A':5,'B':4,'S':3,'D':3,'P':2}
        self.__userShips={'A':5,'B':4,'S':3,'D':3,'P':2}
        
#-------------------------------------------------------------------------------
    def drawBoards(self,hide):
        yaxis=['A','B','C','D','E','F','G','H','I','J']
        
        ships={'A':'Aircraft Carrier  ','B':'Battleship        ','D':'Destroyer         ','P':'Patrol Boat       ','S':'Submarine         '}
        computerships=[]
        userships=[]
        for i in self.getEnemyFleet(True)[1]:
            userships.append(ships[i])
        for i in self.getEnemyFleet(False)[1]:
            computerships.append(ships[i])
        computerData=[str(self.getHits(True))+' '*16,str(self.getMisses(True))+' '*16,'0'+str(len(self.getEnemyFleet(True)[1]))+' '*16]+userships+([' '*18]*(7-len(userships)))
        userData=[str(self.getHits(False))+' '*16,str(self.getMisses(False))+' '*16,'0'+str(len(self.getEnemyFleet(False)[1]))+' '*16]+computerships+([' ']*(7-len(computerships)))
        data=['Nbr. of hits  :','Nbr. of misses:','Ships sunk    :',' '*15,' '*15,' '*15,' '*15,' '*15,' '*15,' '*15]  
        
        print("   Computer's board:         User's board:          at round:", self.__rounds)
        print('   1 2 3 4 5 6 7 8 9 10      1 2 3 4 5 6 7 8 9 10'+' '*18+'Computer Status:  User Status:')    
        for i in range(10):
            print(yaxis[i]+' |', end='')
            for j in range(10):
                if not hide or self.__computerBoard[i][j] in '#*':
                    print(self.__computerBoard[i][j]+'|', end='')
                else:
                    print(' |', end='')
            print('   '+yaxis[i]+' |', end='')
            for j in range(10):
                print(self.__userBoard[i][j]+'|',end='')
            print(end='  ')
            print(data[i], end=' ')
            print(computerData[i], end='')
            print(userData[i], end='')
            print('')
                
#-------------------------------------------------------------------------------    
    def validatePlacement(self,computer,ship,size,x,y,orientation):
        if computer:
            board=self.__computerBoard
        else:
            board=self.__userBoard
        if board[y][x]==' ':
            for i in range(size):
                if orientation=='h':
                    if (x+i) not in range(10) or board[y][x+i]!=' ':
                        return False
                else:
                    if (y+i) not in range(10) or board[y+i][x]!=' ':
                        return False
            if i==size-1:
                for i in range(size):
                    if orientation=='h':
                        board[y][x+i]=ship
                    else:
                        board[y+i][x]=ship
                return True
        else:
            return False
        
#-------------------------------------------------------------------------------
    def getEnemyFleet(self,computer):
        ships=[]
        sunk=[]
        if computer:
            for k,v in self.__userShips.items():
                if v!=0:
                    ships.append(k)
                else:
                    sunk.append(k)
        else:
            for k,v in self.__computerShips.items():
                if v!=0:
                    ships.append(k)
                else:
                    sunk.append(k)
        return [ships,sunk]
    
#-------------------------------------------------------------------------------
    def checkWinning(self,computer):
        if computer:
            for v in self.__userShips.values():
                if v!=0:
                    return False
            return True
        else:
            for v in self.__computerShips.values():
                if v!=0:
                    return False
            return True
        
#-------------------------------------------------------------------------------            
    def makeA_Move(self,computer,x,y):
        if computer:
            board=self.__userBoard
            ships=self.__userShips
        else:
            board=self.__computerBoard
            ships=self.__computerShips
        if board[y][x] in 'ABDPS':
            ship=board[y][x]
            ships[board[y][x]]-=1
            board[y][x]='#'
            return ship
        elif board[y][x]==' ':
            board[y][x]='*'
            return ' '
        else:
            return board[y][x]
        
#-------------------------------------------------------------------------------        
    def checkIfSunk(self,computer,ship):
        if computer:
            if self.__userShips[ship]==0:
                return True
            else:
                return False
        else:
            if self.__computerShips[ship]==0:
                return True
            else:
                return False
            
# ---------------------------------------------------------------------------
    def incrementRounds(self):
        self.__rounds+=1
        
# ---------------------------------------------------------------------------
    def getHits(self,computer):
        if computer:
            board=self.__userBoard
        else:
            board=self.__computerBoard
        hits=0
        for i in range(10):
            for j in range(10):
                if board[i][j]=='#':
                    hits+=1
        if hits<10:
            hits='0'+str(hits)
        return hits

# ---------------------------------------------------------------------------
    def getMisses(self,computer):    
        if computer:
            board=self.__userBoard
        else:
            board=self.__computerBoard
        misses=0
        for i in range(10):
            for j in range(10):
                if board[i][j]=='*':
                    misses+=1
        if misses<10:
            misses='0'+str(misses)
        return misses

class Stack:    
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        
    def pop(self):
        return self.__items.pop()
    
    def peek(self):
        return self.__items[len(self.__items)-1]
    
    def is_empty(self):
        return len(self.__items) == 0
    
    def size(self):
        return len(self.__items)
    
# ---------------------------------------------------------------------------------                                
# The main program
# ---------------------------------------------------------------------------------                                

a=BattleshipGame()
b=Stack()
key=['A','B','C','D','E','F','G','H','I','J']
shipsize={'A':5,'B':4,'S':3,'D':3,'P':2}
ships={'A':'Aircraft Carrier','B':'Battleship','D':'Destroyer','P':'Patrol Boat','S':'Submarine'}
for ship,size in shipsize.items():
    a.drawBoards(True)
    print('Placing a '+ships[ship]+' of size '+str(size))
    #computer places ship
    while not a.validatePlacement(True,ship,size,random.randint(0,9),random.randint(0,9),random.choice(['h','v'])):
        continue   
    
#user places ship
    valid=False
    while not valid:
        userinput=input('Enter coordinates x y (x in [A...J] and y in [1..10]):')
        try:
            y,x=userinput.split(' ')
            x=int(x)-1
            y=key.index(y.upper())            
            if y in range(10) and x in range(10):
                orientation=' '
                while orientation not in 'hv':
                    orientation=input('This ship is vertical or horizontal (v,h)?')
                if a.validatePlacement(False,ship,size,x,y,orientation):
                    valid=True
                else:
                    print('Cannot place a '+ships[ship]+' there. Stern is out of the board or collides with other ship.')
                    print('Please take a look at the board and try again.')
                    input('Hit ENTER to continue')
        except:
            valid=False
a.drawBoards(True)
input('Done placeing user ships. Hit ENTER to continue') 
    
    
endgame=False
playerturn=True 
computerhits=0
while not endgame:
    #player's turn
    if playerturn:
        a.incrementRounds()
        valid=False
        a.drawBoards(True)
        while not valid:
            try:
                usermove=input('Enter coordinates x y (x in [A..J] and y in [1..10]):')
                (y,x)=usermove.split(' ')  
                x=int(x)-1
                y=key.index(y.upper())
                if y in range(10) and x in range(10):
                    move=a.makeA_Move(False,x,y)
                    if move in 'ABDPS':
                        print('Hit at',usermove)
                        valid=True
                        if a.checkIfSunk(False,move):
                            print(ships[move], 'sunk')
                            if a.checkWinning(False):
                                print('Congratulations! User WON!')
                                endgame=True
                    elif move==' ':
                        print('Sorry,',usermove, 'is a miss')
                        valid=True
                    else:
                        print('Sorry,',usermove, 'was already played. Try again.')
            except:
                valid=False
                
            armada=a.getEnemyFleet(False)
            print ("Ships to sink:[", end="")
            for ship in armada[0]:
                print (ships[ship], " ", end="")
            print ("]  Ships sunk:[",end="")
            for ship in armada[1]:
                print (ships[ship], " ", end="")
            print("]")            
                
        playerturn=False  
    
    #computer's turn    
    else:
        if b.is_empty():
            move='#'
            x=0
            y=0
            while move in '#*':
                if not y>9:
                    #finding the smallest ship and its size
                    jumps=5
                    for i in a.getEnemyFleet(True)[0]:
                        if shipsize[i]<=jumps:
                            jumps=shipsize[i]
                    x=x+jumps
                    if x>9:
                        x=x-9
                        y+=1   
                else:
                    x+=1
                    if x>9:
                        y+=1
                move=a.makeA_Move(True,x,y)
        else:
            x,y=b.pop()
            y=int(y)
            move=a.makeA_Move(True,x,y)
            while move in '#*' and not b.is_empty():
                x,y=b.pop()
                y=int(y)
                move=a.makeA_Move(True,x,y)
                
        if move in 'ABDPS':
            if y==9 and x==9:
                b.push((x-1,y))
                b.push((x,y-1))
            elif y==9 and x==0:
                b.push((x,y-1))
                b.push((x+1,y)) 
            elif y==0 and x==0:
                b.push((x,y+1))
                b.push((x+1,y))
            elif y==0 and x==9:
                b.push((x-1,y))
                b.push((x,y+1))
            elif y==0:
                b.push((x-1,y))
                b.push((x,y+1))
                b.push((x+1,y))
            elif y==9:
                b.push((x-1,y))
                b.push((x,y-1))
                b.push((x+1,y))
            elif x==0:
                b.push((x,y+1))
                b.push((x,y-1))
                b.push((x+1,y))  
            elif x==9:
                b.push((x,y+1))
                b.push((x-1,y))
                b.push((x,y-1))  
            else:
                b.push((x,y+1))
                b.push((x-1,y))
                b.push((x,y-1))
                b.push((x+1,y))
            
            computerhits+=1    
            print('Computer did a Hit at', key[y], x+1)
            if a.checkIfSunk(True,move):
                #empty the stack if the ship is sunk
                if computerhits==shipsize[move]:
                    while not b.is_empty():
                        b.pop()
                    computerhits=0
                print(ships[move], 'sunk')
                if a.checkWinning(True):
                    print ("Sorry! Computer WON! Here is what the board looked like:")
                    # display boards without hiding the computer ships
                    a.drawBoards(False)
                    input("Press ENTER to continue")
                    endgame=True
        else:
            print('Computer missed at', y, x+1)    
        playerturn=True
