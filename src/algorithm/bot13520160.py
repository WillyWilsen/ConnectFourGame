from turtle import pos
from src.constant import ColorConstant, GameConstant
from src.model import State
import random

class Bot13520160:
    def __init__(self) -> None:
        pass

    def find(self, state: State, player: int, thinking_time: float) -> int:
        """
        [DESC]
            Function to find the best move for player
        [PARAMS]
            state: State -> current state
            player: int -> player to find the best move
            thinking_time: float -> time limit for bot to find the best move
        [RETURN]
            int -> column to place piece
        """
        # Implement greedy algorithm here66
        # ...
        player_color = GameConstant.PLAYER_COLOR[player]
        if (player == 1):
            other_color = GameConstant.PLAYER_COLOR[player - 1]
        else:
            other_color = GameConstant.PLAYER_COLOR[player + 1]

        # PRIORITY ATTACK
        for i in range(state.board.row):
            for j in range(state.board.col):
                if (state.board.__getitem__(pos=[i, j]).color == player_color):
                    if (i > 2):
                        # PRIORITY ATTACK VERTICAL
                        if (state.board.__getitem__(pos=[i - 1, j]).color == player_color and 
                        state.board.__getitem__(pos=[i - 2, j]).color == player_color and state.board.__getitem__(pos=[i - 3, j]).color != other_color):
                            if (state.board.__getitem__(pos=[0, j]).color == ColorConstant.BLACK):
                                return j
                        
                        # PRIORITY ATTACK DIAGONAL
                        if (j > 0 and j < 4):
                            if (state.board.__getitem__(pos=[i - 1, j + 1]).color == player_color and 
                            state.board.__getitem__(pos=[i - 2, j + 2]).color == player_color):
                                if (i != 5):
                                    if (state.board.__getitem__(pos=[i + 1, j - 1]).color == ColorConstant.BLACK and state.board.__getitem__(pos=[0, j - 1]).color == ColorConstant.BLACK):
                                        if (i == 4):
                                            return j - 1
                                        else:
                                            if (state.board.__getitem__(pos=[i + 2, j - 1]).color != ColorConstant.BLACK):
                                                return j - 1

                                if (state.board.__getitem__(pos=[i - 2, j + 3]).color != ColorConstant.BLACK and
                                state.board.__getitem__(pos=[i - 3, j + 3]).color != other_color and state.board.__getitem__(pos=[0, j + 3]).color == ColorConstant.BLACK):
                                    return j + 3
                            else:
                                if (state.board.__getitem__(pos=[i - 1, j + 1]).color == player_color and 
                                state.board.__getitem__(pos=[i - 2, j + 2]).color != other_color and state.board.__getitem__(pos=[i - 3, j + 3]).color == player_color):
                                    if (state.board.__getitem__(pos=[i - 1, j + 2]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j + 2]).color == ColorConstant.BLACK):
                                        return j + 2
                                else:
                                    if (state.board.__getitem__(pos=[i - 1, j + 1]).color != other_color and 
                                    state.board.__getitem__(pos=[i - 2, j + 2]).color == player_color and state.board.__getitem__(pos=[i - 3, j + 3]).color == player_color):
                                        if (state.board.__getitem__(pos=[i, j + 1]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j + 1]).color == ColorConstant.BLACK):
                                            return j + 1
                        
                        if (j > 2 and j < 6):
                            if (state.board.__getitem__(pos=[i - 1, j - 1]).color == player_color and 
                            state.board.__getitem__(pos=[i - 2, j - 2]).color == player_color):
                                if (i != 5):
                                    if (state.board.__getitem__(pos=[i + 1, j + 1]).color == ColorConstant.BLACK and state.board.__getitem__(pos=[0, j + 1]).color == ColorConstant.BLACK):
                                        if (i == 4):
                                            return j + 1
                                        else:
                                            if (state.board.__getitem__(pos=[i + 2, j + 1]).color != ColorConstant.BLACK):
                                                return j + 1
                                                
                                if (state.board.__getitem__(pos=[i - 2, j - 3]).color != ColorConstant.BLACK and 
                                state.board.__getitem__(pos=[i - 3, j - 3]).color != other_color and state.board.__getitem__(pos=[0, j - 3]).color == ColorConstant.BLACK):
                                    return j - 3
                            else:
                                if (state.board.__getitem__(pos=[i - 1, j - 1]).color == player_color and 
                                state.board.__getitem__(pos=[i - 2, j - 2]).color != other_color and state.board.__getitem__(pos=[i - 3, j - 3]).color == player_color):
                                    if (state.board.__getitem__(pos=[i - 1, j - 2]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j - 2]).color == ColorConstant.BLACK):
                                        return j - 2
                                else:
                                    if (state.board.__getitem__(pos=[i - 1, j - 1]).color != other_color and 
                                    state.board.__getitem__(pos=[i - 2, j - 2]).color == player_color and state.board.__getitem__(pos=[i - 3, j - 3]).color == player_color):
                                        if (state.board.__getitem__(pos=[i, j - 1]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j - 2]).color == ColorConstant.BLACK):
                                            return j - 1

                    # PRIORITY ATTACK HORIZONTAL
                    if (j >= 0 and j < 4):
                        if (state.board.__getitem__(pos=[i, j + 1]).color == player_color and 
                        state.board.__getitem__(pos=[i, j + 2]).color == player_color and state.board.__getitem__(pos=[i, j + 3]).color != other_color):
                            if (state.board.__getitem__(pos=[0, j + 3]).color == ColorConstant.BLACK):
                                if (i == 5):
                                    return j + 3
                                else:
                                    if (state.board.__getitem__(pos=[i + 1, j + 3]).color != ColorConstant.BLACK):
                                        return j + 3
                        else:
                            if (state.board.__getitem__(pos=[i, j + 1]).color == player_color and 
                            state.board.__getitem__(pos=[i, j + 2]).color != other_color and state.board.__getitem__(pos=[i, j + 3]).color == player_color):
                                if (state.board.__getitem__(pos=[0, j + 2]).color == ColorConstant.BLACK):
                                    if (i == 5):
                                        return j + 2
                                    else:
                                        if (state.board.__getitem__(pos=[i + 1, j + 2]).color != ColorConstant.BLACK):
                                            return j + 2
                            else:
                                if (state.board.__getitem__(pos=[i, j + 1]).color != other_color and 
                                state.board.__getitem__(pos=[i, j + 2]).color == player_color and state.board.__getitem__(pos=[i, j + 3]).color == player_color):
                                    if (state.board.__getitem__(pos=[0, j + 1]).color == ColorConstant.BLACK):
                                        if (i == 5):
                                            return j + 1
                                        else:
                                            if (state.board.__getitem__(pos=[i + 1, j + 1]).color != ColorConstant.BLACK):
                                                return j + 1

                    if (j > 2 and j <= 6):
                        if (state.board.__getitem__(pos=[i, j - 1]).color == player_color and 
                        state.board.__getitem__(pos=[i, j - 2]).color == player_color and state.board.__getitem__(pos=[i, j - 3]).color != other_color):
                            if (state.board.__getitem__(pos=[0, j - 3]).color == ColorConstant.BLACK):
                                if (i == 5):
                                    return j - 3
                                else:
                                    if (state.board.__getitem__(pos=[i + 1, j - 3]).color != ColorConstant.BLACK):
                                        return j - 3
                        else:
                            if (state.board.__getitem__(pos=[i, j - 1]).color == player_color and 
                            state.board.__getitem__(pos=[i, j - 2]).color != other_color and state.board.__getitem__(pos=[i, j - 3]).color == player_color):
                                if (state.board.__getitem__(pos=[0, j - 2]).color == ColorConstant.BLACK):
                                    if (i == 5):
                                        return j - 2
                                    else:
                                        if (state.board.__getitem__(pos=[i + 1, j - 2]).color != ColorConstant.BLACK):
                                            return j - 2
                            else:
                                if (state.board.__getitem__(pos=[i, j - 1]).color != other_color and 
                                state.board.__getitem__(pos=[i, j - 2]).color == player_color and state.board.__getitem__(pos=[i, j - 3]).color == player_color):
                                    if (state.board.__getitem__(pos=[0, j - 1]).color == ColorConstant.BLACK):
                                        if (i == 5):
                                            return j - 1
                                        else:
                                            if (state.board.__getitem__(pos=[i + 1, j - 1]).color != ColorConstant.BLACK):
                                                return j - 1

        # DEFEND
        for i in range(state.board.row):
            for j in range(state.board.col):
                if (state.board.__getitem__(pos=[i, j]).color == other_color):
                    if (i > 0 and i < 4):
                        # DEFEND VERTICAL
                        if (state.board.__getitem__(pos=[i - 1, j]).color != player_color and 
                        state.board.__getitem__(pos=[i + 1, j]).color == other_color and state.board.__getitem__(pos=[i + 2, j]).color == other_color):
                            if (state.board.__getitem__(pos=[0, j]).color == ColorConstant.BLACK):
                                return j

                        # DEFEND DIAGONAL
                        if (j > 0 and j < 4):
                            if (state.board.__getitem__(pos=[i - 1, j - 1]).color != player_color and 
                            state.board.__getitem__(pos=[i + 1, j + 1]).color == other_color and state.board.__getitem__(pos=[i + 2, j + 2]).color == other_color):
                                if (state.board.__getitem__(pos=[i, j - 1]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j - 1]).color == ColorConstant.BLACK):
                                    return j - 1
                            
                                if (state.board.__getitem__(pos=[i + 3, j + 3]).color == ColorConstant.BLACK and state.board.__getitem__(pos=[0, j + 3]).color == ColorConstant.BLACK):
                                    if (i != 3):
                                        return j + 3
                                    else:
                                        if (state.board.__getitem__(pos=[i + 4, j + 3]).color != ColorConstant.BLACK):
                                            return j + 3
                        
                        if (j > 2 and j < 6):
                            if (state.board.__getitem__(pos=[i - 1, j + 1]).color != player_color and 
                            state.board.__getitem__(pos=[i + 1, j - 1]).color == other_color and state.board.__getitem__(pos=[i + 2, j - 2]).color == other_color):
                                if (state.board.__getitem__(pos=[i, j + 1]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j + 1]).color == ColorConstant.BLACK):
                                    return j + 1

                                if (state.board.__getitem__(pos=[i + 3, j - 3]).color == ColorConstant.BLACK and state.board.__getitem__(pos=[0, j - 3]).color == ColorConstant.BLACK):
                                    if (i != 3):
                                        return j - 3
                                    else:
                                        if (state.board.__getitem__(pos=[i + 4, j - 3]).color != ColorConstant.BLACK):
                                            return j - 3

                    # DEFEND HORIZONTAL
                    if (state.board.__getitem__(pos=[i, 3]).color == ColorConstant.BLACK):
                        if (state.board.__getitem__(pos=[0, 3]).color == ColorConstant.BLACK):
                            if (i != 5):
                                if (state.board.__getitem__(pos=[i + 1, 3]).color != ColorConstant.BLACK):
                                    return 3
                            else:
                                return 3
                    else:
                        if (j > 0 and j < 4):
                            if (state.board.__getitem__(pos=[i, j - 1]).color != player_color and 
                            (state.board.__getitem__(pos=[i, j + 1]).color == other_color or state.board.__getitem__(pos=[i, j + 2]).color == other_color)):
                                if (state.board.__getitem__(pos=[i, j + 1]).color == ColorConstant.BLACK and state.board.__getitem__(pos=[0, j + 1]).color == ColorConstant.BLACK):
                                    if (i == 5):
                                        return j + 1
                                    else:
                                        if (state.board.__getitem__(pos=[i + 1, j + 1]).color != ColorConstant.BLACK):
                                            return j + 1

                                if (state.board.__getitem__(pos=[i, j - 1]).color == ColorConstant.BLACK and state.board.__getitem__(pos=[0, j - 1]).color == ColorConstant.BLACK):
                                    if (i == 5):
                                        return j - 1
                                    else:
                                        if (state.board.__getitem__(pos=[i + 1, j - 1]).color != ColorConstant.BLACK):
                                            return j - 1
                        
                        if (j > 2 and j < 6):
                            if (state.board.__getitem__(pos=[i, j + 1]).color != player_color and 
                            (state.board.__getitem__(pos=[i, j - 1]).color == other_color or state.board.__getitem__(pos=[i, j - 2]).color == other_color)):
                                if (state.board.__getitem__(pos=[i, j - 1]).color == ColorConstant.BLACK and state.board.__getitem__(pos=[0, j - 1]).color == ColorConstant.BLACK):
                                    if (i == 5):
                                        return j - 1
                                    else:
                                        if (state.board.__getitem__(pos=[i + 1, j - 1]).color != ColorConstant.BLACK):
                                            return j - 1

                                if (state.board.__getitem__(pos=[i, j + 1]).color == ColorConstant.BLACK and state.board.__getitem__(pos=[0, j + 1]).color == ColorConstant.BLACK):
                                    if (i == 5):
                                        return j + 1
                                    else:
                                        if (state.board.__getitem__(pos=[i + 1, j + 1]).color != ColorConstant.BLACK):
                                            return j + 1

        # ATTACK
        for i in range(state.board.row):
            for j in range(state.board.col):
                if (state.board.__getitem__(pos=[i, j]).color == player_color):
                    if (i > 2):
                        # ATTACK VERTICAL
                        if (state.board.__getitem__(pos=[i - 1, j]).color != other_color and 
                        state.board.__getitem__(pos=[i - 2, j]).color != other_color and state.board.__getitem__(pos=[i - 3, j]).color != other_color):
                            if (state.board.__getitem__(pos=[0, j]).color == ColorConstant.BLACK):
                                return j

                        # ATTACK DIAGONAL
                        if (j > 0 and j < 4):
                            if (state.board.__getitem__(pos=[i - 1, j + 1]).color != other_color and 
                            state.board.__getitem__(pos=[i - 2, j + 2]).color != other_color and state.board.__getitem__(pos=[i - 3, j + 3]).color != other_color):
                                if (i != 5):
                                    if (state.board.__getitem__(pos=[i + 1, j - 1]).color == ColorConstant.BLACK and state.board.__getitem__(pos=[0, j - 1]).color == ColorConstant.BLACK):
                                        if (i == 4):
                                            return j - 1
                                        else:
                                            if (state.board.__getitem__(pos=[i + 2, j - 1]).color != ColorConstant.BLACK):
                                                return j - 1

                                if (state.board.__getitem__(pos=[i - 1, j + 1]).color != player_color):
                                    if (state.board.__getitem__(pos=[i, j + 1]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j + 1]).color == ColorConstant.BLACK):
                                        return j + 1
                                else:
                                    if (state.board.__getitem__(pos=[i - 2, j + 2]).color != player_color):
                                        if (state.board.__getitem__(pos=[i - 1, j + 2]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j + 2]).color == ColorConstant.BLACK):
                                            return j + 2
                                    else:
                                        if (state.board.__getitem__(pos=[i - 3, j + 3]).color != player_color):
                                            if (state.board.__getitem__(pos=[i - 2, j + 3]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j + 3]).color == ColorConstant.BLACK):
                                                return j + 3
                        
                        if (j > 2 and j < 6):
                            if (state.board.__getitem__(pos=[i - 1, j - 1]).color != other_color and 
                            state.board.__getitem__(pos=[i - 2, j - 2]).color != other_color and state.board.__getitem__(pos=[i - 3, j - 3]).color != other_color):
                                if (i != 5):
                                    if (state.board.__getitem__(pos=[i + 1, j + 1]).color == ColorConstant.BLACK and state.board.__getitem__(pos=[0, j + 1]).color == ColorConstant.BLACK):
                                        if (i == 4):
                                            return j + 1
                                        else:
                                            if (state.board.__getitem__(pos=[i + 2, j + 1]).color != ColorConstant.BLACK):
                                                return j + 1

                                if (state.board.__getitem__(pos=[i - 1, j - 1]).color != player_color):
                                    if (state.board.__getitem__(pos=[i, j - 1]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j - 1]).color == ColorConstant.BLACK):
                                        return j - 1
                                else:
                                    if (state.board.__getitem__(pos=[i - 2, j - 2]).color != player_color):
                                        if (state.board.__getitem__(pos=[i - 1, j - 2]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j - 2]).color == ColorConstant.BLACK):
                                            return j - 2
                                    else:
                                        if (state.board.__getitem__(pos=[i - 3, j - 3]).color != player_color):
                                            if (state.board.__getitem__(pos=[i - 2, j - 3]).color != ColorConstant.BLACK and state.board.__getitem__(pos=[0, j - 3]).color == ColorConstant.BLACK):
                                                return j - 3

                    # ATTACK HORIZONTAL
                    if (j >= 0 and j < 4):
                        if (state.board.__getitem__(pos=[i, j + 1]).color != other_color and 
                        state.board.__getitem__(pos=[i, j + 2]).color != other_color and state.board.__getitem__(pos=[i, j + 3]).color != other_color):
                            if (state.board.__getitem__(pos=[i, j + 2]).color != player_color and state.board.__getitem__(pos=[0, j + 2]).color == ColorConstant.BLACK):
                                if (i == 5):
                                    return j + 2
                                else:
                                    if (state.board.__getitem__(pos=[i + 1, j + 2]).color != ColorConstant.BLACK):
                                        return j + 2

                            if (state.board.__getitem__(pos=[i, j + 1]).color != player_color and state.board.__getitem__(pos=[0, j + 1]).color == ColorConstant.BLACK):
                                if (i == 5):
                                    return j + 1
                                else:
                                    if (state.board.__getitem__(pos=[i + 1, j + 1]).color != ColorConstant.BLACK):
                                        return j + 1

                    if (j > 2 and j <= 6):
                        if (state.board.__getitem__(pos=[i, j - 1]).color != other_color and 
                        state.board.__getitem__(pos=[i, j - 2]).color != other_color and state.board.__getitem__(pos=[i, j - 3]).color != other_color):
                            if (state.board.__getitem__(pos=[i, j - 2]).color != player_color and state.board.__getitem__(pos=[0, j - 2]).color == ColorConstant.BLACK):
                                if (i == 5):
                                    return j - 2
                                else:
                                    if (state.board.__getitem__(pos=[i + 1, j - 2]).color != ColorConstant.BLACK):
                                        return j - 2

                            if (state.board.__getitem__(pos=[i, j - 1]).color != player_color and state.board.__getitem__(pos=[0, j - 1]).color == ColorConstant.BLACK):
                                if (i == 5):
                                    return j - 1
                                else:
                                    if (state.board.__getitem__(pos=[i + 1, j - 1]).color != ColorConstant.BLACK):
                                        return j - 1

        if (state.board.__getitem__(pos=[0, 3]).color == ColorConstant.BLACK):
            return 3
        else:
            if (state.board.__getitem__(pos=[0, 2]).color == ColorConstant.BLACK):
                return 2
            else:
                if (state.board.__getitem__(pos=[0, 4]).color == ColorConstant.BLACK):
                    return 4
                else:
                    if (state.board.__getitem__(pos=[0, 1]).color == ColorConstant.BLACK):
                        return 1
                    else:
                        if (state.board.__getitem__(pos=[0, 5]).color == ColorConstant.BLACK):
                            return 5
                        else:
                            if (state.board.__getitem__(pos=[0, 0]).color == ColorConstant.BLACK):
                                return 0
                            else:
                                return 6
