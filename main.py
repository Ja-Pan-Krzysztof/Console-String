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
            color_char: str = 'white',
            rows: int = 1
    ):
        self.col: int = self.columns
        self.rows = rows
        self.my_string = my_string
        self.char = char
        self.color_str = color_str
        self.color_char = color_char

    def start_code(self):
        # Colors :

        self.color_char = colors.get(self.color_char)
        self.color_str = colors.get(self.color_str)

        # Columns :

        self.col = self.col - len(self.my_string)

        if self.col % 2 == 0:
            col_l = self.col / len(self.char * 2) - 1
            col_r = self.col / len(self.char * 2) - 1

        else:
            col_l = int(self.col / len(self.char * 2) + 0.5) - 1
            col_r = int(self.col / len(self.char * 2) - 0.5) - 1

        col_l = self.char * int(col_l)
        col_r = self.char * int(col_r)
        # Rows :

        if self.rows % 2 == 0:
            if self.rows == 2:
                row_1 = 0
                row_2 = 1

            else:
                row_1 = int(self.rows / 2 - 1)
                row_2 = int(self.rows / 2)

        else:
            row_1 = int(self.rows / 2 - 0.5)
            row_2 = int(self.rows / 2 - 0.5)

        row_t = (self.char * self.columns + '\n') * row_1
        row_b = ('\n' + self.char * self.columns) * row_2

        print(f'{self.color_char}{row_t}{col_l} {self.color_str}{self.my_string} {self.color_char}{col_r}{row_b}\033[0m')


code = Code(color_char='blue', rows=50)
code.start_code()


