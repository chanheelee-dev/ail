import numpy as np
import matplotlib.pyplot as plt


def define_rng(random_seed=8927):
    return np.random.default_rng(random_seed)


rng = define_rng()


def sample_xy(intercept_gen, slope_gen, sample_size=100):
    x = np.linspace(0, 1, sample_size)

    # y = b + a*x + Norm(0, 0.5)
    line_gen = intercept_gen + slope_gen * x
    y = line_gen + rng.normal(scale=0.5, size=sample_size)

    return x, y, line_gen


def plot_xy(x, y, model):
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(
        111, xlabel="x", ylabel="y", title="Generated data and unerlying model"
    )
    ax.plot(x, y, "x", label="sampled data")
    ax.plot(x, model, label="true regression line", lw=2.0)
    plt.legend(loc=0)
    return fig
