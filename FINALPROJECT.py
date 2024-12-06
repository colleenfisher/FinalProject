import pygame
import random
import sys

pygame.init()

# Constants
CARD_WIDTH = 60
CARD_HEIGHT = 80
MARGIN = 5  
COLUMNS = 10
ROWS = 5
MARGIN_TOP = 100  
MARGIN_LEFT = MARGIN
SCREEN_WIDTH = COLUMNS * (CARD_WIDTH + MARGIN) + MARGIN_LEFT
SCREEN_HEIGHT = MARGIN_TOP + ROWS * (CARD_HEIGHT + MARGIN) + MARGIN

# Generate the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Memory Matching Game')

# Colors
BACKGROUND_COLOR = (30, 30, 30)
CARD_BACK_COLOR = (50, 50, 200)
CARD_FRONT_COLOR = (200, 200, 200)
TEXT_COLOR = (255, 255, 255)

# Load sound effects
positive_sound = pygame.mixer.Sound("/Users/colleenfisher/Documents/Foundations of Programming/game/positive_sound.wav")
negative_sound = pygame.mixer.Sound("/Users/colleenfisher/Documents/Foundations of Programming/game/negative_sound.wav")


# Function to create cards
def create_cards():
    symbols = ['&', '$', '?', '!', '€', '»', '~', '*', '☺', ':', '#', '^', '{', '[', ';', '@', '+', '=', '|', '<', '♠', '♣', '♥', '♦', '%']
    card_values = symbols * 2  
    random.shuffle(card_values)
    cards = []
    for row in range(ROWS):
        for col in range(COLUMNS):
            x = MARGIN_LEFT + col * (CARD_WIDTH + MARGIN)
            y = MARGIN_TOP + row * (CARD_HEIGHT + MARGIN)
            rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
            value = card_values.pop()
            card = {'rect': rect, 'value': value, 'matched': False, 'face_up': False}
            cards.append(card)
    return cards

# Function to check for a match
def check_for_match(card1, card2):
    return card1['value'] == card2['value']

# Function to check if the game is completed
def game_completed(cards):
    return all(card['matched'] for card in cards)

# Start menu function
def start_menu():
    font_name = pygame.font.match_font('segoeuisymbol, Arial Unicode MS, Arial')
    font = pygame.font.Font(font_name, 48)
    selected_mode = None
    
    while selected_mode is None:
        screen.fill(BACKGROUND_COLOR)
        
        title_text = font.render("Memory Matching Game", True, TEXT_COLOR)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        # Draw buttons for Easy, Medium, and Hard modes
        easy_button = font.render("1. Easy (Untimed)", True, TEXT_COLOR)
        medium_button = font.render("2. Medium (Timed)", True, TEXT_COLOR)
        hard_button = font.render("3. Hard (Timed with Penalty)", True, TEXT_COLOR)
        easy_rect = easy_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
        medium_rect = medium_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        hard_rect = hard_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))

        screen.blit(easy_button, easy_rect)
        screen.blit(medium_button, medium_rect)
        screen.blit(hard_button, hard_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_mode = 'easy'
                elif event.key == pygame.K_2:
                    selected_mode = 'medium'
                elif event.key == pygame.K_3:
                    selected_mode = 'hard'

    return selected_mode

# Function to display the game over or win screen 
def display_end_menu(result_text):
    font_name = pygame.font.match_font('segoeuisymbol, Arial Unicode MS, Arial')
    font_large = pygame.font.Font(font_name, 72)
    font_small = pygame.font.Font(font_name, 36)
    display_time = pygame.time.get_ticks()
    waiting_for_input = True

    while waiting_for_input:
        screen.fill(BACKGROUND_COLOR)
        text = font_large.render(result_text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        screen.blit(text, text_rect)

        replay_text = font_small.render("Press R to Play Again or Q to Quit", True, TEXT_COLOR)
        replay_rect = replay_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(replay_text, replay_rect)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Play again
                    waiting_for_input = False
                    return True
                elif event.key == pygame.K_q:  # Quit game
                    pygame.quit()
                    sys.exit()

        # Check if 30 seconds have passed since the end screen appeared
        if pygame.time.get_ticks() - display_time >= 30000:
            waiting_for_input = False  # Automatically close after 30 seconds

        pygame.display.flip()

# Main game function
def main():
    global timer_duration
    selected_mode = start_menu()
    
    # Set timer duration based on selected mode
    if selected_mode == 'easy':
        timer_duration = None  # No timer 
    elif selected_mode == 'medium':
        timer_duration = 8* 1000  #Timed mode without penalty
    elif selected_mode == 'hard':
        timer_duration = 15 * 1000  # Timed mode with penalty

    while True:  # Main game loop
        cards = create_cards()
        first_card = None
        second_card = None
        waiting = False
        wait_time = 1000  
        wait_start_time = None
        game_over = False
        attempts = 0
        matches = 0

        # Timer variables
        timer_start_time = None
        timer_running = False

        clock = pygame.time.Clock()
        font_name = pygame.font.match_font('segoeuisymbol, Arial Unicode MS, Arial')
        font = pygame.font.Font(font_name, 36)

        running = True
        while running:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not waiting and not game_over:
                    pos = pygame.mouse.get_pos()
                    for card in cards:
                        if card['rect'].collidepoint(pos) and not card['face_up'] and not card['matched']:
                            card['face_up'] = True
                            if not first_card:
                                first_card = card
                                if not timer_running and timer_duration is not None:  # Start the timer for timed mode
                                    timer_start_time = pygame.time.get_ticks()
                                    timer_running = True
                            elif not second_card:
                                second_card = card
                                waiting = True
                                wait_start_time = pygame.time.get_ticks()
                                attempts += 1
                            break  

            if timer_running:
                elapsed_time = pygame.time.get_ticks() - timer_start_time
                remaining_time = max(0, timer_duration - elapsed_time)
                if remaining_time <= 0:
                    game_over = True

            if waiting:
                current_time = pygame.time.get_ticks()
                if current_time - wait_start_time >= wait_time:
                    if check_for_match(first_card, second_card):
                        first_card['matched'] = True
                        second_card['matched'] = True
                        matches += 1
                        positive_sound.play()  # Play positive sound for a match
                    else:
                        first_card['face_up'] = False
                        second_card['face_up'] = False
                        negative_sound.play()  # Play negative sound for no match
                        if selected_mode == 'hard' and timer_running:  # Deduct 1 second for incorrect match in Hard mode
                            timer_start_time -= 1000  # Deduct 1 second (1000 milliseconds)
                    first_card = None
                    second_card = None
                    waiting = False

            if not game_over and game_completed(cards):
                game_over = True
                timer_running = False  # Stop the timer for timed mode

            screen.fill(BACKGROUND_COLOR)
            if timer_running:
                timer_text = font.render(f'Time Left: {remaining_time // 1000}', True, TEXT_COLOR)
                timer_rect = timer_text.get_rect(topleft=(MARGIN, MARGIN))
                screen.blit(timer_text, timer_rect)

            attempts_text = font.render(f'Attempts: {attempts}', True, TEXT_COLOR)
            matches_text = font.render(f'Matches: {matches}', True, TEXT_COLOR)
            attempts_rect = attempts_text.get_rect(topright=(SCREEN_WIDTH - MARGIN, MARGIN))
            matches_rect = matches_text.get_rect(topright=(SCREEN_WIDTH - MARGIN, attempts_rect.bottom + 5))
            screen.blit(attempts_text, attempts_rect)
            screen.blit(matches_text, matches_rect)

            for card in cards:
                if card['face_up'] or card['matched']:
                    pygame.draw.rect(screen, CARD_FRONT_COLOR, card['rect'])
                    text = font.render(str(card['value']), True, (0, 0, 0))
                    text_rect = text.get_rect(center=card['rect'].center)
                    screen.blit(text, text_rect)
                else:
                    pygame.draw.rect(screen, CARD_BACK_COLOR, card['rect'])

            if game_over:
                result_text = "You Win!" if matches == len(cards) // 2 else "Game Over!"
                if display_end_menu(result_text):  # Show end menu and check if play again is chosen
                    break  # Restart 
                else:
                    running = False  # Exit 
                pygame.quit()
                sys.exit()

            pygame.display.flip()

# Run the game
main()


