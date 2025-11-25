import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression

def summary_data(df, columns):
    for col in columns:
        print(
        f"""\nSummary for {col}:
            Mean: {df[col].mean():.2f}
            Median: {df[col].median():.2f}
            Min: {df[col].min()}
            Max: {df[col].max()}
              """)
        

def simulating_proportions(df, column, size):
    """
    Calculate the observered proprotion of the value 1 in a specific column in a DataFrame,
    and then simulate how the proportion can look in a random sample of given size.
    """
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
    Calculate the mean confidence intervall for the values in a DataFrame column.
    """
    mean = x.mean()
    std = x.std(ddof=1)
    n = len(x)
    t_stats = stats.t.ppf(1 - (1 - confidence) / 2, df=n - 1)
    margin = t_stats*(std/np.sqrt(n))
    return mean - margin, mean + margin


def ci_mean_bootstrap(x, B=5000, confidence=0.95, seed=42):   
    """
    Calculate the mean confidence intervall for the values in a DataFrame column using bootstrap method.
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
    Using the redression to predict y-value given a specific x-value
    """
    return intercept_hat + slope_hat * x

