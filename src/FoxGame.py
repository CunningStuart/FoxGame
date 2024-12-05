# Letter IDs
F = 1
O = 2
X = 3


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
        self.board: list[list[int]] = (
            [[O, 0, 0, 0],
             [0, O, 0, 0],
             [0, 0, O, 0],
             [0, 0, 0, O]])
        
        self.letters_left: dict[int, int] = {
            F: 5,
            O: 2,
            X: 5
        }

    def letter_as_str(self, letter: int) -> str:
        """
        Get integer representation of letter as a string

        Parameters
        ----------
            letter : int
                Integer representation of F, O or X

        Returns
        -------
            " " : str
                Returns if letter is 0
            "F" : str
                Returns if letter is 1
            "O" : str
                Returns if letter is 2
            "X" : str
                Returns if letter is 3
            "ERR" : str
                Returns if input is not valid
        """
        if F == letter:
            return "F"
        elif O == letter:
            return "O"
        elif X == letter:
            return "X"
        elif 0 == letter:
            return " "
        else:
            return "ERR"

    def print_int(self) -> None:
        """
        Print the current board state, as integers

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

    def print_str(self) -> None:
        """
        Print the current board state, as letters

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        for row in self.board:
            for col in row:
                print(f"{self.letter_as_str(col)} ", end="")
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
        for i in range(1, 4):
            remaining += self.letters_left[i]
        
        return remaining

    def check_fox(self) -> bool:
        """
        Checks whether "FOX" has been made on the board. Will check
        horizontal, vertical, diagonal, forwards, backwards

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
        