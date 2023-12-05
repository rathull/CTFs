t = {
    'T': 1.5,
    'O': 1.25,
    'P': 3.5,
    'M': 3.75,
    'A': 0.4
}
for _ in range(7):
    toppings = "".join(set(input()))
    price = 15
    for c in toppings:
        if c in t.keys():
            price += t[c]
    if price > 20:
        price *= 0.95
    print(round(price, 2))