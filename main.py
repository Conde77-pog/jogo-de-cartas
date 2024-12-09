import os
import pygame
import sys
from Button import *

class Card:
    def __init__(self, full_path, name):
        self.name = name.split(".")[0]
        self.texture = pygame.image.load(full_path) 
        self.texture = pygame.transform.scale(self.texture,(100,150))

pygame.init()
BG = pygame.image.load("assets/Background.png")
window_width, window_height = 800, 600


def get_font(size):
    return pygame.font.SysFont('Arial', size)
def play(deck):
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    # Preload background and text to avoid redrawing them every frame.
    BG = pygame.image.load("assets/Background.png")
    PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))

    # Create button once before the loop.
    PLAY_BACK = Button(
        image=pygame.image.load("assets/Rect.png"), pos=(640, 460),
        text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green"
    )

    running = True
    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # Draw static elements only once and minimize changes to the display.
        screen.blit(BG, (0, 0))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        # Update button color and check for hover effect.
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main()

        pygame.display.update()

def main():
    running = True
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Load and display the background image
    BG = pygame.image.load("assets/Background.png")
    pygame.transform.scale(BG,(5000,5000))
    deck = []

    directory_path = r"C:\Users\Guilherme\OneDrive\Ambiente de Trabalho\programação\python\jogo de cartas\assets\cards"

    try:
        files = os.listdir(directory_path)
        print("Files in directory:", files)
    except FileNotFoundError:
        print(f"Error: Directory {directory_path} not found.")
        sys.exit()
    except Exception as e:
        print(f"Unexpected error while listing directory: {e}")
        sys.exit()

    for name in files:
        full_path = os.path.join(directory_path, name)
        if os.path.isfile(full_path):
            try:
                deck.append(Card(full_path, name))
            except Exception as e:
                print(f"Failed to process {name}: {e}")
    
    PLAY_BUTTON = Button(
        image=pygame.image.load("assets/Rect.png"),
        pos=(640, 250),
        text_input="PLAY",
        font=get_font(75),
        base_color="#d7fcd4",
        hovering_color="White",
    )
    
    while running:
        screen.blit(BG, (0, 0))  # Draw background image
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Draw the menu text
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        screen.blit(MENU_TEXT, MENU_RECT)

        # Draw and update buttons
        PLAY_BUTTON.changeColor(MENU_MOUSE_POS)
        PLAY_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((800, 600))
                    pygame.display.set_caption("Windowed Mode")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(deck)

        pygame.display.update()

    pygame.quit()
    sys.exit()

main()