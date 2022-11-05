import random

def rain():
    return "."

def space():
    return " "

rain_or_space = [rain(), space()]


def rain_or_space_function():
    rain_str = ""
    for i in range(random.choice(range(10, 101))):
        rain_str += random.choice(rain_or_space)
    return rain_str


def runner():
    for i in range(random.choice(range(20000, 2000000))):
        print(rain_or_space_function())

if __name__ == "__main__":
    runner()





