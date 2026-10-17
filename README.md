# Assignment 1: PyTorch Foundations (Task 3: Text Classification)

Generative AI & LLM, Fall 2026. Real vs. fake news classification with PyTorch.

## Setup

Python 3.10 on Windows (PowerShell):

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Place `txt_train.csv`, `txt_val.csv` and `txt_test.csv` in the `data/` folder.

## Files

| File | Purpose |
|---|---|
| `txt_classifier.py` | Text classifier: histogram, truncation/padding, optimizers, LSTM |
| `show_pairs.py` | Prints real/fake article pairs (Task 3.5) |
| `results/` | Saved console output from each run |
| `figures/length_histogram.png` | Task 3.1 histogram |
| `Report.pdf` | Results and analysis |

## Command-line arguments

| Argument | Meaning | Default |
|---|---|---|
| `--data_dir` | Folder containing the CSV files | `data` |
| `--batch_size` | Batch size | 1 |
| `--max_len` | Truncate/pad articles to this many tokens (-1 disables) | -1 |
| `--n_epochs` | Number of epochs | 5 |
| `--optimizer` | `sgd` or `adam` | `adam` |
| `--learning_rate` | Learning rate | 5.0 for SGD, 0.001 for Adam |
| `--model` | `bow` (EmbeddingBag baseline) or `lstm` | `bow` |
| `--hidden_dim` | LSTM hidden size | 64 |
| `--embed_dim` | Embedding size | 64 |
| `--seed` | Random seed | 42 |
| `--length_histogram` | Only draw the article-length histogram | off |
| `--output` | Checkpoint file name | `txt_model.pth` |

## Commands used for the experiments

```powershell
# Task 3.1
python txt_classifier.py --batch_size 1 --max_len -1 --length_histogram

# Task 3.2
python txt_classifier.py --batch_size 1 --max_len -1 --optimizer sgd
python txt_classifier.py --batch_size 1 --max_len 1024 --optimizer sgd
python txt_classifier.py --batch_size 32 --max_len 1024 --optimizer sgd
python txt_classifier.py --batch_size 32 --max_len -1 --optimizer sgd   # crashes (expected)

# Task 3.3
python txt_classifier.py --batch_size 32 --max_len 1024 --optimizer sgd
python txt_classifier.py --batch_size 32 --max_len 1024 --optimizer adam

# Task 3.4
python txt_classifier.py --batch_size 32 --max_len 1024 --model bow --output txt_bow.pth
python txt_classifier.py --batch_size 32 --max_len 1024 --model lstm --output txt_lstm.pth
```

## Model checkpoints

Google Drive: [PASTE SHAREABLE LINK HERE]

## AI tool use

[PASTE THE SHAREABLE CONVERSATION LINK(S) HERE, as required by the assignment]