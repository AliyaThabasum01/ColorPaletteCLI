import random

def random_color():
    return "#" + "".join(random.choice("0123456789ABCDEF") for _ in range(6))

def generate_palette(count):
    return [random_color() for _ in range(count)]
