import random


class Card:
    """ A class to describe cards in a pack """
    def __init__(self, number):
        self._card_number = number

    def get_suit(self):
        """ return a string 'C', 'S', 'H', 'D' """
        if self._card_number <= 12:
            return "S"
        elif self._card_number >= 13 and self._card_number <= 25:
            return "H"
        elif self._card_number >= 26 and self._card_number <= 38:
            return "D"
        elif self._card_number >= 39 and self._card_number <= 51:
            return "C"
        else:
            return ValueError
        pass

    def get_value(self):
        """ return a string 'A'..'10', 'J', 'Q', 'K' """
        if self._card_number % 13 == 0:
            return "A"
        elif self._card_number % 13 == 1:
            return "2"
        elif self._card_number % 13 == 2:
            return "3"
        elif self._card_number % 13 == 3:
            return "4"
        elif self._card_number % 13 == 4:
            return "5"
        elif self._card_number % 13 == 5:
            return "6"
        elif self._card_number % 13 == 6:
            return "7"
        elif self._card_number % 13 == 7:
            return "8"
        elif self._card_number % 13 == 8:
            return "9"
        elif self._card_number % 13 == 9:
            return "10"
        elif self._card_number % 13 == 10:
            return "J"
        elif self._card_number % 13 == 11:
            return "Q"
        elif self._card_number % 13 == 12:
            return "K"
        pass

    def get_short_name(self):
        """ return card name eg '10D' '8C' 'AH' """
        pass

    def get_long_name(self):
        """ return card name eg 'Ten of Diamonds' """
        pass


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self):
        """ returns the number of cards still in the deck """
        pass

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        """ removes the top card from the deck and returns it (as a card object) """
        pass

    def add_card(self, new_card):
        """ add a card to the bottom of the deck """
        self._card_list.append(new_card)


card = Card(1)
print(card.get_suit())
deck = Deck()
deck.shuffle_deck()
for _ in range(deck.length()):
    card = deck.take_top_card()
    print(card.get_long_name())