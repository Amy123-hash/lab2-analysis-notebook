# Lab 2: Analysis Notebook — Framingham Heart Study

PUBH 4201 — Applied Computing for Health Data Science

## What's here

```
.
├── README.md
├── AI_USAGE.md
├── environment.yml
├── notebooks/
│   └── framingham_analysis.ipynb              # main Lab 2 notebook (Python)
├── rendered/
│   └── framingham_analysis.html                # exported HTML of the main notebook
└── data/
    └── fetch_data.py                            # optional convenience script; notebooks also
                                                  # load the data directly from its public URL
```

## Dataset

Framingham Heart Study teaching subset (4,240 participants, 15 predictor variables, 10-year CHD
outcome). Both notebooks load it directly from its public source at runtime with
`pd.read_csv(DATA_URL)` — no manually downloaded/cleaned copy is checked into the repo.

> The exact source URL is set near the top of each notebook. If your course's own
> `data/raw/lab2-epi-framingham/SOURCE.md` specifies a different canonical URL, swap it in —
> the loading/cleaning/analysis code downstream does not depend on which mirror you use, as
> long as the column names match the standard Framingham teaching schema (`age`, `sysBP`,
> `totChol`, `currentSmoker`, `diabetes`, `TenYearCHD`, etc.).

## How to re-run

### Main notebook (`framingham_analysis.ipynb`)

1. Create the environment: `conda env create -f environment.yml && conda activate lab2-fhs`
   (or just `pip install pandas numpy matplotlib scikit-learn jupyter`).
2. Open `notebooks/framingham_analysis.ipynb` in Jupyter.
3. **Kernel → Restart Kernel and Run All Cells.** No manual steps required (data loads over
   the network from the URL in the notebook).
4. Export the rendered copy:
   ```bash
   jupyter nbconvert --to html --execute notebooks/framingham_analysis.ipynb \
     --output-dir=rendered --output=framingham_analysis.html
   ```

## Note on the mixed-language extra credit

Not submitted. I attempted it (first with `rpy2`'s `%%R` Jupyter magic, then with
`reticulate`/Quarto after the first approach hit an unresolved Windows compatibility error),
but ran out of time before getting a working, rendered version. Full details of both attempts
are in `AI_USAGE.md`.

## Notes

- Both notebooks require an internet connection when run (the data is fetched live, not from a
  local copy).
- AI assistance is documented inline in each notebook (a markdown cell near the top and a
  summary section near the bottom) and in `AI_USAGE.md`.
