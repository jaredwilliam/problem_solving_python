import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()


def generate_single_guess(pool: list) -> str:
    return random.choice(pool)


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


def score_simulation(guesses: list, answer: list) -> list:
    # average percent of correct characters
    pct_correct_per_sim = []
    for guess in guesses:
        pct_correct_per_sim.append(score_guess(guess, answer))
    return pct_correct_per_sim


def variance(scores: list) -> float:
    return np.var(scores)


def stdDev(scores: list) -> float:
    return np.std(scores)


def plot_pct_correct_vs_sim(scores: list) -> None:
    fig, ax = plt.subplots()
    ax.scatter(range(len(scores)), scores)
    plt.show()


def plot_histogram(scores: list) -> None:

    # Freedman-Diaconis Rule for bins
    max_value = max(scores)
    min_value = min(scores)
    n = len(scores)
    iqr = np.subtract(*np.percentile(scores, [75, 25]))
    h = 2 * iqr * n ** (-1 / 3)
    bins = int((max_value - min_value) / h)

    fig, ax = plt.subplots()
    ax.hist(scores, bins=bins)
    plt.show()


def hill_climb_guessing(pool: list, target: str, guess_results_list: bool = False):
    final_solution = []
    guess_results = []
    target_index = 0

    while len(final_solution) < len(target):
        guess = generate_single_guess(pool)

        if guess == target[target_index]:
            guess_results.append(1)
            final_solution.append(guess)
            target_index += 1
        else:
            guess_results.append(0)

    if guess_results_list:
        return guess_results
    else:
        return len(guess_results)


def hill_climb_simulation(
    pool: list, target: str, num_sims: int = 1, guess_results_list: bool = False
) -> list:
    guess_counts = []

    for _ in range(num_sims):
        guess_counts.append(hill_climb_guessing(pool, target, guess_results_list))

    return guess_counts


def calc_cumulative_correct_guesses(guesses: list) -> list:
    # Needed because the sublists are not guaranteed to be the same size
    result = []

    for guess_list in guesses:
        result.append(np.cumsum(guess_list))
    return result


def plot_cumlative_correct_guesses(guesses: list) -> None:

    # x_axis_len = 0
    # for guess_list in guesses:
    #     if len(guess_list) > x_axis_len:
    #         x_axis_len = len(guess_list)

    fig, ax = plt.subplots()
    for guess in guesses:
        ax.step(
            range(len(guess)), guess, where="post", color="cornflowerblue", alpha=0.5
        )
    plt.show()


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

    # guesses = simulate_guesses(pool=pool, length=target_len, num_sims=1000)
    # simulation_scores = score_simulation(guesses, target)
    # plot_pct_correct_vs_sim(simulation_scores)
    # plot_histogram(simulation_scores)
    # plot_histogram(hill_climb_guesses)

    # * Hill Climbing
    hill_climb_guesses = hill_climb_simulation(pool, target, 1000, True)
    cumulative_guesses = calc_cumulative_correct_guesses(hill_climb_guesses)
    # for cum_guess in cumulative_guesses:
    #     print(cum_guess)
    # cumulative_sums = np.cumsum(hill_climb_guesses, axis=1)

    plot_cumlative_correct_guesses(cumulative_guesses)
