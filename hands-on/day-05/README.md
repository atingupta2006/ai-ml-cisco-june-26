# Day 05 — Unsupervised Learning

**Theme:** Unsupervised Learning

## Session focus

- **Concepts:** K-Means, elbow method, DBSCAN, clustering evaluation, segmentation
- **Use-case:** NYSE stock segmentation

## Before you start

Read [lab execution guide](../../docs/lab-execution-guide.md) and open [labs.md](labs.md).

## Data

| File | Rows | Path |
|------|------|------|
| NYSE stocks | **500** daily | [`../../data/nyse/nyse_stocks.csv`](../../data/nyse/nyse_stocks.csv) |

Kaggle reference: [NYSE](https://www.kaggle.com/dgawlik/nyse)

Labs aggregate **25** symbols into per-stock features before clustering.

## Labs

| Lab | Topic | Notebook / script |
|-----|--------|--------|
| 1 | K-Means baseline | `notebooks/lab01_kmeans_baseline.ipynb` · `lab01_kmeans_baseline.py` |
| 2 | Elbow method | `notebooks/lab02_elbow_method.ipynb` · `lab02_elbow_method.py` |
| 3 | DBSCAN clusters | `notebooks/lab03_dbscan_clusters.ipynb` · `lab03_dbscan_clusters.py` |
| 4 | Cluster metrics | `notebooks/lab04_cluster_metrics.ipynb` · `lab04_cluster_metrics.py` |
| 5 | NYSE multi-cluster view | `notebooks/lab05_nyse_multi_cluster_view.ipynb` · `lab05_nyse_multi_cluster_view.py` |
| 6 | Segmentation summary | `notebooks/lab06_segmentation_summary.ipynb` · `lab06_segmentation_summary.py` |

## Syllabus

[course-content.txt](../../../course-content.txt) | [syllabus coverage](../../docs/syllabus-coverage.md)
