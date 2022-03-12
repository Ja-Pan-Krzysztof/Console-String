import os
from colors import colors

size = os.get_terminal_size()


class Code:
    columns = size.columns
    rows = size.lines

    def __init__(
            self,
            my_string: str = 'Start Code',
            char: str = '/',
            color_str: str = 'white',
            color_char: str = 'white'
    ):
        self.col: int = self.columns
        self.my_string = my_string
        self.char = char
        self.color_str = color_str
        self.color_char = color_char

    def start_code(self, color_str: str = None, color_char: str = None):

        if color_str is None:
            color_str = colors.get(self.color_str)

        else:
            color_str = colors.get(color_str)

        if color_char is None:
            color_char = colors.get(self.color_char)

        else:
            color_char = colors.get(color_char)

        self.col = self.col - len(self.my_string)

        if self.col % 2 == 0:
            row_l = self.col / len(self.char * 2) - 1
            row_r = self.col / len(self.char * 2) - 1

        else:
            row_l = int(self.col / len(self.char * 2) + 0.5) - 1
            row_r = int(self.col / len(self.char * 2) - 0.5) - 1

        row_l = self.char * int(row_l)
        row_r = self.char * int(row_r)

        print(f'{color_char}{row_l} {color_str}{self.my_string} {color_char}{row_r}\033[0m')


code = Code(color_char='blue')
code.start_code()


