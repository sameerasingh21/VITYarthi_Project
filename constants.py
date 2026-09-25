SNAKE = "Snake"
WATER = "Water"
GUN = "Gun"

CHOICES = [SNAKE, WATER, GUN]

WINNING_COMBINATIONS = {
    (SNAKE, WATER),
    (WATER, GUN),
    (GUN, SNAKE)
}