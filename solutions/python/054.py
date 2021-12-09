"""
    Problem 54
    ==========
    
    
    In the card game poker, a hand consists of five cards and are ranked, from
    lowest to highest, in the following way:
    
    • High Card: Highest value card.
    • One Pair: Two cards of the same value.
    • Two Pairs: Two different pairs.
    • Three of a Kind: Three cards of the same value.
    • Straight: All cards are consecutive values.
    • Flush: All cards of the same suit.
    • Full House: Three of a kind and a pair.
    • Four of a Kind: Four cards of the same value.
    • Straight Flush: All cards are consecutive values of same suit.
    • Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    
    The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
    
    If two players have the same ranked hands then the rank made up of the
    highest value wins; for example, a pair of eights beats a pair of fives
    (see example 1 below). But if two ranks tie, for example, both players
    have a pair of queens, then highest cards in each hand are compared (see
    example 4 below); if the highest cards tie then the next highest cards are
    compared, and so on.
    
    Consider the following five hands dealt to two players:
    
    Hand   Player 1            Player 2              Winner
    1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
    Pair of Fives       Pair of Eights
    2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
    Highest card Ace    Highest card Queen
    3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
    Three Aces          Flush with Diamonds
    4D 6S 9H QH QC      3D 6D 7H QD QS
    4      Pair of Queens      Pair of Queens        Player 1
    Highest card Nine   Highest card Seven
    2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
    5      Full House          Full House            Player 1
    With Three Fours    with Three Threes
    
    The file, [1]poker.txt, contains one-thousand random hands dealt to two
    players. Each line of the file contains ten cards (separated by a single
    space): the first five are Player 1's cards and the last five are Player
    2's cards. You can assume that all hands are valid (no invalid characters
    or repeated cards), each player's hand is in no specific order, and in
    each hand there is a clear winner.
    
    How many hands does Player 1 win?
    
    
    Visible links
    1. poker.txt
    Answer: 142949df56ea8ae0be8b5306971900a4
"""
import os
from common import check

FILE_NAME = "p054_poker.txt"
PROBLEM_NUMBER = 54
ANSWER_HASH = "142949df56ea8ae0be8b5306971900a4"

ROYAL_FLUSH = 9
STRAIGHT_FLUSH = 8
FOUR_OF_A_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_A_KIND = 3
TWO_PAIRS = 2
ONE_PAIR = 1
HIGH_CARD = 0

CARDS = "AKQJT98765432"

def load_hands(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        all_cards = [[card.strip() for card in line.split(" ")] for line in lines]
        return [[cards[:5], cards[5:]] for cards in all_cards]

def get_suits(hand):
    return set((card[1] for card in hand))

def get_cards(hand):
    return [card[0] for card in hand]

def is_flush(hand):
    return len(get_suits(hand)) == 1 

def get_straight(hand):
    cards = get_cards(hand)
    for i, c in enumerate(CARDS[:9]):
        if c in cards:
            for j in range(1, 5):
                if CARDS[i+j] not in cards:
                    return None
            return c
    return None

def get_group(hand):
    cards = get_cards(hand)
    amounts = { c : sum(1 for i in cards if i == c) for c in set(cards) }
    four = next((k for k, v in amounts.items() if v == 4), None)
    if four:
        return (FOUR_OF_A_KIND, four)
    three = next((k for k, v in amounts.items() if v == 3), None)
    pair_gen = (k for k, v in amounts.items() if v == 2)
    pair_a = next(pair_gen, None)
    if three is not None:
        if pair_a is not None:
            return (FULL_HOUSE, three)
        return (THREE_OF_A_KIND, three)
    pair_b = next(pair_gen, None)
    if pair_a is None and pair_b is None:
        high_card = CARDS[min(CARDS.index(c) for c in set(cards))]
        return (HIGH_CARD, high_card)
    elif pair_b is None:
        return (ONE_PAIR, pair_a)
    else:
        pair_a_rank = CARDS.index(pair_a)
        pair_b_rank = CARDS.index(pair_b)
        return (TWO_PAIRS, CARDS[min(pair_a_rank, pair_b_rank)])

def get_rank(hand):
    straight = get_straight(hand)
    flush = is_flush(hand)
    if flush and straight is not None:
        if straight == "A":
            return (ROYAL_FLUSH)
        else:
            return (STRAIGHT_FLUSH, straight)

    group = get_group(hand)
    if group[0] == FOUR_OF_A_KIND:
        return group
    
    if flush:
        return (FLUSH,)
    if straight is not None:
        return (STRAIGHT, straight)
    return group

player_1_score = 0
player_2_score = 0

def get_score(card):
    return CARDS.index(card)    

def compare(hand_a, hand_b):
    rank_a = get_rank(hand_a)
    rank_b = get_rank(hand_b)

    if rank_a[0] != rank_b[0]:
        return -1 if rank_a[0] > rank_b[0] else 1
    else:
        for i in range(len(rank_a)-1):
            card_a = rank_a[1+i]
            card_b = rank_b[1+i]
            if card_a == card_b:
                continue
            return -1 if get_score(card_a) < get_score(card_b) else 1
        
        # compare high cards
        hand_a.sort(key=lambda card: get_score(card[0]))
        hand_b.sort(key=lambda card: get_score(card[0]))
        for i in range(5):
            card_a = hand_a[i][0]
            card_b = hand_b[i][0]
            if card_a == card_b:
                continue
            return -1 if get_score(card_a) < get_score(card_b) else 1

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), FILE_NAME)
    hands = load_hands(file_path)
    player_1 = sum(1 for hand_a, hand_b in hands if compare(hand_a, hand_b) < 0)
    check(player_1, PROBLEM_NUMBER, ANSWER_HASH)
