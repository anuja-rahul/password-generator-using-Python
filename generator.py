import random
import string


class PasswordGenerator:

    __LEVELS = [1, 2, 3, 4]

    def __init__(self, length: int = 25, level: int = 4):
        self.__length = length
        if level in PasswordGenerator.__LEVELS:
            self.__level = level
        else:
            raise Exception("Level out of range !")

    def get_password(self):
        password = ""

        if self.__level == 1:
            password = self.__loop_password(0)
        elif self.__level == 2:
            password = self.__loop_password(1)
        elif self.__level == 3:
            password = self.__loop_password(2)
        elif self.__level == 4:
            password = self.__loop_password(3)

        return password

    def __loop_password(self, method: int):
        password = ""
        length = self.__length
        types = [self.__get_lowercase_letters, self.__get_uppercase_letters,
                 self.__get_numbers, self.__get_special_characters]

        while length != 0:
            password += types[random.randint(0, method)]()
            length -= 1
        return password

    @staticmethod
    def __get_lowercase_letters():
        return random.choice(string.ascii_lowercase)

    @staticmethod
    def __get_uppercase_letters():
        return random.choice(string.ascii_uppercase)

    @staticmethod
    def __get_special_characters():
        special_char = "!@#$%^&*()_+{}[]<>?/~"
        return random.choice(special_char)

    @staticmethod
    def __get_numbers():
        return str(random.randint(0, 10))
