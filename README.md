# Python_turtle_matchingCard
matching card game with turtle
'''
Jie Feng
Project

'''


In this game we have used two different py files, one containing a class for a "card" and all related attributes and the other 
containing the rest of the program


card_menu : 
	~Constructor method: This method contains values for the name of the front and back of the card gif files, 
	its coordinates and whether it is face up or down
	~A face_down and face_up method to return the name of the faceup or facedown gif file
	~card_flip checks the current condition of the card (face up or down) and then returns the opposite
	~check_in_reigon checks if the user has clicked on the card or not
	~__eq__ checks if the two faceup cards are the same then returns the corresponding boolean

draw:
	~A class called player_stats which stores the players matches, guesses, name, leaderboard and the number of cards
	~drawing_menu function that takes input for name and number of cards, then returns a list of shuffled cards
	~draw_square is to draw the card board
	~blank_card is to draws a white rectangle to hide a card at position x,y
	~draw_bottom_menu draw the bottom menu
	~right_menu draws the right menu as well as opens the leaderboard.txt file
	~add_to_leaderboard adds the player to the leaderboard file
	~quit_button is to add the quitbutton.gif into the quit location
	~click checks to see if the player has clicked the quitbutton, or checks which card it has clicked
	~check_for_match is where it checks if two cards match, flips them and checks if the game is won
	~place_card puts the specified card at location x,y
	~placing_cards draws all the cards
	~mix_card shuffles and returns the list of cards
	~main contains the sequence of execution of the above methods

testing: 
	We had to make sure that all error messages and warnings displayed appropriately so we intentionally put in incorrect inputs to see if out 		program accounted for any error.We had to make sure that when users clicks were being detected , and it has to be inside the shape to 		make it run or do something.  I have our first error due to the problem when user wants to quit the game but board just quit right away 		without showing up the message saying " You Quit", so I found out that we can delay the message by using time.sleep(3) for 3 seconds to 		pop up message. We also found an error that clicking an already faceup card would crash the program, so we added code that only 		registered clicks if the card was already face down.We found an error that the program would not run if the leaderboard.txt was empty or 	did not already have 6 scores in it, thus we made it so that we deleted empty [""] arrays from the leaderboard array so that the program 	would not give an error while trying to sort it. We had to make sure that when player win, end the game and add the players name in 		to the leaderboard with their scores.
