import math

from kicker.model_game_bar import GameBar
from kicker.CONST_GAME_FIGURES import *
from kicker.CONST_BALL import Coordinate
from kicker.CONST_SIMULATION import SIMULATION_TIME_STEP
from kicker.CONST_SIMULATION import SHOOT_SPEED
from kicker.CONST_SIMULATION import BAR_SPEED
from kicker.CONST_KICKER import COURT_HEIGHT


class ComputerMidfielder(GameBar):
    """Konstanten"""
    NUMBER_OF_FIGURES = 5
    DISTANCE_FIGURES = MIDFIELDER_DISTANCE_BETWEEN_FIGURES
    POSITION_ON_BAR_MIDFIELDER_RIGHT_OUTSIDE = (COURT_HEIGHT - MAX_POS_MIDFIELDER - 4 * DISTANCE_FIGURES) / 2
    POSITION_ON_BAR_MIDFIELDER_RIGHT = (COURT_HEIGHT - MAX_POS_MIDFIELDER - 2 * DISTANCE_FIGURES) / 2
    POSITION_ON_BAR_MIDFIELDER_MIDDLE = (COURT_HEIGHT - MAX_POS_MIDFIELDER) / 2
    POSITION_ON_BAR_MIDFIELDER_LEFT = (COURT_HEIGHT - MAX_POS_MIDFIELDER + 2 * DISTANCE_FIGURES) / 2
    POSITION_ON_BAR_MIDFIELDER_LEFT_OUTSIDE = (COURT_HEIGHT - MAX_POS_MIDFIELDER + 4 * DISTANCE_FIGURES) / 2
    ABS_X_POSITION = BAR_POSITION_MIDFIELDER
    X_REFLECTION_PLANE = ABS_X_POSITION + FIGURE_FOOT_WIDTH + BALL_RADIUS
    X_OFFSET_REFLECTION_PLANE = FIGURE_FOOT_WIDTH + BALL_RADIUS
    Y_OFFSET_REFLECTION_PLANE = FIGURE_FOOT_HEIGHT / 2 + BALL_RADIUS

    def __init__(self):
        super().__init__(MAX_POS_MIDFIELDER / 2)


'''hier fehlen noch Methoden fürs Schießen und Collision der Spieler mit Ball'''
