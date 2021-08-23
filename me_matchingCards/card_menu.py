'''
Jie Feng
CS5001,Fall 2020
Project

'''

class Cards:

    def __init__(self,front,back,x,y):         
        self.front=front
        self.back=back
        self.x=x
        self.y=y
        self.face_upp=0
        
    def face_down(self):
        return self.back

    def face_up(self):
        return self.front
    def both_card(self):
        return (self.front,self.back)
    
    def card_flip(self):
        if self.face_upp ==0:
            self.face_upp=1
            return self.front
        else:
            self.face_upp=0
            return self.back
        
        #return Cards(self.back,self.front)


    def check_in_region(self,x,y):         # check if click inside the region
        if abs(x-self.x)<=50 and abs(y-self.y)<=75:
            return True

        else:
            return False 
   
    
    def __eq__(self,other):
        return self.front == other.front     # if the card front is equal, they both erase and tries+1
 





        





