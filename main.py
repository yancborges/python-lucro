from random import randint
from values import Value

def gen_list(size=None):

    if not size:
        size = randint(5, 365)

    return [Value(r, randint(1, 10)) for r in range(size)]


def get_best_sell(_list, buy_day):

    # Logic:
    #
    # A list index is choosen (buy_day)
    # So i sort the list remaining (after the buy day) 
    # 
    # [1, 5, 8, 2, 5, 3, 6]
    #       [8] Buy day
    #          [2, 5, 3, 6] Possible days for selling
    #          [2, 3, 5, 6] Sorted (used quick sort there)
    # 
    # With list sorted, i know the last index has the highest price,
    # Then, i just need to get the exchange value
    # 
    # exchange = sell_price - buy_price


    if buy_day >= len(_list) or buy_day < 0:
        raise IndexError('Buy day must be within day list range')

    possible_sells = _list[buy_day:]
    possible_sells = sort_list(possible_sells)

    return _list[buy_day], possible_sells[-1]


def sort_list(_list):

    # Quick sort here
    lower_index = 0
    lower_obj = _list[lower_index]
    for i in _list:
        curr_index = _list.index(i)
        lower_index = curr_index
        lower_obj = _list[lower_index]
        for j in _list[curr_index:]:

            if j.price < lower_obj.price:
                lower_index = _list.index(j)
                lower_obj = j

        dummy = _list[lower_index]
        _list[lower_index] = _list[curr_index]
        _list[curr_index] = dummy


    return _list


def run():

    # A list size can be used here, get_list(size=10)
    _list = gen_list()
    print('When did you buy?')
    for item in _list:
        print(item)

    buy_day = input('Buy day: ')
    if not buy_day.isdigit():
        raise ValueError('Day must be a number')

    buy_day = int(buy_day)
    buy_obj, sell_obj = get_best_sell(_list, buy_day)

    exchange = sell_obj.price - buy_obj.price

    print('\nBought at day #{} for ${}'.format(buy_obj.day, buy_obj.price))
    if exchange > 0:
        print('Best sell day is #{}, price: ${}'.format(sell_obj.day, sell_obj.price))
        print('Exchange: {}'.format(exchange))
    else:
        print('No possible exchange :(')


run()

            

