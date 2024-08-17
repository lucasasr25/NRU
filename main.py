import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("NRU Algorithm Visualization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Font
font = pygame.font.SysFont(None, 36)

# NRU Page class
class Page:
    def __init__(self, page_id):
        self.page_id = page_id
        self.reference_bit = random.choice([0, 1])
        self.modified_bit = random.choice([0, 1])
        self.classification = self.classify()
    
    def classify(self):
        return 2 * self.reference_bit + self.modified_bit
    
    def draw(self, x, y):
        color = [WHITE, YELLOW, BLUE, GREEN][self.classification]
        pygame.draw.rect(screen, color, (x, y, 180, 100))
        text = font.render(f"Page {self.page_id}", True, BLACK)
        screen.blit(text, (x + 10, y + 10))
        rm_text = font.render(f"R={self.reference_bit} M={self.modified_bit}", True, BLACK)
        screen.blit(rm_text, (x + 10, y + 50))

# Initialize pages
pages = [Page(i) for i in range(1, 9)]

def nru_replacement(pages):
    # Find the lowest classified page for replacement
    min_class = min(page.classification for page in pages)
    candidates = [page for page in pages if page.classification == min_class]
    return random.choice(candidates)

# Main loop
running = True
while running:
    screen.fill(BLACK)
    
    # Draw pages
    for i, page in enumerate(pages):
        page.draw(50 + (i % 4) * 150, 50 + (i // 4) * 150)
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Simulate page replacement
                replaced_page = nru_replacement(pages)
                replaced_page.reference_bit = random.choice([0, 1])
                replaced_page.modified_bit = random.choice([0, 1])
                replaced_page.classification = replaced_page.classify()
    
    # Display instructions
    instructions = font.render("Press SPACE to replace a page using NRU", True, WHITE)
    screen.blit(instructions, (50, 500))
    
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
