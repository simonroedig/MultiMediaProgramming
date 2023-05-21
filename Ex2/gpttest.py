import pygame
import random

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
WIDTH = 1024
HEIGHT = 780

# Farben
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Fenster erstellen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meer-Spiel")

# Hintergrund des Fensters zeichnen
screen.fill(BLUE)

# Palmeninseln erstellen
def draw_island(x, y, size):
    pygame.draw.circle(screen, WHITE, (x, y), size)

islands = []
for _ in range(5):
    size = random.randint(20, 60)
    x = random.randint(size, WIDTH - size)
    y = random.randint(size, HEIGHT - size)
    draw_island(x, y, size)
    islands.append((x, y, size))

# Spielfigur erstellen
player_radius = 20
player_x = WIDTH // 2
player_y = HEIGHT // 2

def draw_player(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), player_radius)

draw_player(player_x, player_y)

# Linie für den Weg der Spielfigur zeichnen
path = []

# Spiel-Schleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            target_x, target_y = pygame.mouse.get_pos()
            path.append((player_x, player_y))

            # Weg zur Zielposition animieren
            while player_x != target_x or player_y != target_y:
                if player_x < target_x:
                    player_x += 1
                elif player_x > target_x:
                    player_x -= 1

                if player_y < target_y:
                    player_y += 1
                elif player_y > target_y:
                    player_y -= 1

                # Prüfen, ob die Spielfigur eine Insel berührt
                for island in islands:
                    island_x, island_y, island_size = island
                    distance = ((player_x - island_x) ** 2 + (player_y - island_y) ** 2) ** 0.5
                    if distance <= player_radius + island_size:
                        player_x, player_y = path[-1]  # Zurück zur vorherigen Position

                path.append((player_x, player_y))
                screen.fill(BLUE)  # Hintergrund neu zeichnen
                for island in islands:
                    island_x, island_y, island_size = island
                    draw_island(island_x, island_y, island_size)
                for i in range(len(path)-1):
                    pygame.draw.line(screen, WHITE, path[i], path[i+1], 2)
                draw_player(player_x, player_y)
                pygame.display.update()

# Pygame beenden
pygame.quit()
