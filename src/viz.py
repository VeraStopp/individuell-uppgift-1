import matplotlib.pyplot as plt
import numpy as np

def plot_hist(df, column, bins=30, ylabel="Frequency"):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df[column], bins=bins, edgecolor="black")
    ax.set_title(f"Distibution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel(ylabel)
    ax.grid(axis="y")
    plt.tight_layout()
    plt.show()

def plot_box_by_group(df, column, group):
    fig, ax = plt.subplots(figsize=(8, 5))
    df.boxplot(column=column, by=group, ax=ax)
    ax.set_title(f"{column} per {group}")
    plt.suptitle("")
    ax.set_xlabel(group)
    ax.set_ylabel(column)
    plt.tight_layout()
    plt.show()

def plot_scatter(df, column1, column2):
    x = df[column1].to_numpy()
    y = df[column2].to_numpy()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(x, y)
    ax.set_title(f"{column1} vs. {column2}")
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.grid(True)
    return ax
    # k, m = np.polyfit(x, y, 1)
    # ix = np.argsort(x)
    # ax.plot(x[ix], (k*x + m)[ix], color="black")

def plot_bar_chart(df, column, ylabel="Frequency"):
    fig, ax = plt.subplots(figsize=(8, 5))
    counts = df[column].value_counts()
    counts.plot(kind="bar", color=["green", "red"], edgecolor="black", ax=ax)
    ax.set_title(f"Frequency of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel(ylabel)
    ax.grid(axis="y")
    plt.xticks(rotation=0)
    plt.tight_layout()