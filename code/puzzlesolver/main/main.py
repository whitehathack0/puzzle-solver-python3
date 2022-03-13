class Node:

    def __init__(self, board, path):
        self.board = board
        self.path = path

    def to_string(self):
        path_str = ''
        for row in self.board:
            for item in row:
                path_str += str(item)
            path_str += '\n'
        return path_str


def bfs(board):
    pass


if __name__ == '__main__':
    with open('resources/test.txt') as f:
        lines = f.readlines()
        length = len(lines[0].split())

    start_board = [[0 for i in range(length)] for j in range(length)]

    for row_index, row in enumerate(lines):
        for col_index, point in enumerate(row.split()):
            if point == '.':
                start_board[row_index][col_index] = 0
            else:
                start_board[row_index][col_index] = int(point)

    start_state = Node(start_board, "")
    goal_state = bfs(start_state)
