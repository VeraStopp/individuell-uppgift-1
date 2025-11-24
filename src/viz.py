import pandas as pd
import numpy as np

# def _cat_for_plot(s, missing_label="Unknown"):  
#     """
#     Replace NaN values with "Unknown" for categorical variables.
#     """  
#     if hasattr(s, "astype"):
#         s = s.astype("object")
#     try:
#         return s.fillna(missing_label)
#     except Exception:
#         return s
    
def _num_for_plot(s):
    try:
        return pd.to_numeric(s, errors="coerce")
    except Exception:
        return s


def plot_hist(ax, x, title, xlabel, ylabel, bins=30, grid=True):
    """
    Create a histogram.
    """
    x = _num_for_plot(x)
    ax.hist(x, bins=bins, edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y")
    return ax

def boxplot_by_group(ax, df, values, group, title, xlabel, ylabel, grid=True):
    """
    Create boxplot of a column grouped by antoher column. 
    """
    df.boxplot(column=values, by=group, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y")
    return ax

def plot_scatter(ax, x, y, title, xlabel, ylabel, alpha=0.6, grid=True):
    """
    Create scatter plot.
    """
    x = _num_for_plot(x)
    y = _num_for_plot(y)
    ax.scatter(x, y, alpha=alpha)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid)
    return ax

def plot_barchart(ax, x, title, xlabel, ylabel="Frequency", grid=True):
    """
    Create a bar chart for a categorical variable
    """
    counts = x.value_counts()
    counts.plot(kind="bar", edgecolor="black", ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y")
    return ax
