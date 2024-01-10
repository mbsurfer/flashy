from flashy_model import FlashyModel
import random


class FlashyController:
    def __init__(self):
        self.model = FlashyModel()

    def get_random_card(self):
        """Returns a random word pairing in the format
        {'French': 'partie', 'English': 'part'}
        """
        words = self.model.get_words()
        if len(words):
            return random.choice(words)
        else:
            return None

    def remove_card(self, card):
        self.model.delete(card)

    def get_word_count(self):
        return len(self.model.get_words())
