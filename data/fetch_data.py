"""
Optional convenience script: downloads the Framingham teaching-subset CSV to data/framingham.csv.

Not required to run the notebooks — both notebooks load the data directly from this same URL
at runtime via pd.read_csv(). This script exists only so the "source data, or a script that
fetches it" checklist item is unambiguous, and for anyone who wants a local copy for offline use.
"""
import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/TarekDib03/Analytics/master/Week3%20-%20Logistic%20Regression/Data/framingham.csv"
OUT_PATH = "data/framingham.csv"

if __name__ == "__main__":
    df = pd.read_csv(DATA_URL)
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved {len(df)} rows to {OUT_PATH}")
