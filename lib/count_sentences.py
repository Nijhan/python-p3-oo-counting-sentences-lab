import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # use setter for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.') if self.value else False

    def is_question(self):
        return self.value.endswith('?') if self.value else False

    def is_exclamation(self):
        return self.value.endswith('!') if self.value else False

    def count_sentences(self):
        # Match one or more sentence-ending punctuation marks as one sentence
        return len(re.findall(r'[.!?]+', self.value))
