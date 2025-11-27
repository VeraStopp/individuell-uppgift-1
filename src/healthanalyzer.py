import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class HealthAnalyzer:
    def __init__(self, df):
        self.df = df
    
    def __repr__(self):
        return f"HealthAnalyzer(n_rows={len(self.df)}, n_cols={len(self.df.columns)})"
    
    def __str__(self):
        return (
        "HealthAnalyzer\n"
        f"- Rows: {len(self.df)}\n"
        f"- Columns: {', '.join(self.df.columns)}"
        )

    def summary_data(self, columns):
        """Calculate and print mean, median, min och max for a numeric column i the DataFrame"""
        for col in columns:
            print(
            f"""\nSummary for {col}:
                Mean: {self.df[col].mean():.2f}
                Median: {self.df[col].median():.2f}
                Min: {self.df[col].min()}
                Max: {self.df[col].max()}
                """)
    
    def boxplot_by_group(self, ax, values, group, title, xlabel, ylabel, grid=True):
        """
        Create a box plot of a numeric column, grouped by a categorical column from the DataFrame.

        Parameters:
            ax: A Matplotlib axes to draw the plot onto.
            values: The numeric column.
            group: the caterical column used for grouping.
            title: The title of the plot.
            xlabel: The label for the x-axis.
            ylabel: The label for the y-axis.
            grid: Default is True.

        Returns:
            The Matplotlib axes (ax) with the box plot drawn. 
        """
        self.df.boxplot(column=values, by=group, ax=ax)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(grid, axis="y")
        return ax
    
    def plot_hist(self, ax, column, title, xlabel, ylabel, bins=30, grid=True):
        """
        Create a histogram of a numeric column from the DataFrame.

        Parameters:
            ax: A Matplotlib axes to draw the plot onto.
            column: The numeric column.
            title: The title of the plot.
            xlabel: The label for the x-axis.
            ylabel: The label for the y-axis.
            bins: Number of bins. Default is 30.
            grid: Default is True.

        Returns:
            The Matplotlib axes (ax) with the box plot drawn. 
        """
        ax.hist(self.df[column], bins=bins, edgecolor="black")
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(grid, axis="y")
        return ax
    
    def plot_barchart(self, ax, column, title, xlabel, ylabel="Frequency", grid=True):
        """
        Create a bar chart showing the frequency of unique values for a catagorical column in the DataFrame.

        Parameters:
            ax: A Matplotlib axes to draw the plot onto.
            column: The categorical column.
            title: The title of the plot.
            xlabel: The label for the x-axis.
            ylabel: The label for the y-axis. Default is "Frequency"
            grid: Default is True.

        Returns:
            The Matplotlib axes (ax) with the box plot drawn. 
        """
        counts = self.df[column].value_counts()
        counts.plot(kind="bar", edgecolor="black", ax=ax)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(grid, axis="y")
        return ax
    
    def plot_scatter(self, ax, column1, column2, title, xlabel, ylabel, alpha=0.6, grid=True):
        """
        Create a scatter plot of two numeric column in the DataFrame.

        Parameters:
            ax: A Matplotlib axes to draw thr plot onto.
            column1: The numeric column for the x-axis.
            column2: The numeric column for the y-axis.
            title: The title of the plot.
            xlabel: The label for the x-axis.
            ylabel: The label for the y-axis.
            alpha: Default is 0.6.
            grid: Default is True.

        Returns:
            The Matplotlib axes (ax) with the box plot drawn. 
        """
        ax.scatter(self.df[column1], self.df[column2], alpha=alpha)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(grid)
        return ax
    
    def simulating_proportions(self, column, size):
        """
        Simulate binary outcomes based on the observed proportion of 1's in the dataset.

        Parameters:
            df: Pandas DataFrame.
            column: Name of the column from wich to estimate the proportion of 1's.
            size: Number of simulated binary observations to generate.

        Returns:
            Prints the observed proportions of 1's and the simulated proportion. 
        """
        np.random.seed(42)
        proportions = self.df[column].value_counts(normalize=True)
        p_1 = proportions[1]
        simulated = np.random.binomial(n=1, p=p_1, size=size)
        print(f"""
        Proportion of 1 in sample : {p_1}                               
        Simulated proportion of 1 with the sample size of {size} : {simulated.mean()}
        """)