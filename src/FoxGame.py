# Letter IDs
F = "F"
O = "O"
X = "X"
E = " "


class FoxGame:
    """Instance of FoxGame"""

    def __init__(self) -> None:
        """
        Creates instance of FoxGame.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        self.board: list[list[str]] = (
            [[O, X, X, X],
             [F, O, E, E],
             [F, E, O, E],
             [F, E, E, O]])
        
        self.letters_left: dict[str, int] = {
            F: 5,
            O: 2,
            X: 5
        }

    def print_board(self) -> None:
        """
        Print the current board state

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        for row in self.board:
            for col in row:
                print(f"{col} ", end="")
            print()

    def get_total_letters_left(self) -> int:
        """
        Gets the number of letters remaining

        Parameters
        ----------
            None

        Returns
        -------
            remaining : int
                Number of letters remaining that can be drawn
        """
        remaining = 0
        for key in self.letters_left.keys():
            remaining += self.letters_left[key]
        
        return remaining

    def check_game_end(self) -> bool:
        """
        Checks whether "FOX" has been made on the board. Will check
        horizontal, vertical, diagonal, forwards, backwards. If it has, 
        the game is finished.

        Parameters
        ----------
            None

        Returns
        -------
            True : bool
                Returns if "FOX" has been made somewhere
            
            False : bool
                Returns if "FOX" has not been made somewhere
        """
        # Check horizontal
        for row in self.board:
            print(row)

    def check_fox(input_check: str) -> bool:
        """
        
        """
        # TODO: make sure input is exactly 3 or 4 characters

        if "FOX" in input_check:
            return True
        elif "XOF" in input_check:
            return True
        else:
            return False

