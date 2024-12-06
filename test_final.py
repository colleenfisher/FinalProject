import unittest
from unittest.mock import patch
import pygame
from FINALPROJECT import SCREEN_WIDTH, create_cards, check_for_match, game_completed

class TestMemoryGame(unittest.TestCase):

    @patch('pygame.Rect')  # Mocking pygame.Rect to avoid rendering
    def test_create_cards(self, MockRect):
        """Test that the create_cards function creates the correct number of cards and shuffles them."""
        cards = create_cards()

        # Check that the correct number of cards is created
        self.assertEqual(len(cards), 5 * 10)  # 5 rows * 10 columns
        
        # Ensure each card value appears exactly twice
        card_values = [card['value'] for card in cards]
        for value in set(card_values):
            self.assertEqual(card_values.count(value), 2)

#['&', '$', '?', '!', '€', '»', '~', '*', '☺', ':', '#', '^', '{', '[', ';', '@', '+', '=', '|', '<', '♠', '♣', '♥', '♦', '%']
    def test_check_for_match(self):
        """Test the match-checking function."""
        card1 = {'value': '&'}
        card2 = {'value': '&'}
        card3 = {'value': '$'}
        #Tester funcs
        # Check that matching cards return True
        self.assertTrue(check_for_match(card1, card2))
        # Check that non-matching cards return False
        self.assertFalse(check_for_match(card1, card3))
        self.assertFalse(check_for_match(card2, card3))

        card1 = {'value': '$'}
        card2 = {'value': '$'}
        card3 = {'value': '&'}
        #Tester funcs
        # Check that matching cards return True
        self.assertTrue(check_for_match(card1, card2))
        # Check that non-matching cards return False
        self.assertFalse(check_for_match(card1, card3))
        self.assertFalse(check_for_match(card2, card3))

        card1 = {'value': '?'}
        card2 = {'value': '?'}
        card3 = {'value': '&'}
        #Tester funcs
        # Check that matching cards return True
        self.assertTrue(check_for_match(card1, card2))
        # Check that non-matching cards return False
        self.assertFalse(check_for_match(card1, card3))
        self.assertFalse(check_for_match(card2, card3))

        card1 = {'value': '!'}
        card2 = {'value': '!'}
        card3 = {'value': '&'}
        #Tester funcs
        # Check that matching cards return True
        self.assertTrue(check_for_match(card1, card2))
        # Check that non-matching cards return False
        self.assertFalse(check_for_match(card1, card3))
        self.assertFalse(check_for_match(card2, card3))

        card1 = {'value': '€'}
        card2 = {'value': '€'}
        card3 = {'value': '&'}
        #Tester funcs
        # Check that matching cards return True
        self.assertTrue(check_for_match(card1, card2))
        # Check that non-matching cards return False
        self.assertFalse(check_for_match(card1, card3))
        self.assertFalse(check_for_match(card2, card3))
    
        card1 = {'value': '»'}
        card2 = {'value': '»'}
        card3 = {'value': '@'}
        #Tester funcs
        # Check that matching cards return True
        self.assertTrue(check_for_match(card1, card2))
        # Check that non-matching cards return False
        self.assertFalse(check_for_match(card1, card3))
        self.assertFalse(check_for_match(card2, card3))

        card1 = {'value': '*'}
        card2 = {'value': '*'}
        card3 = {'value': '@'}
        #Tester funcs
        # Check that matching cards return True
        self.assertTrue(check_for_match(card1, card2))
        # Check that non-matching cards return False
        self.assertFalse(check_for_match(card1, card3))
        self.assertFalse(check_for_match(card2, card3))

        card1 = {'value': '☺'}
        card2 = {'value': '☺'}
        card3 = {'value': '*'}
        #Tester funcs
        # Check that matching cards return True
        self.assertTrue(check_for_match(card1, card2))
        # Check that non-matching cards return False
        self.assertFalse(check_for_match(card1, card3))
        self.assertFalse(check_for_match(card2, card3))

        card1 = {'value': ':'}
        card2 = {'value': ':'}
        card3 = {'value': '*'}
        #Tester funcs
        # Check that matching cards return True
        self.assertTrue(check_for_match(card1, card2))
        # Check that non-matching cards return False
        self.assertFalse(check_for_match(card1, card3))
        self.assertFalse(check_for_match(card2, card3))

        card1 = {'value': '#'}
        card2 = {'value': '#'}
        card3 = {'value': '^'}
        #Tester funcs
        # Check that matching cards return True
        self.assertTrue(check_for_match(card1, card2))
        # Check that non-matching cards return False
        self.assertFalse(check_for_match(card1, card3))
        self.assertFalse(check_for_match(card2, card3))

    def test_game_completed(self):
        """Test the game completion check."""
        cards = [{'matched': True} for _ in range(50)]  # All cards matched
        self.assertTrue(game_completed(cards))  # Game should be completed

        cards = [{'matched': False} for _ in range(50)]  # No cards matched
        self.assertFalse(game_completed(cards))  # Game should not be completed

    # @patch('pygame.mouse.get_pos', return_value=(150, 150))  # Mock mouse position
    def test_invalid_mouse_click(self):
        """Test clicking outside the cards (no action should be taken)."""
        cards = create_cards()
        clicked_pos = (SCREEN_WIDTH + 10, SCREEN_WIDTH + 10)

        # Check that no card is selected if the click is outside of any card
        self.assertFalse(any(card['rect'].collidepoint(clicked_pos) for card in cards))

if __name__ == '__main__':
    unittest.main()    
