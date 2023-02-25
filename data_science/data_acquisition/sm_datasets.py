from pathlib import Path
import statsmodels.api as sm
import pandas as pd

# Default paths
ROOT = Path(__file__).parents[2]
DEFAULT_PATH = ROOT / "datasets"

rdata_args = {"HistData.Guerry": ("Guerry", "HistData")}
rdata_path = {"HistData.Guerry": DEFAULT_PATH / "guerry.csv"}


def download(dataset_name, target_path=""):
    target_path = target_path if target_path else rdata_path[dataset_name]
    args = rdata_args[dataset_name]

    # Download data here
    df = sm.datasets.get_rdataset(*args).data

    # Save as csv
    df.to_csv(target_path)

    return target_path

def read(dataset_name, src_path=""):
    src_path = src_path if src_path else rdata_path[dataset_name]
    args = rdata_args[dataset_name]

    df = pd.read_csv(src_path, index_col=0)
    return df