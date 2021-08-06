from connect_four.game.gameboard import GameBoard
import pytest

@pytest.fixture
def test_board():
    return GameBoard(shape=(6,7))

def test_gameboard_init(test_board):
    assert isinstance(test_board, GameBoard)

def test_game_shape():
    test_board = GameBoard()
    assert test_board.shape == (6, 7)

def test_board_values():
    assert False