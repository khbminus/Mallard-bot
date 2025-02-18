import random
from content.dictionaries import BASIC_REPLIES_DICT, RANDOM_RESPONCES_DICT, RANDOM_STICKERS


class Mallard:
    """
    Replies to stuff.
    """

    def __init__(self, random_answer_rate=200):
        self.RANDOM_ANSWER_RATE = random_answer_rate
        pass

    def process(self, saying: str):
        """
        :param saying:
        """
        if len(saying) == 0:
            return None, False
        if (reply := self.check_basic_saying_based_on_dict(saying, BASIC_REPLIES_DICT)) is not None:
            return reply, False
        if (reply := self.generate_random_answer()) is not None:
            return reply

    @staticmethod
    def check_basic_saying_based_on_dict(saying: str, basic_dict):
        """
        Checks if saying has some basic words to reply (like "ква").
        :param saying:
        """
        saying = saying.upper()
        found_keywords = []
        for keyword in basic_dict.keys():
            if (upper := keyword.upper()) in saying and len(basic_dict[keyword]) > 0:
                found_keywords.append(upper)

        if (l := len(found_keywords)) > 0:
            chosen_keyword = found_keywords[random.randint(0, l - 1)]
            return basic_dict[chosen_keyword][random.randint(0, len(basic_dict[chosen_keyword]) - 1)]
        return None

    def generate_random_answer(self):
        """
        says random stuff
        :return:
        """
        if random.randint(0, self.RANDOM_ANSWER_RATE) == 0:
            if random.randint(0, 2) == 0:
                random.shuffle(RANDOM_RESPONCES_DICT)
                return RANDOM_RESPONCES_DICT[random.randint(0, len(RANDOM_RESPONCES_DICT) - 1)], False
            else:
                random.shuffle(RANDOM_STICKERS)
                return RANDOM_STICKERS[random.randint(0, len(RANDOM_STICKERS) - 1)], True
        return None, False
