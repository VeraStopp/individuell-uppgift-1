import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
        

def simulating_proportions(df, column, size):
    """
    Simulate binary outcomes based on the observed proportion of 1's in the dataset.

    Parameters:
        df: Pandas DataFrame.
        column: Name of the column from wich to estimate the proportion of 1's.
        size: Number of simulated binary observations to generate.

    Returns:
        Prints the observed proportions of 1's and the simulated proportion. 
    """
    if column not in df.columns:
        raise ValueError(f"The column "{column}" doesn't exist in the DataFrame.")
    np.random.seed(42)
    proportions = df[column].value_counts(normalize=True)
    p_1 = proportions[1]
    simulated = np.random.binomial(n=1, p=p_1, size=size)
    print(f"""
    Proportion of 1 in sample : {p_1}                               
    Simulated proportion of 1 with the sample size of {size} : {simulated.mean()}
    """)
   


def conf_intervall(x, confidence=0.95):
    """
    Calculate the confidence intervall for the mean of a sample using the t-distrubution.
    
    Parameters:
        x: Array-like sequence of numeric observations.
        confidence: Confidence level (0 and 1). Optional. Default is 0.95
    
    Returns:
        A tuple (lower, upper) representing the calculated confidence intervall.
    """
    mean = x.mean()
    std = x.std(ddof=1)
    n = len(x)
    t_stats = stats.t.ppf(1 - (1 - confidence) / 2, df=n - 1)
    margin = t_stats*(std/np.sqrt(n))
    return mean - margin, mean + margin


def ci_mean_bootstrap(x, B=5000, confidence=0.95, seed=42):   
    """
    Calculate the confidence intervall for the mean of a sample using bootstrap method.

    Parameters:
        x: Array-like sequence of numeric observations.
        B: Number of bootstrap samples to generate. Default is 5000
        confidence: Confidence level (0 and 1). Default is 0.95.
        seed: Random seed for reproducibility. Default is 42.
    """
    x = np.asarray(x, dtype=float)
    n = x.size
    rng = np.random.default_rng(seed)
    boot_means = np.empty(B)
    for b in range(B):
        sample = rng.choice(x, size=n, replace=True)
        boot_means[b] = sample.mean()
    alpha = 1 - confidence
    lower = np.percentile(boot_means, 100 * (alpha / 2))
    upper = np.percentile(boot_means, 100 * (1 - alpha / 2))
    return lower, upper

def regression(df, x, y):
    """
    Fit a simple linear regression model using one predictor variable.

    Parameters:
        df: Pandas DataFrame.
        x: Name of the column to use as the predictor variable.
        y: Name of the column to use as the response variable.
    
    Returns:
        A tuple containing:
            intercept_hat: Estimated intercept of the regression line.
            slope_hat: Estimated slope coefficient.
            r2: R-squared.
            y_hat: Predicted values from the fitted model.
            residulas: Differense between observed and predicted values.
    """
    x = df[[x]].values
    y = df[y].values
    linreg = LinearRegression()
    linreg.fit(x, y)

    intercept_hat = float(linreg.intercept_)
    slope_hat = float(linreg.coef_[0])
    r2 = float(linreg.score(x, y))
    y_hat = linreg.predict(x)
    residuals = y - y_hat
    return intercept_hat, slope_hat, r2, y_hat, residuals


def regression_prediction(x, intercept_hat, slope_hat):
    """
    Calculate the predicted value from a linear regression model.

    Parameters:
        x: Numeric value or array-like input for which to calculate predictions.
        intercept_hat: Estimated intercept of the regression line.
        slope_hat: Estimated slope coefficient.
    """
    return intercept_hat + slope_hat * x

def plot_scatter(ax, x, y, title, xlabel, ylabel, alpha=0.6, grid=True):
        """
        Create a scatter plot of two numeric variables.

        Parameters:
            ax: A Matplotlib axes to draw thr plot onto.
            column1: The numeric variable for the x-axis.
            column2: The numeric variable for the y-axis.
            title: The title of the plot.
            xlabel: The label for the x-axis.
            ylabel: The label for the y-axis.
            alpha: Default is 0.6.
            grid: Default is True.

        Returns:
            The Matplotlib axes (ax) with the box plot drawn.
        """
        ax.scatter(x, y, alpha=alpha)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(grid)
        return ax

