import random


def generate_guess(pool: list, length: int) -> str:
    generation = random.choices(pool, k=length)
    return generation
    # result = "".join(generation)
    # return result


def check_guess(guess: list, answer: list):
    length = len(answer)
    correct = 0
    for g_i, t_i in enumerate(zip(guess, answer)):

        pass


if __name__ == "__main__":

    target = "methinks it is like a weasel"

    pool = [
        " ",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    target_len = len(target)

    guess = generate_guess(pool=pool, length=target_len)

    # print(guess)
    # if guess == target:
    #     print(":)")
    # else:
    #     print(":(")

    target_as_list = [ch for ch in target]
    zipped = list(zip(guess, target_as_list))

    for item in zipped:
        print(item[0])
    # for g_i, t_i in enumerate(zip(guess, target_as_list)):
    #     print(g_i, t_i)
