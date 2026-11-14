SIZE_X = 4
SIZE_Y = 2
BASE_SURVIVE_POINTS = 20


storaged_item = {'name': 'i', 'price': 5, 'cells': 1}
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

max_sum = sum(x['price'] for x in items.values())



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


def gen_inventory(size_x, size_y, items, storaged_items):
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
                    inventory[line][cell] = f'[{item}]'
                filled += items_temp[item]
                used.append(item)

        for item in used:
            del items_temp[item]

    return inventory


def draw_result(size_x=SIZE_X, size_y=SIZE_Y, 
                items=items, storaged_item=storaged_item, 
                base_survive_points=BASE_SURVIVE_POINTS):
    res_sum, storaged_items = gen_table_memo(items, 
                                size_x*size_y - storaged_item['cells'])

    items[storaged_item['name']] = dict()
    items[storaged_item['name']]['price'] = storaged_item['price']
    items[storaged_item['name']]['cells'] = storaged_item['cells']
    storaged_items.add(storaged_item['name'])
    
    inventory = gen_inventory(size_x, size_y, items, storaged_items)

    res_points = base_survive_points + 2*res_sum - max_sum
    if res_points > 0:
        print('Итоговые очки выживания:', res_points)
        for line in inventory:
            print(*line, sep=',')
    else:
        print('Err')


if __name__ == '__main__':
    draw_result(7, 1)