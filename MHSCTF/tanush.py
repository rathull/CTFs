import sys


def main(toppings):
    tmp = {
        "T": 1.5,
        "O": 1.25,
        "P": 3.5,
        "M": 3.75,
        "A": 0.4
    }
    possible_toppings = list(tmp.keys())
    toppings_used = []

    cost = 15
    for top in toppings:
        if(top in possible_toppings):
            if(top not in toppings_used):
                cost += tmp[top]
                toppings_used.append(top)
            else:
                continue
        else:
            continue
    if(cost > 15):
        print(round(cost * 0.95, 2))
    else:
        print(cost)
for i in range(7):
    x = input()
    while x == '\n' or x == '':
        x = input()
    # print(repr(x))
    main(x)