import os
import pygame
import sys

class Card:
    def __init__(self, full_path, name):
        self.name = name.split(".")[0]
        self.texture = pygame.image.load(full_path) 
        self.texture = pygame.transform.scale(self.texture,(200,300))

def main():

    pygame.init()

    running = True
    window_width, window_height = 800, 600
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    deck = []
    directory_path = r"C:\Users\Guilherme\OneDrive\Ambiente de Trabalho\programação\python\jogo de cartas\cards"


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
            print(f"Processing file: {name}")
            try:
                deck.append(Card(full_path, name))
            except Exception as e:
                print(f"Failed to process {name}: {e}")
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to exit fullscreen
                    screen = pygame.display.set_mode((800, 600))  # Switch to windowed mode
                    pygame.display.set_caption("Windowed Mode")
        
        screen.fill((0, 0, 0))
        
        for i, card in enumerate(deck):
            screen.blit(card.texture, (200 * i, 200 * i))
        
        pygame.display.flip()
    

    pygame.quit()
    sys.exit()

main()
