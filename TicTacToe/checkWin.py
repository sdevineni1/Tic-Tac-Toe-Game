#  -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 08:45:20 2019

@author: Samuel Fisher, Intern
Johns Hopkins University Applied Physics Laboratory
"""

import copy

# Display who won and add to win counter
def whoWin(x, End, Xwin, Owin):
    Xwin = 0
    Owin = 0
    if x == 1:
        End.configure(text="Player 1 has won!", background='white')
        Xwin = 1
    elif x == 2:
        End.configure(text="Player 2 has won!", background='white')
        Owin = 1
    else:
        End.configure(text="Nobody Wins", background='white')
    gameover = 1
    L = [Xwin, Owin, gameover]
    return L


# Check if there is a three in a row
# If there is a win, a display which team one and count that win
def checkWin(place, AIturn, End, Xwin, Owin, turn, aiSkill):
    if place[1] == place[0] and place[0] == place[2] and place[1] != 0:
        print("Player", place[1], " wins")
        return whoWin(place[1], End, Xwin, Owin)
    if place[0] == place[3] and place[0] == place[6] and place[0] != 0:
        print("Player", place[0], " wins")
        return whoWin(place[0], End, Xwin, Owin)
    if place[0] == place[4] and place[0] == place[8] and place[0] != 0:
        print("Player", place[0], " wins")
        return whoWin(place[0], End, Xwin, Owin)
    if place[1] == place[4] and place[1] == place[7] and place[1] != 0:
        print("Player" , place[1], " wins")
        return whoWin(place[1], End, Xwin, Owin)
    if place[2] == place[4] and place[2] == place[6] and place[2] != 0:
        print("Player", place[2], " wins")
        return whoWin(place[2], End, Xwin, Owin)
    if place[2] == place[5] and place[2] == place[8] and place[2] != 0:
        print("Player", place[2], " wins")
        return whoWin(place[2],End,Xwin,Owin)
    if place[3] == place[4] and place[3] == place[5] and place[3] != 0:
        print("Player", place[3], " wins")
        return whoWin(place[3],End,Xwin,Owin)
    if place[6] == place[7] and place[8] == place[6] and place[6] != 0:
        print("Player", place[6], " wins")
        return whoWin(place[7], End, Xwin, Owin)
    tie = 1
    for i in place:
        if i == 0:
            tie = 0
    if tie == 1:
        return whoWin(3, End, Xwin, Owin)
        
    return [0, 0, 0]


# Check who won without calling whoWin
# Necessary for MiniMax
def checkWin2(place):
    if place[1] == place[0] and place[0] == place[2] and place[1] != 0:
        return place[1]
    if place[0] == place[3] and place[0] == place[6] and place[0] != 0:
        return place[0]
    if place[0] == place[4] and place[0] == place[8] and place[0] != 0:
        return place[0]
    if place[1] == place[4] and place[1] == place[7] and place[1] != 0:
        return place[1]
    if place[2] == place[4] and place[2] == place[6] and place[2] != 0:
        return place[2]
    if place[2] == place[5] and place[2] == place[8] and place[2] != 0:
        return place[2]
    if place[3] == place[4] and place[3] == place[5] and place[3] != 0:
        return place[3]
    if place[6] == place[7] and place[8] == place[6] and place[6] != 0:
        return place[6]

    # tie logic
    tie = 1
    for i in place:
        if i == 0:
            tie = 0
    if tie == 1:
        return 0
        
    return [0, 0, 0]

# Checks and returns the available indices
# where the next move can be executed.
def available_moves(place):
    available_move_count_index_list = []
    index = 0
    for i in place:
        if i == 0:
            available_move_count_index_list.append(index)

        index += 1

    return available_move_count_index_list


# Calculates the score of a possible win(10 points).
def calculate_score(place, depth):
    if checkWin2(place) == 1:
        score = depth - 10
    elif checkWin2(place) == 2:
        score = 10 - depth
    else:
        score = 0
    return score


def minmax(place, depth, player):
    if checkWin2(place) != [0, 0, 0]:
        return calculate_score(place, depth), 1

    depth += 1
    scores = []
    moves = []

    available_move_index_list = available_moves(place)

    for available_move_index in available_move_index_list:
        place_child = perform_move(place, available_move_index, player)

        # Get place child score:
        if player == 1:  # Maximizing player
            next_player = 2
        else:  # Minimizing player
            next_player = 1

        score, index = minmax(place_child, depth, next_player)
        scores.append(score)
        moves.append(available_move_index)

    max_score_index = moves[scores.index(max(scores))]
    min_score_index = moves[scores.index(min(scores))]
    ret_val = [max(scores), max_score_index] if player == 2 else [min(scores), min_score_index]
    return ret_val


def perform_move(place, position, player):
    place_copy = copy.deepcopy(place)
    place_copy[position] = player
    return place_copy

# Check possibilities for wins in the next move
def checkWinPos(place, player):
   # Create checkWinPos here

   return None