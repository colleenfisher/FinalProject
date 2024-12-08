# FinalProject
To run this code, I right click and select "Run Python" and then I selected "Run Python in Terminal"
Once the game launches, a start menu will appear. The player will type "1" for easy, "2" for medium, or "3" for hard depending on their desired game mode. 
If the player selects the easy mode, the memory matching game will run with no timer. The player is free to play for as long as they need to complete all of the matches. When this level is over the player will either type "R" to replay the game or "Q" to quit the game. 
If the player selects the medium mode, the memory matching game will run with a timer that counts down from 250 seconds. If the player completes the game in that time constraint, a "You Win" message will appear with the option to either type "R" to replay the game or "Q" to quit the game. If the player does not complete the game in that time constraint, a "Game Over" message will appear with the option to either type "R" to replay the game or "Q" to quit the game. 
If the player selects the hard mode, the memory matching game will run with a timer that counts down from 250 seconds, however with each wrong matching pair the timer will decrease by one second. If the player completes the game in that time constraint, a "You Win" message will appear with the option to either type "R" to replay the game or "Q" to quit the game. If the player does not complete the game in that time constraint, a "Game Over" message will appear with the option to either type "R" to replay the game or "Q" to quit the game. 
On each level a negative sound will play with each wrong matching pair. A positive sound will play with each correct matching pair. 

Test Suite
I included several tests to make sure different parts of the memory game are working correctly. 
The test_create_cards() test checks that the game creates the right number of cards (50 in total) and that each card symbol shows up twice, as it should. 
The test_check_for_match() test makes sure the game correctly identifies matching cards, returning True when they match and False when they don’t. 
The test_game_completed() test checks that the game knows when all the cards have been matched and the game is over.
The test_invalid_mouse_click() test makes sure that if the player clicks outside the cards, nothing happens, so the game only reacts to valid card clicks. 
All of these tests came back and passed, which helped me to ensure that my game ran correctly. 
