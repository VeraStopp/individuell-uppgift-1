import numpy as np
from scipy import stats

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
    np.random.seed(42)
    proportions = df[column].value_counts(normalize=True)
    p_1 = proportions[1]
    simulated = np.random.binomial(n=1, p=p_1, size=size)
    print(f"Proportion of 1 in sample: {p_1}")
    print(f"Simulated proportion of 1 with the sample size of {size}: {simulated.mean()}")


def conf_intervall(x, confidence=0.95):
    mean = x.mean()
    std = x.std(ddof=1)
    n = len(x)
    t_stats = stats.t.ppf(1 - (1 - confidence) / 2, df=n - 1)
    margin = t_stats*(std/np.sqrt(n))
    return mean - margin, mean + margin


def ci_mean_bootstrap(x, B=5000, confidence=0.95):   
    x = np.asarray(x, dtype=float)
    n = len(x)
    boots = np.empty(B)
    for b in range(B):
        boot_sample = np.random.choice(x, size=n)
        boots[b] = np.mean(boot_sample)
    lower = np.percentile(boots, 100*confidence / 2)
    upper = np.percentile(boots, 100*(1 - confidence / 2))
    return lower, upper
