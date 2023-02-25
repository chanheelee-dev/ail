import statsmodels.api as sm
from pathlib import Path

# Default paths
ROOT = Path(__file__).parents[2]
DEFAULT_PATH = ROOT / "datasets"

rdata_args = {"HistData.Guerry": ("Guerry", "HistData")}
rdata_path = {"HistData.Guerry": DEFAULT_PATH / "guerry.csv"}

def download(dataset_name, target_path=""):
    target_path = target_path if target_path else rdata_path[dataset_name]
    