# Author: Michael Nadeau
# GitHub username: michaelna1
# Date: 11/25/20022
# Description: Creates player, mancala board, and mancala class for playing the game of mancala. The player class
# has player objects with name attributes. The mancala board class updates the board by executing the moves of the game
# and implementing the special rules. The mancala class takes user input for game moves, displays the game board values,
# evaluates if the winning condition is met, returns the state of the game, and keeps track of the game state.


class Player:
    """Represents a player with a name. Includes a method for retrieving the player's name."""

    def __init__(self, name):
        """Creates a player object with a name data member."""

        self._name = name

    def get_name(self):
        """Returns the player object's name."""

        return self._name


class MancalaBoard:
    """Represents the game board for Mancala. Includes a dictionary of the board's elements, including the pits
    and stores for both players. Includes methods for retrieving the entire board, and the different elements. Also
    has methods for changing the board's values. Finally, includes a method for Mancala's game mechanics, called
    modify_board, which executes player moves initiated in the Mancala class-- addresses the games special rules, and
    updates the pits and stores for both players."""

    def __init__(self):
        """Creates an instance of a Mancala game board using the games initial conditions-- 4 seeds in each pit,
        and player stores starting at zero."""

        self._board = {"player_1_pits": [4,4,4,4,4,4],
                       "player_1_store": 0,
                       "player_2_pits": [4,4,4,4,4,4],
                       "player_2_store": 0}

    def get_board(self):
        """Returns the game board as a dictionary."""

        return self._board

    def get_player_1_pits(self):
        """Returns player 1's pits as a list."""

        return self._board["player_1_pits"]

    def set_player_1_pits(self, list):
        """Sets player 1's pits to new values, using a list argument."""

        self._board["player_1_pits"] = list

    def get_player_2_pits(self):
        """Returns player 2's pits as a list."""

        return self._board["player_2_pits"]

    def set_player_2_pits(self, list):
        """Sets player 2's pits to new values, using a list argument."""

        self._board["player_2_pits"] = list


    def get_player_1_store(self):
        """Returns player 1's store as an integer."""

        return self._board["player_1_store"]

    def set_player_1_store(self, seeds):
        """Sets player 1's store to a new value using an integer argument."""

        self._board["player_1_store"] += seeds

    def get_player_2_store(self):
        """Returns player 2's store as an integer."""

        return self._board["player_2_store"]

    def set_player_2_store(self, seeds):
        """Sets player 2's store to a new values using an integer argument."""

        self._board["player_2_store"] += seeds

    def modify_board(self, player, pit_number):
        """Executes moves by players initiated in the Mancala class. Uses the player and pit number argument to move
        seeds according to mancala's rules. Also implements the special rules: when the last seed lands in the player
        argument's stores, they can take another turn--this will be indicated by printing a string--, and if the player
        argument's turn ends with the last seed landing in one of their empty pits, they take that seed and the ones in
        the opposite pits and place them in their store. """

        if player == "player_1":            #determines which side of the board to start on.

            player_side = "player_1"

        else:

            player_side = "player_2"

        seeds = self._board[player + "_pits"][pit_number - 1]           #number of seeds in selected pit.
        self._board[player + "_pits"][pit_number - 1] = 0               #sets selected pit to zero; seeds removed.

        while seeds > 0:                                                #evaluates if seeds are still in one's "hand".

            pit_number += 1                                             #advances to next pit.
            if pit_number > 6 and player_side == "player_1" :           #conditional for player 1 reaching their store.
                if player == "player_1":                                #adds seed to store

                    self._board["player_1_store"] += 1
                    seeds -= 1

                    if all(pit == 0 for pit in self._board["player_1_pits"]) and seeds == 0:       #game end

                        return

                    if seeds == 0:                                      #special rule: player takes additional turn.

                        print("player 1 take another turn")

                player_side = "player_2"                                #shift to opposite side of board
                pit_number = 0

            elif pit_number > 6 and player_side == "player_2":          #conditional for player 2 reaching their store.
                if player == "player_2":

                    self._board["player_2_store"] += 1
                    seeds -= 1

                    if all(pit == 0 for pit in self._board["player_2_pits"]) and seeds == 0:    #game end

                        return

                    if seeds == 0:                                      #special rule: player takes additional turn.

                        print("player 2 take another turn")

                player_side = "player_1"                                #shift to opposite side of board.
                pit_number = 0

            else:                                                       #deposits seeds in each pit, and handles special rule.
                                                                        #in which player lands in empty pit and takes seeds on the opposite side.
                if seeds == 1 and self._board[player_side + "_pits"][pit_number - 1] == 0 and player_side == player:

                    if player == "player_1":

                        other_side_pit = self._board["player_2_pits"][6 - pit_number]      #seeds in opposite pit.
                        self._board["player_2_pits"][6 - pit_number] = 0

                    else:

                        other_side_pit = self._board["player_1_pits"][6 - pit_number]
                        self._board["player_1_pits"][6 - pit_number] = 0

                    self._board[player + "_store"] += 1 + other_side_pit                    #seeds added to player's store.
                    seeds -= 1

                else:

                    self._board[player_side + "_pits"][pit_number - 1] += 1                 #deposit a seed in pit.
                    seeds -= 1                                                              #decrement seeds in hand.


class Mancala:
    """Represents a mancala game with board, player, and game state attributes. Has methods to generate players,
    print the game board, play the game and return the winner."""

    def __init__(self):
        """Creates a mancala game with game board object from the MancalaBoard class, player object from the Player
        class,and game state attributes. The game state is updated for any wins or ties in the play_game() method."""

        self._board = MancalaBoard()
        self._player_1 = None
        self._player_2 = None
        self._game_state = "Game has not ended"


    def create_player(self, name):
        """Using a name argument, a Player object is created."""

        if self._player_1 == None:

            self._player_1 = Player(name)

        else:

            self._player_2 = Player(name)

    def print_board(self):
        """Prints the object from the MancalaBoard class, which is a dictionary, by displaying the player names,
        pits, and stores."""

        print("player1:")
        print(f"store: {self._board.get_player_1_store()}")
        print(self._board.get_player_1_pits())

        print("player2:")
        print(f"store: {self._board.get_player_2_store()}")
        print(self._board.get_player_2_pits())


    def play_game(self, player_index, pit_index):
        """Using the player number and pit index as arguments, the method executes moves in the mancala game. Uses
        the modify_board() method from the MancalaBoard class to update the game board and evaluates if the game has
        ended and updates the game_state attribute. Returns a string if the user mistakenly inputs an incorrect
        pit value or if the game is over. """

        if pit_index < 1 or pit_index > 6:                      #if user input has incorrect index for pits.
            return "Invalid number for pit index"

        if self._game_state != "Game has not ended":
            return "Game is ended"

        if player_index == 1:
            player = "player_1"

        else:
            player = "player_2"

        self._board.modify_board(player, pit_index)  # updates the board using the rules of the game.

        game_end = False

        player_1_seeds_in_pits = 0  # keeps track of seeds in pits for end of game.
        player_2_seeds_in_pits = 0

        if all(pit == 0 for pit in self._board.get_player_1_pits()):  # determines if game is over.
            game_end = True

            for pit in self._board.get_player_2_pits():  # sums the seeds remaining in the pits at end of game.
                player_2_seeds_in_pits += pit

        if all(pit == 0 for pit in self._board.get_player_2_pits()):  # determines if game is over.
            game_end = True

            for pit in self._board.get_player_1_pits():  # sums the seeds remaining in the pits at the end of game.
                player_1_seeds_in_pits += pit

        if game_end == True:  # updates the pits and stores at the end of the game.

            clear_board = [0, 0, 0, 0, 0, 0]
            self._board.set_player_1_pits(clear_board)
            self._board.set_player_2_pits(clear_board)
            self._board.set_player_1_store(player_1_seeds_in_pits)
            self._board.set_player_2_store(player_2_seeds_in_pits)

            if self._board.get_player_1_store() > self._board.get_player_2_store():  # game_state is updated.
                self._game_state = f"Winner is player 1: {self._player_1.get_name()}"

            elif self._board.get_player_2_store() > self._board.get_player_1_store():
                self._game_state = f"Winner is player 2: {self._player_2.get_name()}"

            else:
                self._game_state = "It's a tie"

        board_list = []                                                                     #list for pits and stores.

        for pit in self._board.get_player_1_pits():
            board_list.append(pit)

        board_list.append(self._board.get_player_1_store())

        for pit in self._board.get_player_2_pits():
            board_list.append(pit)

        board_list.append(self._board.get_player_2_store())

        return board_list

    def return_winner(self):
        """Returns the winner of the game using the game_state attribute."""

        return self._game_state

