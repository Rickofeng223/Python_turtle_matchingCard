'''
Jie Feng
CS5001,Fall 2020
Project

'''
import turtle
from card_menu import * 
import time
import random

t=turtle.Turtle()

#WE MAKE A NEW TURTLE FOR WRITING THE STATUS SO THAT WE CAN USE TURTLE.CLEAR() WITH EASE
wpen=turtle.Turtle()
wpen.penup()
wpen.speed(-1)
#PEN TO DRAW BLANKS
pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(-1)

ts=turtle.Screen()


class player_stats:
    def __init__(self):
        self.matches=0
        self.guesses=0
        self.name=None
        self.leaderboard=[]
        self.num_cards=None
        
player=player_stats()

def drawing_menu():
    player.name=ts.textinput("CS5001 Memory", "Your Name:")
    #print(name)
    
    number_cards = int(ts.numinput("Set Up","# of Cards to Play: (8,10 or 12)",default=12, minval=8, maxval=12))
    player.num_cards=number_cards
    if number_cards == 9 or number_cards ==11:  #if number card equal to 9, or 11
        ttt=turtle.Turtle()
        tss=turtle.Screen()
        tss.addshape("card_warning.gif")
        ttt.shape("card_warning.gif")
        time.sleep(3)
        ttt.hideturtle()
        # 9-1 =9 go to this function
        if number_cards-1==8:
            player.num_cards=number_cards-1
            return mix_card(number_cards-1)#mix_card_8()
        # 11-1=10 go to this function
        elif number_cards-1==10:
            player.num_cards=number_cards-1
            return mix_card(number_cards-1)#mix_card_10()       
    # if user put in 8,10,12
    else:
        return mix_card(number_cards)
             
def draw_square(x, y):
    t.penup()
    t.goto(x,y)
    t.pensize(10)
    t.speed(13)          #drawing speed
    t.penup()
    t.forward(300)
    t.down()
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(850)
    t.left(90)
    t.forward(600)
    t.left(90)
    t.forward(850)
    t.left(90)
    t.forward(400)
    t.penup()
    t.home()
    
def blank_card(x,y):
    
    pen.color('white')
    pen.setpos(x-50,y+75)
    pen.begin_fill()
    for i in range(0,2):
        pen.fd(100)
        pen.right(90)
        pen.fd(150)
        pen.right(90)
    pen.end_fill()
    pen.setpos(x,y)
    
def draw_bottom_menu(x,y):
    t.goto(x,y)
    t.pensize(10)
    t.forward(100)
    t.down()
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(850)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(850)
    t.penup()#up()
    #t.home()
    wpen.setpos(-580,-340)
    wpen.hideturtle()
    wpen.write("Status: Guesses:"+str(player.guesses)+"Matches:"+str(player.matches), font=("Arial", 23, "normal"))
    
def right_menu(x,y):
    t.goto(x,y)
    t.pensize(10)
    t.pencolor("blue")
    t.forward(100)
    t.down()
    t.left(90)
    t.forward(600)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.forward(600)
    t.left(90)
    t.forward(250)
    t.penup()
    t.goto(480,330)

    #Use a 'try' to mitigate an error if no leaderboard.txt exists
    try:
        f = open('leaderboard.txt', 'r')
    except:
        t.setpos(0,0)
        ts.addshape('leaderboard_error.gif')
        t.shape('leaderboard_error.gif')
        ts.update()
        time.sleep(1)
        f = open('leaderboard.txt', 'w')
        f.close()
        f = open('leaderboard.txt', 'r')   
    t.color('blue')
    t.goto(480,330)
    t.write("Leader:", move=True, align="right", font=("Arial", 23, "normal"))
    t.goto(490,280)
        #Add the contents of the file to list
    for i in range(0,6):
        player.leaderboard.append(f.readline().replace('\n',''))
        t.goto(490,230-(i*50))
        t.write(player.leaderboard[i], move=True, align="right", font=("Arial", 20, "normal"))

        #Turn the number from string to integer so we can sort the list later
    for j in range(0,6):
        try:
            player.leaderboard[j]=player.leaderboard[j].split(':')
            player.leaderboard[j][1]=int(player.leaderboard[j][1])
        except:
            pass
            
        #If there is an empty [''] then remove it so there is no error while sorting
    for k in range(0,6):
        try:
            player.leaderboard.remove([''])
        except:
            pass
    f.close()
    #IF THE LEADERBOARD TEXT FILE IS NOT FOUND
        
def add_to_leaderboard():
    player.leaderboard.append([player.name,player.guesses])
    player.leaderboard.sort(key=lambda x: x[1])
    if len(player.leaderboard)>6:
        player.leaderboard.pop(-1)
    f = open('leaderboard.txt', 'w')
    for i in range(0,len(player.leaderboard)):
        f.write(player.leaderboard[i][0]+":"+str(player.leaderboard[i][1])+'\n')
    f.close()
    
def quit_button(x,y):
    qt=turtle.Turtle()
    qs=turtle.Screen()
    qt.penup()
    qt.goto(x,y)
    qs.addshape("quitbutton.gif")
    qt.shape("quitbutton.gif")
   
cardlis=[ ]
def click(x,y):
    
    if abs(x-450)<=15 and abs(y-(-300))<=10:
        t1=turtle.Turtle()
        ts1=turtle.Screen()
        ts1.addshape("quitmsg.gif")
        t1.shape("quitmsg.gif")
        time.sleep(3)
        ts.bye()
    
    else:
        for card in cardlis:
            #ADDED "and card.face_upp==0" INSIDE IF STATEMENT, IF THE CARD IS ALREADY FACEUP, CLICK DOESN'T REGISTER
            if card.check_in_region(x,y) and card.face_upp==0:
                place_card(card.x,card.y,card.card_flip())
                check_for_match(card)       #call function from line 13

   
                              
face_up_lis=[ ]
def check_for_match(card):
    if len(face_up_lis)==0:
        face_up_lis.append(card)
        print("1st choice: " + face_up_lis[0].face_up())
    else:
                
        print("2nd choice: " + face_up_lis[0].face_up())
        if face_up_lis [0] == card:
            #t.hideturtle()
            print("they equal")
            player.matches+=1
            player.guesses+=1
            #IF THE CARDS MATCH, WE ADD THE IMAGE OF A BLANK CARD TO GIVE THE ILLUSION THAT ITS BEEN REMOVED
            place_card(card.x,card.y,card.card_flip())
            time.sleep(1)
            turtle.tracer(0)
            blank_card(face_up_lis[0].x,face_up_lis[0].y)
            blank_card(card.x,card.y)
            turtle.tracer(1)
            #t.clearstamp(face_up_lis)
        else:
            #flipping back
            place_card(face_up_lis[0].x,face_up_lis[0].y,face_up_lis[0].card_flip())
            time.sleep(1)
            place_card(card.x,card.y,card.card_flip())
            
            print("not equal, clearing list")
            player.guesses+=1
        #WRITE THE NEW STATUS
        wpen.clear()
        wpen.write("Status: Guesses:"+str(player.guesses)+"Matches:"+str(player.matches), font=("Arial", 23, "normal"))
        face_up_lis.clear()
        if player.matches==player.num_cards/2:
            add_to_leaderboard()
            t.setpos(0,0)
            ts.addshape('winner.gif')
            t.shape('winner.gif')
            t.stamp()
            ts.update()
            time.sleep(3)
            ts.bye()
        
    for acard in face_up_lis:
        print(acard.face_up())
                    

def place_card(x,y,card):         
    t.shape(card)
    t.penup()#up()
    t.goto(x,y)
    id_=t.stamp()
        

def placing_cards(front_cards_list):           
    ts.addshape('card_blank.gif')
    for each in front_cards_list:
        ts.addshape(each.face_down())
        ts.addshape(each.face_up())
    
    for each in front_cards_list:
        place_card(each.x, each.y, each.face_down())   
    
def mix_card(number_cards):          # numbers of shuffle cards return
    front_image = ["2_of_clubs.gif","ace_of_diamonds.gif","3_of_hearts.gif",
                   "queen_of_hearts.gif","jack_of_spades.gif",
                   "king_of_diamonds.gif"]
    place=[(-540,280),(-360,280),(-180,280),(0,280),(-540,90),(-360,90),(-180,90),(0,90),(-540,-100)
           ,(-360,-100),(-180,-100),(0,-100)]

    front_image_list = []
    for each in range(number_cards//2):
        front_image_list.append(front_image[each])
        front_image_list.append(front_image[each])
    random.shuffle(front_image_list)
    
    for each in range(0,number_cards):
        cardlis.append(Cards(front_image_list[each],"card_back.gif",place[each][0],place[each][1]))
    
    return cardlis
    
def main():

    front_cards_list=drawing_menu()         # return whatever user enter the # of cards-> mix_card#
    draw_square(-80,20)
    draw_bottom_menu(120,-360)
    right_menu(500,-230)
    quit_button(450,-300)  #place the quit button gif
    placing_cards(front_cards_list)          #call the placing_card on each (mix_card#)
    ts.onscreenclick(click)    # catch the click use it to quit the game
    turtle.done()

main()

