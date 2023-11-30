
# B1 Techadon - Chess Game (MOVES ONLY)
import pygame
import sys
import random


pygame.init()

# Insert board here...
WIDTH, HEIGHT = 750, 750
TILE_SIZE = WIDTH // 8
brown = (150, 75, 0)  
beige = (245, 245, 220)  

# Initialize Pygame
pygame.init()

# Create the chessboard
chessboard = [[beige if (i + j) % 2 == 0 else brown for j in range(8)] for i in range(8)]

# Create the Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard")


    # Draw the chessboard
for row in range(8):
        for col in range(8):
            pygame.draw.rect(screen, chessboard[row][col], (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Update the display
pygame.display.flip()

# Initialize lists to store captured pieces
captured_player_pieces = []
captured_opponent_pieces = []

# Load images for pieces (white and black)
W1 = pygame.image.load("Imgs/W_bishop.png")
W1 = pygame.transform.scale(W1,(100,100))
B1 = pygame.image.load("Imgs/B_bishop.png")
B1 = pygame.transform.scale(B1,(100,100))
W2 = pygame.image.load("Imgs/W_knight.png")
W2 = pygame.transform.scale(W2,(100,100))
B2 = pygame.image.load("Imgs/B_knight.png")
B2 = pygame.transform.scale(B2,(100,100))
W3 = pygame.image.load("Imgs/W_rook.png")
W3 = pygame.transform.scale(W3,(100,100))
B3 = pygame.image.load("Imgs/B_rook.png")
B3 = pygame.transform.scale(B3,(100,100))
W4 = pygame.image.load("Imgs/W_queen.png")
W4 = pygame.transform.scale(W4,(100,100))
B4 = pygame.image.load("Imgs/B_queen.png")
B4 = pygame.transform.scale(B4,(100,100))
W5 = pygame.image.load("Imgs/W_pawn.png")
W5 = pygame.transform.scale(W5,(100,100))
B5 = pygame.image.load("Imgs/B_pawn.png")
B5 = pygame.transform.scale(B5,(100,100))
W6 = pygame.image.load("Imgs/W_king.png")
W6 = pygame.transform.scale(W6,(100,100))
B6 = pygame.image.load("Imgs/B_king.png")
B6 = pygame.transform.scale(B6,(100,100))

screen.blit(B3,(0,0))

# Initial positions for pieces
player_pieces = {
    (1, 0): W5,
    (1, 1): W5,
    (1, 2): W5,
    (1, 3): W5,
    (1, 4): W5,
    (1, 5): W5,
    (1, 6): W5,
    (1, 7): W5,
    (0, 0): W3,
    (0, 1): W2,
    (0, 2): W1,
    (0, 3): W4,
    (0, 4): W6,
    (0, 5): W1,
    (0, 6): W2,
    (0, 7): W3,
}

opponent_pieces = {
    (6, 0): B5,
    (6, 1): B5,
    (6, 2): B5,
    (6, 3): B5,
    (6, 4): B5,
    (6, 5): B5,
    (6, 6): B5,
    (6, 7): B5,
    (7, 0): B3,
    (7, 1): B2,
    (7, 2): B1,
    (7, 3): B4,
    (7, 4): B6,
    (7, 5): B1,
    (7, 6): B2,
    (7, 7): B3,
}


def draw_pieces():
    for position, image in player_pieces.items():
        screen.blit(image, (position[1] * 100, position[0] * 100))
    for position, image in opponent_pieces.items():
        screen.blit(image, (position[1] * 100, position[0] * 100))


running = True
has_king_moved = False
has_queen_rook_moved = False
has_king_rook_moved = False
# Function to get all possible moves for a given player
def get_possible_moves(player_pieces):
    possible_moves = []
    for position in player_pieces:
        row, col = position
        piece = player_pieces[position]
        if piece in [W5, B5]:
            # Pawn moves
            direction = 1 if piece == W5 else -1
            # Move one square forward
            new_position = (row + direction, col)
            if new_position not in player_pieces and 0 <= new_position[0] < 8:
                possible_moves.append((position, new_position))
            # Move two squares forward (only on the first move)
            new_position = (row + 2 * direction, col)
            if (
                position[0] == (1 if piece == W5 else 6)
                and new_position not in player_pieces
                and (row + direction, col) not in player_pieces
                and 0 <= new_position[0] < 8
            ):
                possible_moves.append((position, new_position))
            # Capture diagonally
            new_position = (row + direction, col + 1)
            if new_position in opponent_pieces:
                possible_moves.append((position, new_position))
            new_position = (row + direction, col - 1)
            if new_position in opponent_pieces:
                possible_moves.append((position, new_position))
        elif piece in [W3, B3]:
            # Rook moves
            for i in range(-7, 8):
                if i != 0:
                    new_position = (row + i, col)
                    if 0 <= new_position[0] < 8 and new_position not in player_pieces:
                        possible_moves.append((position, new_position))
                    new_position = (row, col + i)
                    if 0 <= new_position[1] < 8 and new_position not in player_pieces:
                        possible_moves.append((position, new_position))
        elif piece in [W2, B2]:
            # Knight moves
            for i in [-2, -1, 1, 2]:
                for j in [-2, -1, 1, 2]:
                    if abs(i) + abs(j) == 3:
                        new_position = (row + i, col + j)
                        if (
                            0 <= new_position[0] < 8
                            and 0 <= new_position[1] < 8
                            and new_position not in player_pieces
                        ):
                            possible_moves.append((position, new_position))
        elif piece in [W1, B1]:
            # Bishop moves
            for i in range(-7, 8):
                if i != 0:
                    new_position = (row + i, col + i)
                    if (
                        0 <= new_position[0] < 8
                        and 0 <= new_position[1] < 8
                        and new_position not in player_pieces
                    ):
                        possible_moves.append((position, new_position))
                    new_position = (row + i, col - i)
                    if (
                        0 <= new_position[0] < 8
                        and 0 <= new_position[1] < 8
                        and new_position not in player_pieces
                    ):
                        possible_moves.append((position, new_position))
        elif piece in [W4, B4]:
            # Queen moves
            for i in range(-7, 8):
                if i != 0:
                    new_position = (row + i, col)
                    if (
                        0 <= new_position[0] < 8
                        and new_position not in player_pieces
                    ):
                        possible_moves.append((position, new_position))
                    new_position = (row, col + i)
                    if (
                        0 <= new_position[1] < 8
                        and new_position not in player_pieces
                    ):
                        possible_moves.append((position, new_position))
                    new_position = (row + i, col + i)
                    if (
                        0 <= new_position[0] < 8
                        and 0 <= new_position[1] < 8
                        and new_position not in player_pieces
                    ):
                        possible_moves.append((position, new_position))
                    new_position = (row + i, col - i)
                    if (
                        0 <= new_position[0] < 8
                        and 0 <= new_position[1] < 8
                        and new_position not in player_pieces
                    ):
                        possible_moves.append((position, new_position))
        elif piece in [W6, B6]:
            # King moves
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i != 0 or j != 0:
                        new_position = (row + i, col + j)
                        if (
                            0 <= new_position[0] < 8
                            and 0 <= new_position[1] < 8
                            and new_position not in player_pieces
                        ):
                            possible_moves.append((position, new_position))
        
            # Castling for the player
            if piece == W6 and not has_king_moved and not is_check(player_pieces, opponent_pieces):
                # Castling king side
                if (
                    (7, 6) not in player_pieces and (7, 5) not in player_pieces
                    and (7, 7) in player_pieces and not has_king_rook_moved
                ):
                    # Check if the squares the king would move through are not under attack
                    if not any(
                        is_square_under_attack(player_pieces, opponent_pieces, (7, 5), "black")
                        or is_square_under_attack(player_pieces, opponent_pieces, (7, 6), "black")
                        for _ in range(3)
                    ):
                        possible_moves.append(((7, 4), (7, 6)))

                # Castling queen side
                if (
                    (7, 1) not in player_pieces and (7, 2) not in player_pieces and (7, 3) not in player_pieces
                    and (7, 0) in player_pieces and not has_queen_rook_moved
                ):
                    # Check if the squares the king would move through are not under attack
                    if not any(
                        is_square_under_attack(player_pieces, opponent_pieces, (7, 2), "black")
                        or is_square_under_attack(player_pieces, opponent_pieces, (7, 3), "black")
                        or is_square_under_attack(player_pieces, opponent_pieces, (7, 4), "black")
                        for _ in range(3)
                    ):
                        possible_moves.append(((7, 4), (7, 2)))                            
    return possible_moves

# Function to make a random move for the AI opponent
def make_random_move():
    possible_moves = get_possible_moves(opponent_pieces)
    if possible_moves:
        return random.choice(possible_moves)
    return None

# Function to check if a square is under attack by the opponent
def is_square_under_attack(player_pieces, opponent_pieces, square, player_color):
    opponent_color = "white" if player_color == "black" else "black"
    for position, piece in opponent_pieces.items():
        if piece in [W5, B5] and (
            (piece == W5 and player_color == "black") or
            (piece == B5 and player_color == "white")
        ):
            # Pawn attack squares
            attack_squares = [
                (position[0] + 1, position[1] + 1),
                (position[0] + 1, position[1] - 1)
            ]
            if square in attack_squares:
                return True
        elif piece in [W3, B3]:
            # Rook attack squares
            if position[0] == square[0] or position[1] == square[1]:
                return True
        elif piece in [W2, B2]:
            # Knight attack squares
            attack_squares = [
                (position[0] + 2, position[1] + 1),
                (position[0] + 2, position[1] - 1),
                (position[0] - 2, position[1] + 1),
                (position[0] - 2, position[1] - 1),
                (position[0] + 1, position[1] + 2),
                (position[0] + 1, position[1] - 2),
                (position[0] - 1, position[1] + 2),
                (position[0] - 1, position[1] - 2)
            ]
            if square in attack_squares:
                return True
        elif piece in [W1, B1]:
            # Bishop attack squares
            if abs(position[0] - square[0]) == abs(position[1] - square[1]):
                return True
        elif piece in [W4, B4]:
            # Queen attack squares
            if position[0] == square[0] or position[1] == square[1] or abs(position[0] - square[0]) == abs(position[1] - square[1]):
                return True
        elif piece in [W6, B6]:
            # King attack squares
            attack_squares = [
                (position[0] + 1, position[1]),
                (position[0] - 1, position[1]),
                (position[0], position[1] + 1),
                (position[0], position[1] - 1),
                (position[0] + 1, position[1] + 1),
                (position[0] + 1, position[1] - 1),
                (position[0] - 1, position[1] + 1),
                (position[0] - 1, position[1] - 1)
            ]
            if square in attack_squares:
                return True

    return False

# Function to check if the player's king is in check
def is_check(player_pieces, opponent_pieces):
    player_king_position = None
    for position, piece in player_pieces.items():
        if piece in [W6, B6]:
            player_king_position = position
            break

    opponent_moves = [move[1] for move in get_possible_moves(opponent_pieces)]
    return player_king_position in opponent_moves

# Main game loop starts here...
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
            
pygame.quit()
sys.exit()

