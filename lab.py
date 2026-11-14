SIZE_X = 4
SIZE_Y = 2

storaged_item = {'price': 5, 'cells': 1}
items = {
    'r': {'price': 25, 'cells': 3},
    'p': {'price': 15, 'cells': 2},
    'a': {'price': 15, 'cells': 2},
    'm': {'price': 20, 'cells': 2},
    'k': {'price': 15, 'cells': 1},
    'x': {'price': 20, 'cells': 3},
    't': {'price': 25, 'cells': 1},
    'f': {'price': 15, 'cells': 1},
    'd': {'price': 10, 'cells': 1},
    's': {'price': 20, 'cells': 2},
    'c': {'price': 20, 'cells': 2}
}


def gen_table_memo(items, max_cells):
    table = [[[0, set()] for _ in range(max_cells)] for _ in range(len(items))]

    for row, item in enumerate(items):
        price = items[item]['price']
        cells = items[item]['cells']

        for col, current_limit in enumerate(range(1, max_cells+1)):
            if row == 0:
                if cells <= current_limit:
                    table[row][col][0] = price
                    table[row][col][1] = set(item)
                continue

            prev_price = table[row-1][col][0]

            if cells > current_limit:
                table[row][col] = table[row-1][col].copy()

            elif cells == current_limit:
                if price >= prev_price:
                    table[row][col][0] = price
                    table[row][col][1] = set(item)
                else:
                    table[row][col] = table[row-1][col].copy()

            else:
                price_rest = table[row-1][col-cells][0]

                if price_rest+price >= prev_price:
                    table[row][col][0] = price_rest+price
                    table[row][col][1] = set(item) | table[row-1][col-cells][1]
                else:
                    table[row][col] = table[row-1][col].copy()
    return table[-1][-1]


def draw_inventory(size_x, size_y, items, storaged_items):
    inventory = [[[] for _ in range(size_x)] for _ in range(size_y)]
    items_temp = dict()
    for item in storaged_items:
        items_temp[item] = items[item]['cells']

    pos = 0
    for line in range(size_y):
        filled = 0
        used = []
        for item in items_temp:
            if items_temp[item] <= size_x - filled:
                for cell in range(size_x - filled):
                    inventory[line][cell] = item
                filled += items_temp[item]
                used.append(item)

        for item in used:
            del items_temp[item]

    return inventory


if __name__ == '__main__':
    max_sum, storaged_items = gen_table_memo(items, SIZE_X*SIZE_Y - storaged_item['cells'])
    print(max_sum, storaged_items)
    print(draw_inventory(SIZE_X, SIZE_Y, items, storaged_items))