# Day 02 — Labs

**Theme:** Python for Data Science | **Lab time (6 labs):** ~290 min (~4.8 h)

**Execution guide:** [docs/lab-execution-guide.md](../../docs/lab-execution-guide.md) — read before Lab 1.

---

## Before every lab

**Environment:** one venv for all days — `setup_student_env.ps1` or `setup_student_env.sh` at repo root. Kernel: **Python (cisco-aiml-lab)**. [Lab execution guide](../../docs/lab-execution-guide.md).

Run notebooks in `notebooks/` in lab order (`lab01` … `lab06`).

---

## Expected outcomes

| After lab | Check |
|-----------|--------|
| Lab 1 | `len(cities)` = **4**; cuisines set has **3** items |
| Lab 2 | `votes` shape = **(5,)**; column means ≈ **[1392, 1290]** |
| Lab 3 | `df.shape` = **(500, 9)**; mean rating ≈ **3.70** |
| Lab 4 | `rating_distribution.png` saved; mean rating ≈ **3.70** |
| Lab 5 | Model trained on **500** rows; intercept ≈ **3.72** |
| Lab 6 | Test size = **100**; RMSE ≈ **0.69** |


## Lab pacing

| Lab | Est. time |
|-----|-----------|
| Lab 1 | ~40 min |
| Lab 2 | ~45 min |
| Lab 3 | ~55 min |
| Lab 4 | ~50 min |
| Lab 5 | ~50 min |
| Lab 6 | ~50 min |
| **Total** | **~290 min** |

---

# Lab 1 — Python structures

## Objective

Practice core Python data structures — lists, tuples, dictionaries, and sets — using restaurant-themed examples.

**Estimated time:** ~40 min

## Lab flow

```text
  list (cities) → tuple (ratings) → dict (restaurant) → set (cuisines)
```

## Tasks

1. Open `notebooks/lab01_python_structures.ipynb` (recommended) or `lab01_python_structures.py`.
2. Run all cells / the script and read the markdown explanations for list, tuple, dict, and set.
3. In the notebook, try appending a city — then reset to 4 cities for the checkpoint.
4. Answer the reflection questions at the end of the notebook.

## Example result

```text
cities (list, len=4): ['Bengaluru', 'Mumbai', 'Delhi', 'Hyderabad']
unique cuisines (set): ['Cafe', 'Chinese', 'North Indian']
```

## Success criteria

* Script runs without errors.
* You can explain the difference between list, tuple, dict, and set.
* `len(cities)` = **4** and the cuisines set contains **3** unique values.

---

# Lab 2 — NumPy arrays

## Objective

Create NumPy arrays, apply vectorized math, and combine columns into a 2-D matrix.

**Estimated time:** ~45 min

## Lab flow

```text
  1-D arrays → normalization → element-wise division → column_stack → axis means
```

## Tasks

1. Open `notebooks/lab02_numpy_arrays.ipynb` (recommended) or `lab02_numpy_arrays.py`.
2. Run through vectorization, z-score normalization, and `column_stack` sections.
3. Complete the experiment cell — change one vote and observe downstream updates.
4. Compare `matrix.sum(axis=0)` with `col_means` in the axis reductions section.

## Example result

```text
votes shape: (5,), dtype: int64
matrix shape: (5, 2)
column means [votes, cost]: [1392. 1290.]
```

## Success criteria

* Script runs without errors.
* `votes.shape` is **(5,)** and `matrix.shape` is **(5, 2)**.
* Column means are approximately **[1392, 1290]**.

---

# Lab 3 — Pandas Zomato load

## Objective

Load the Zomato restaurants CSV with Pandas and perform first-pass exploration.

**Estimated time:** ~55 min

## Lab flow

```text
  read_csv → shape / columns → head → describe
```

## Tasks

1. Confirm the dataset path in [data/README.md](../../data/README.md): `zomato/zomato_restaurants.csv` (**500** rows).
2. Open `notebooks/lab03_pandas_zomato_load.ipynb` (recommended) or `lab03_pandas_zomato_load.py`.
3. Run all cells; verify `df.shape == (500, 9)`.
4. Complete the categorical exploration and filtering sections; note mean rating ≈ **3.70**.

## Example result

```text
shape (rows, cols): (500, 9)
mean aggregate_rating: 3.70
```

## Success criteria

* `df.shape` = **(500, 9)**.
* Nine columns present including `aggregate_rating`, `votes`, and `average_cost_for_two`.
* `describe()` shows mean rating near **3.70**.

---

# Lab 4 — Seaborn plots

## Objective

Build exploratory plots with Seaborn — rating distribution and cost by city.

**Estimated time:** ~50 min

## Lab flow

```text
  load CSV → histplot (ratings) → boxplot (cost by city) → save figure
```

## Tasks

1. Open `notebooks/lab04_seaborn_plots.ipynb` (recommended) or `lab04_seaborn_plots.py`.
2. Run all cells; confirm `output/rating_distribution.png` is saved.
3. Experiment with histogram `bins` (10 vs 20) in the notebook.
4. Describe one insight from the rating histogram and one from the cost box plot.

## Example result

```text
rating plot saved: rating_distribution.png
mean rating: 3.70
top city by avg cost: Kolkata (1402)
```

## Success criteria

* `output/rating_distribution.png` is created.
* Mean rating printed ≈ **3.70**.
* You can describe one insight from each plot.

---

# Lab 5 — Linear regression fit

## Objective

Fit ordinary least squares (OLS) linear regression to predict `aggregate_rating` from `votes` and `average_cost_for_two`.

**Estimated time:** ~50 min

## Lab flow

```text
  select features → LinearRegression.fit → inspect intercept & coefficients → sample predictions
```

## Tasks

1. Open `notebooks/lab05_linear_regression_fit.ipynb` (recommended) or `lab05_linear_regression_fit.py`.
2. Fit the model and compare predicted vs actual ratings for the first three rows.
3. Complete the extension cell — add `online_order` encoded as 0/1 and refit.
4. Relate intercept and coefficients to the OLS equation \( \hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 \).

## Example result

```text
training rows: 500
intercept: 3.7167
coefficients [votes, cost]: [0. -0.]
```

## Success criteria

* Model fits on **500** rows without error.
* Intercept and two coefficients are printed.
* You can state which features were used as \(X\) and which column is \(y\).

---

# Lab 6 — LR evaluation metrics

## Objective

Split data into train/test sets and evaluate regression with **R²**, **MSE**, **MAE**, and **RMSE**.

**Estimated time:** ~50 min

## Lab flow

```text
  train_test_split → fit on train → predict test → metric functions
```

## Tasks

1. Open `notebooks/lab06_lr_evaluation_metrics.ipynb` (recommended) or `lab06_lr_evaluation_metrics.py`.
2. Run all cells; record R², MSE, MAE, and RMSE on the test set.
3. Review predicted-vs-actual and residual plots.
4. Compare RMSE (~**0.69**) to the rating range (2.5–4.9) and discuss whether R² near zero is acceptable.

## Example result

```text
train size: 400, test size: 100
R2: -0.0031
RMSE: 0.6852
```

## Success criteria

* Train size **400** and test size **100** (with `test_size=0.2`, `random_state=42`).
* All four metrics printed.
* You can define R², MSE, MAE, and RMSE in your own words.

---
