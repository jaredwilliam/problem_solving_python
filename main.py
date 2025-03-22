import random


def generate_guess(pool: list, length: int) -> list:
    guess = random.choices(pool, k=length)
    return guess


def simulate_guesses(pool: list, length: int, num_sims: int = 1) -> list:
    guesses = []
    for i in range(num_sims):
        guesses.append(generate_guess(pool, length))
    return guesses


def score_guess(guess: list, answer: list) -> float:
    length = len(answer)
    correct = 0
    for pair in list(zip(guess, answer)):
        if pair[0] == pair[1]:
            correct += 1
    return correct / length


def score_simulation(guesses: list, answer: list) -> float:
    # average percent of correct characters
    pct_correct_per_sim = []
    for guess in guesses:
        pct_correct_per_sim.append(score_guess(guess, answer))
    mean = sum(pct_correct_per_sim) / len(guesses)
    return mean


if __name__ == "__main__":

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

    target = "methinks it is like a weasel"

    target_len = len(target)

    guesses = simulate_guesses(pool=pool, length=target_len, num_sims=1000)
    print(score_simulation(guesses, target))

    # guess_limit = 10000

    # best_guess = None
    # best_score = 0

    # for i in range(guess_limit):
    #     guess = generate_guess(pool=pool, length=target_len)
    #     score = score_guess(guess, target)

    #     if score > best_score:
    #         best_guess = guess
    #         best_score = score
    # print(list(zip(best_guess, target)))
    # print(best_score)

    # target_as_list = [ch for ch in target]
    # zipped = list(zip(guess, target_as_list))

    # for i, pair in enumerate(zipped):
    #     if pair[0] == pair[1]:
    #         print(":)")
    #     else:
    #         print(":(")

    # for g_i, t_i in enumerate(zip(guess, target_as_list)):
    #     print(g_i, t_i)
