MAX_CELLS = 4
items = {
    'a': {'price': 700, 'cells': 3},
    'b': {'price': 300, 'cells': 1},
    'c': {'price': 500, 'cells': 2},
    'd': {'price': 550, 'cells': 2},
}


def gen_table_memo(items, max_cells=MAX_CELLS):
    table = [[0 for _ in range(max_cells)] for _ in range(len(items))]

    for row, item in enumerate(items.values()):
        price = item['price']
        cells = item['cells']

        for col, current_limit in enumerate(range(1, max_cells+1)):
            if row == 0:
                table[row][col] = 0 if cells > current_limit else price
                continue

            prev_price = table[row-1][col]

            if cells > current_limit:
                table[row][col] = prev_price
            elif cells == current_limit:
                table[row][col] = max(prev_price, price)
            else:
                price_rest = table[row-1][col-cells]
                table[row][col] = max(prev_price, price_rest+price)
    return table
                



if __name__ == '__main__':
    print(*gen_table_memo(items), sep='\n')