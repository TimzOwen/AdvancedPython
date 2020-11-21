# import modules needed for the program to run
import random

# Deck of Cards in python
print("Welcome to the world of Cards")

class Cards(object):
    #declare a method to take in th suit and value of the cards
    def __init__(self, card_suit, card_val):
        self.card_suit = card_suit
        self.card_val = card_val
    def displayCards(self):
        #print value and the suit
        print("{} of {} ".format(self.card_val, self.card_suit))
class Deck(object):
    def __init__(self):
        # instantiate 2 methods to build the deck and add them in an array
        self.cards = []
        self.buildDeck()
    def buildDeck(self):
        # loop through all the cards
        for suits in ["Clubs","Spades","Diamond","Hearts"]:
            #use the range to add with values
            for values in range(1,14):
                # Add up the cards to the List cards using append
                self.cards.append(Cards(suits, values))
    # create a method to display to the user the cards
    def showCards(self):
        for c in self.cards:
            c.displayCards()
    # create a method to shuffle the entire deck (import Random from python)
    def shuffleDeck(self):
        # shuffle with -1 and in reverse to index 0
        for x in range(len(self.cards)-1,0,-1):
            # use randint - random number generator to select cards
            # the range is form L--->R
            rand_card_no = random.randint(0,x)
            #sap the cards
            self.cards[x],self.cards[rand_card_no] = self.cards[rand_card_no],self.cards[x]
    # create a method to and return the pop() as end card indication
    def retrieveCard(self):
        return self.cards.pop()
#Now create a player to start playing and make sure to access the deck and add the cards to the players "pocket"
class GamePlayer(object):
    # create an emplty list to start from and retreive the cards from the deck addign to the player
    def __init__(self,playerName):
        self.playerName = playerName
        self.pocket = []
    # create a method to add the cards to the pocket from the deck
    def retreive(self, deck):
        self.pocket.append(deck.retrieveCard())
        return self
    # check player's card
    def checkPocket(self):
        for playerCards in self.pocket:
            playerCards.displayCards()
    # method to discard cards like joker if retrieved
    def discardJokers(self):
        # return a pop method to remove them because its stated that its not in the deck
        return self.pocket.pop()
# cards = Cards("Clubs",6)
# print(cards.display())
deck = Deck()
deck.shuffleDeck()

# owen = GamePlayer("OWen")
# owen.retreive(deck).retreive(deck)
# print(owen.checkPocket())

# card = deck.retrieveCard()
# print(card.displayCards())



# CHECKING CODE FROM ASSIGNMENTS GIVEN
# Cross check quiz 1
card = Cards(5, 1)
# prints "5 of clubs"
print(card)

# cross check quiz 2
card = Cards(12, 4)
# prints "Queen of hearts"
print(card)

# cross check quiz 3
deck = Deck()
# Add the 52 standard cards to the new deck
deck.add_standard_cards()

# cross check quiz 4
# Reorder the cards in the deck randomly.
#  The shuffle method makes use of the randint function
deck.shuffle()

# cross check quiz 5
# Create a new tiny Deck of cards called hand, made up
#   of the last five cards in deck.  The deal method should
#   also remove those last five cards from "deck".
hand = deck.deal(5)

# print the cards in the hand
for card in hand.card_list:
    print(card)

print("----")

# cross check quiz 6
# print the remaining cards in the deck
for card in deck.card_list:
    print(card)















import math
from bigfloat import *
import matplotlib.pyplot as plt
from visual import *

# A class to handle the time ranges
class timeHoursSeconds(object):
    def __init__(self,s,h,d,y):
        self.s = s
        self.h = h
        self.d = d
        self.y = y
    def fromStoHours(self):
        h = self.s/60/60
        return h
    def fromStoDays(self):
        d = self.s/60/60/24
        return d
    def fromStoYears(self):
        y = self.s/60/60/24/365
        return y
    def fromDaysToS(self):
        s = self.d*24*60*60
        return s
    def fromDaysToH(self):
        h = self.d * 24
        return h
    def fromDaysToY(self):
        y = self.d/365
        return y



class planet(object):
    G = 6.67 * math.pow(10,-11)
    sunM = 1.989 * math.pow(10,30)
    eaM = 5.973 * math.pow(10,24)
    RTL = 384400000
    def __init__(self,name,mass,RS,theta0,radius):
        self.name = name
        self.mass = mass
        self.RS = RS
        self.theta0 = theta0
        self.radius = radius
    def gravitationalForce(self,m2=1):
        if m2 ==1:
            f = self.G * (self.mass*self.sunM)/math.pow(self.RS,2)
        else:
            f = self.G * (self.mass*self.eaM)/math.pow(self.RTL,2)
        return f
    def angularVelocity(self,m2=1):
        w = math.sqrt(self.gravitationalForce(m2=m2)/(self.mass*self.RS))
        return w
    def velocity(self,m2=1):
        v = self.angularVelocity(m2=1) * self.RS
        return v
    def angularPosition(self,t,m2=1):
        theta = self.theta0 + self.angularVelocity(m2=m2) * t
        return theta
    def varAngularPosition(self,t,dt,m2=1):
        dtheta = self.angularPosition(t+dt,m2=m2)-self.angularPosition(t,m2=m2)
        return dtheta
    def periodAroundSun(self,m2=1):
        p = timeHoursSeconds(2*math.pi/self.angularVelocity(m2=m2),0,0,0)
        return p
    def picture(self,x,y,z,col,trail):
        if col == 1:
            return sphere(pos=vector(x,y,z),color=color.red,radius=self.radius,make_trail=trail)
        elif col == 2:
            return sphere(pos=vector(x,y,z),color=color.blue,radius=self.radius,make_trail=trail)
        elif col == 3:
            return sphere(pos=vector(x,y,z),color=color.green,radius=self.radius,make_trail=trail)
        elif col == 4:
            return sphere(pos=vector(x,y,z),color=color.cyan,radius=self.radius,make_trail=trail)
        elif col == 5:
            return sphere(pos=vector(x,y,z),color=color.yellow,radius=self.radius,make_trail=trail)
        else:
            return sphere(pos=vector(x,y,z),color=color.white,radius=self.radius,make_trail=trail)


mercury = planet("Mercury",3.302 * math.pow(10,23),57910000000,0,0.3)
venus = planet("Venus",4.8685 * math.pow(10,24),108200000000,0,0.4)

earth = planet("Earth",5.973 * math.pow(10,24),149600000000,0,0.5)
# As for the Moon, input Earth-Moon distance
moon = planet("Moon",7.347 * math.pow(10,22),384400000,0,0.2)

mars = planet("Mars",6.4185 * math.pow(10,23),227900000000,0,0.45)
jupiter = planet("Jupiter",1.8986 * math.pow(10,27),778500000000,0,.8)
saturn = planet("Saturn",5.6846 * math.pow(10,26),1433000000000,0,0.7)
uranus = planet("Uranus",8.6832 * math.pow(10,25),2877000000000,0,0.6)
neptune = planet("Neptune",1.0243 * math.pow(10,26),4503000000000,0,0.6)



# Simulation data
years = timeHoursSeconds(0,0,3655,0)
seconds = years.fromDaysToS()
print("Years: ",years.y)
print("Days: ",years.d)
print("Seconds: ",seconds)
t = 0
dt = timeHoursSeconds(10000,0,0,0)


# Planets
merc = mercury.picture(1.5,0,0,1,True)
ven = venus.picture(3,0,0,3,True)
ea = earth.picture(5,0,0,2,True)
mar = mars.picture(7,0,0,3,True)
jup = jupiter.picture(9,0,0,5,True)
sat = saturn.picture(11,0,0,6,True)
ur = uranus.picture(13,0,0,3,True)
nep = neptune.picture(15,0,0,2,True)
planetsf = [merc,ven,ea,mar,jup,sat,ur,nep]
planets = [mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
# The Moon
v = vector(0.9,0,0)
mo = moon.picture(5+0.9,0,0,10,True)

for k in planets:
    revp = k.periodAroundSun()
    print("Planet name: ",k.name)
    print(k.name," mass: ",k.mass," kg")
    print(k.name," distance from the sun: ",k.RS/1000," Km")
    print(k.name," angular velocity: ",k.angularVelocity()," rad/s")
    print(k.name," period around the sun: ",revp.fromStoYears()," terrestrial year/s")
    print("\n")
    

# Our program
while t < seconds:
    rate(50)
    for plan in range(len(planets)):
        planetsf[plan].pos = rotate(planetsf[plan].pos,angle=planets[plan].varAngularPosition(t,dt.s),axis=(0,0,1))
    v = rotate(v,angle=moon.varAngularPosition(t,dt.s,m2=2),axis=(0,0,1))
    mo.pos = ea.pos + v
    t += dt.s

    
    
    
    
    
    
    
    
    
    
    
    
    
    
# assignment 3 Sorting it all out

# checkpoint step one (The city class)

# define the city class and pass in the required arguemnts
class City:
    def __init__(self, country_Code,name,region,populations,latitude,longitude):
        self.country  = country
        self.name = name
        self.region = region
        self.populations =populations
        self.latitude = latitude
        self.longitude = longitude
    
