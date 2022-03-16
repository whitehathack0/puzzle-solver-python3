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


def is_goal(current_node):
    length = len(current_node.board)

    for row_index, row in enumerate(current_node.board):
        for col_index, point in enumerate(row):
            if row_index*length + col_index != current_node.board[row_index][col_index]:
                return False
    return True


def go_up(current_node, zero_pos_x, zero_pos_y) -> Node:
    move_up_node = current_node

    if zero_pos_x - 1 < 0:
        return None
    else:
        above_val = current_node.board[zero_pos_x-1][zero_pos_y]
        move_up_node.board[zero_pos_x][zero_pos_y] = above_val
        move_up_node.board[zero_pos_x - 1][zero_pos_y] = 0
        return move_up_node


def go_down(current_node, zero_pos_x, zero_pos_y) -> Node:
    move_down_node = current_node

    if zero_pos_x + 1 >= len(current_node.board):
        return None
    else:
        below_val = current_node.board[zero_pos_x + 1][zero_pos_y]
        move_down_node.board[zero_pos_x][zero_pos_y] = below_val
        move_down_node.board[zero_pos_x + 1][zero_pos_y] = 0
        return move_down_node


def go_left(current_node, zero_pos_x, zero_pos_y) -> Node:
    move_left_node = current_node

    if zero_pos_y - 1 < 0:
        return None
    else:
        left_val = current_node.board[zero_pos_x][zero_pos_y - 1]
        move_left_node.board[zero_pos_x][zero_pos_y] = left_val
        move_left_node.board[zero_pos_x][zero_pos_y - 1] = 0
        return move_left_node


def go_right(current_node, zero_pos_x, zero_pos_y) -> Node:
    move_right_node = current_node

    if zero_pos_y + 1 >= len(current_node.board):
        return None
    else:
        right_val = current_node.board[zero_pos_x][zero_pos_y + 1]
        move_right_node.board[zero_pos_x][zero_pos_y] = right_val
        move_right_node.board[zero_pos_x][zero_pos_y + 1] = 0
        return move_right_node


def bfs(start_node):
    node_queue = [start_node]
    counter = 0

    while node_queue:
        current_node = node_queue.pop()
        if counter == 100000:
            return "1000WASREACHED"
        else:
            counter += 1

        if is_goal(current_node):
            return current_node.path

        break_out_flag = False
        for row_index, row in enumerate(current_node.board):
            for col_index, point in enumerate(row):
                if point == 0:
                    break_out_flag = True
                    zero_pos_x = row_index
                    zero_pos_y = col_index
                    break
            if break_out_flag:
                break

        move_up_node = go_up(current_node, zero_pos_x, zero_pos_y)
        if move_up_node and move_up_node.board:
            move_up_node.path += current_node.to_string()
            node_queue.append(move_up_node)

        move_down_node = go_down(current_node, zero_pos_x, zero_pos_y)
        if move_down_node and move_down_node.board:
            move_down_node.path += current_node.to_string()
            node_queue.append(move_down_node)

        move_left_node = go_left(current_node, zero_pos_x, zero_pos_y)
        if move_left_node and move_left_node.board:
            move_left_node.path += current_node.to_string()
            node_queue.append(move_left_node)

        move_right_node = go_right(current_node, zero_pos_x, zero_pos_y)
        if move_right_node and move_right_node.board:
            move_right_node.path += current_node.to_string()
            node_queue.append(move_right_node)


if __name__ == '__main__':
    with open('resources/easy_test.txt') as f:
        lines = f.readlines()
        length = len(lines[0].split())

    start_board = [[0 for i in range(length)] for j in range(length)]

    for row_index, row in enumerate(lines):
        for col_index, point in enumerate(row.split()):
            if point == '.':
                start_board[row_index][col_index] = 0
            else:
                start_board[row_index][col_index] = int(point)

    start_state = Node(start_board, '')
    goal_path = bfs(start_state)
    print(goal_path)
