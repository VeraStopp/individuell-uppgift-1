import pandas as pd

class HealthAnalyzer:
    def __init__(self, df):
        self.df = df

    def summary_data(self, columns):
        for col in columns:
            print(
            f"""\nSummary for {col}:
                Mean: {self.df[col].mean():.2f}
                Median: {self.df[col].median():.2f}
                Min: {self.df[col].min()}
                Max: {self.df[col].max()}
                """)
    
    def plot_scatter(self, column1, column2):
        """
        Creating a scatter plot with two given DataFrame columns
        """
        x = self.df[column1].to_numpy()
        y = self.df[column2].to_numpy()
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(x, y)
        ax.set_title(f"{column1} vs. {column2}")
        ax.set_xlabel(column1)
        ax.set_ylabel(column2)
        ax.grid(True)
        return ax