class Direction:

    def __init__(self):
        self.__set(False, False, False, False)

    def __set(self, up, right, down, left):
        self.__up = up
        self.__right = right
        self.__down = down
        self.__left = left

    def up(self):
        self.__set(True, False, False, False)

    def right(self):
        self.__set(False, True, False, False)

    def down(self):
        self.__set(False, False, True, False)

    def left(self):
        self.__set(False, False, False, True)

    def get_up(self):
        return self.__up

    def get_right(self):
        return self.__right

    def get_down(self):
        return self.__down

    def get_left(self):
        return self.__left
