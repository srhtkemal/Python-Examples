import random


def shuffle_by_adding_end_of_list(input_list: list) -> list:
    for i in range(len(input_list)):
        random_index = random.randint(0, len(input_list) - 1)
        element = input_list.pop(random_index)
        input_list.append(element)
    return input_list


def shuffle_as_new_list(input_list: list) -> list:
    new_list = []
    while input_list:
        random_index = random.randint(0, len(input_list)-1)
        element = input_list.pop(random_index)
        new_list.append(element)
    return new_list


def share_cards_among_x_players(x, shuffled_list):

    cards_of_all_players = {}
    for i in range(x):
        cards = []

        for j in range(len(shuffled_list)//x):

            cards.append(shuffled_list[j*x+i])
        cards_of_all_players[f'player_{i+1}'] = cards
    return cards_of_all_players


def score_to_grouped_card(card: int) -> str:
    if (card > 51 or card < 0):
        return "Invalid Card"
    if (card > 47):
        card -= 52  # it is -52 bc when we divide by 4, it gives us extra -1; so when we add +2, it will appear as +1
    if ((card) % 4 == 0):  # card//4+1 bc index starts at 0.  0=>C2, 3=>S2
        return f"C{card//4+2}"  # Clubs
    elif ((card) % 4 == 1):
        return f"D{card//4+2}"  # Diamonds
    elif ((card) % 4 == 2):
        return f"H{card//4+2}"  # Hearts
    elif (card % 4 == 3):
        return f"S{card//4+2}"  # Spades
    else:
        return "Unidentified Card"


def grouped_card_to_score(grouped_card: str) -> int:
    group = grouped_card[0]  # C4, D10, H5, S11 etc.
    rank = int(grouped_card[1:])
    if (rank < 1 or rank > 13):
        return -1
    if (rank == 1):
        rank = 14  # bc of the table below
    if (group == 'C'):
        return (rank-2)*4
    elif (group == 'D'):
        return (rank-2)*4 + 1
    elif (group == 'H'):
        return (rank-2)*4 + 2
    elif (group == 'S'):
        return (rank-2)*4 + 3
    else:
        return -1
    # Clubs, Diamonds, Hearts, Spades
    # 0: C2,   1: D2,  2: H2,   3: S2
    # 4: C3,   5: D3,  6: H3,   7: S3,
    # 8: C4,   9: D4, 10: H4,  11: S4,
    # ...
    # 40: C12, 41: D12, 42:H12, 43:S12,
    # 44: C13, 45: D13, 46:H13, 47:S13,
    # 48: C1,  49: D1,  50:H1,  51:S1
    # Aces are the strongest


# Testing the functions

not_shuffeled_deck = [i for i in range(52)]  # 0-51
shuffled_deck_as_new_list = shuffle_as_new_list(not_shuffeled_deck.copy())
shuffled_deck_by_adding_end_of_list = shuffle_by_adding_end_of_list(
    not_shuffeled_deck.copy())
print("Not Shuffled Deck: ", not_shuffeled_deck)
print("\nShuffled Deck as New List: ", shuffled_deck_as_new_list)
print("\nShuffled Deck by Adding End of List: ",
      shuffled_deck_by_adding_end_of_list)
print("\nShared Cards among 13 players: ",
      share_cards_among_x_players(13, shuffled_deck_as_new_list.copy()))

print("\nGrouped Card of score 48: ", score_to_grouped_card(48))
print("\nGrouped Card of score 11: ", score_to_grouped_card(11))
print("\nGrouped Card of score  1: ", score_to_grouped_card(1))
print("\nScore of grouped card S3: ", grouped_card_to_score("S3"))
print("\nScore of grouped card H5: ", grouped_card_to_score("H5"))
print("\nScore of grouped card S1: ", grouped_card_to_score("S1"))
