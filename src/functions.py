
def summary_data(df, columns):
    for col in columns:
        print(
        f"""\nSummary for {col}:
            Mean: {df[col].mean():.2f}
            Median: {df[col].median():.2f}
            Min: {df[col].min()}
            Max: {df[col].max()}
              """)
        
