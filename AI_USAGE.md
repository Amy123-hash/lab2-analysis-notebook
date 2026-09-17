# AI Usage Log — Lab 2

Tool used: Claude (Anthropic), web/chat interface.

## Main notebook (`framingham_analysis.ipynb`)

- Asked Claude to help scaffold the notebook's overall structure (load → inspect → transform →
  model → visualize → interpret) matching the Lab 2 requirements.
- Asked Claude to draft the `pd.cut()` logic for bucketing `age` into four groups, and the
  `groupby(...).agg(...)` call for the age-group × smoking-status CHD summary table.
- Asked Claude to explain why exponentiating logistic regression coefficients (`np.exp(coef_)`)
  gives odds ratios, and to draft the two-panel `matplotlib` figure comparing observed CHD rates
  and modeled odds ratios.
- I chose the specific features (`age`, `sysBP`, `totChol`, `currentSmoker`, `diabetes`), the age
  cutpoints, and wrote the final interpretation paragraph myself.

## Extra-credit notebook: attempt 1, `rpy2` (abandoned) → attempt 2, `reticulate` (used)

### Attempt 1: rpy2 %%R magic (Jupyter, Python kernel)

- Not covered in lecture. Asked Claude to explain what `rpy2.ipython`'s `%load_ext` / `%%R`
  magic does, and the `-i`/`-o` flags for passing objects between Python and R.
- Hit `ModuleNotFoundError: No module named 'rpy2'` on first run. Asked Claude what it meant;
  fixed with `%pip install rpy2` in a notebook cell, then a full kernel restart (per Claude's
  explanation that `%pip` targets the active kernel's environment, unlike a plain terminal
  `pip install`, which can end up in a different Python than VS Code's notebook is using).
- After installing rpy2 and restarting, `%load_ext rpy2.ipython` still failed, now with a
  different error:
  ```
  error: symbol 'R_getVar' not found in library 'C:\Program Files\R\R-4.4.2\bin\x64\R.dll': error 0x7f
  ```
  Asked Claude to diagnose this. It confirmed rpy2 itself had installed successfully (the pip
  log showed `Successfully installed rpy2-3.6.7 ...`), so the problem was rpy2's compiled
  bindings failing to bind to the specific R 4.4.2 DLL on my machine — an ABI-level
  incompatibility, not a missing-package or PATH problem.
- Tried Claude's suggested workaround, adding R's DLL directory explicitly in Python
  (`os.add_dll_directory(r"C:\Program Files\R\R-4.4.2\bin\x64")`) before importing rpy2. Same
  `R_getVar` error persisted.
- Claude then searched for the exact error text and found this is a known, long-standing class
  of rpy2-on-Windows issue (multiple open/historical GitHub issues on the rpy2 repo with similar
  DLL/ABI errors across different rpy2/R version combinations, without one universal fix).
  Given my deadline, I decided with Claude to abandon rpy2 rather than keep debugging an
  unresolved compatibility issue.

### Attempt 2: reticulate (Quarto .qmd) — what I actually submitted

- Asked Claude to explain how `reticulate` differs from `rpy2` (R embeds Python, rather than
  Python embedding R), and why that direction tends to be more reliable on Windows.
- Asked Claude to draft the `.qmd` structure: an R chunk to load/clean the data, a Python chunk
  that receives the R data frame via `reticulate`'s automatic `r.` object exposure and fits a
  `scikit-learn` logistic regression, and a final R chunk that reads the Python result back via
  `py$` and builds the R-vs-Python comparison table.
- Asked Claude to explain the `r.model_df` / `py$py_odds_ratios` syntax for passing objects in
  each direction.
- I decided what the two-way exchange should actually accomplish (fit the same model on both
  sides and compare the odds ratios), chose the features, and wrote the interpretation.
- **Caveat:** I have not yet fully re-executed this `.qmd` end-to-end on my machine as of writing
  this log entry — I'm doing that next, immediately before submitting, and will update this note
  if anything else comes up.

## Environment error encountered while running the main notebook

### Error: `ModuleNotFoundError: No module named 'sklearn'`

**Error text:**
```
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[4], line 1
----> 1 from sklearn.linear_model import LogisticRegression
      3 features = ["age", "sysBP", "totChol", "currentSmoker", "diabetes"]
      4 X = df_clean[features]

ModuleNotFoundError: No module named 'sklearn'
```

**What this means:** The logistic-regression cell imports `scikit-learn` (as `sklearn`), but
that package wasn't installed in the Python environment my VS Code notebook was actually
using — the code itself was correct, the environment was just missing the dependency.

**Fix:** Asked Claude what the error meant and how to fix it. Added a new cell above the
regression code and ran `%pip install scikit-learn` (using `%pip` rather than a plain
terminal `pip install`, since that installs into the specific environment the notebook
kernel is using, which matters in VS Code where multiple Python environments can be
present). Once the install finished, restarted the kernel (Kernel → Restart Kernel) so the
new package would be picked up.

**Verified by:** Re-ran `from sklearn.linear_model import LogisticRegression` and it
completed with no error, then re-ran the full regression cell and confirmed the
`odds_ratios` output matched what was expected (age and diabetes with the highest odds
ratios).

- **Outcome: not submitted.** With my deadline approaching, I ran into further setup friction
  getting `reticulate`/Quarto working (`install.packages()` and `quarto render` need to run in
  an R console and a terminal respectively, not a Python notebook cell — a mistake I made under
  time pressure) and made the call with Claude to prioritize a complete, correct, on-time main
  submission over a rushed and unverified extra-credit attempt. The mixed-language notebook is
  not included in this submission.

## What I did NOT ask AI to do

- Did not ask AI to write the final interpretation paragraphs from scratch — I wrote those based
  on reading my own output tables/plots, then had Claude review wording for clarity only.
- Did not use AI-generated data; both notebooks load the real public dataset.
