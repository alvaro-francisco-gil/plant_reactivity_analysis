from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).parent.parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
WAV_FOLDER = RAW_DATA_DIR / "wav_files"
TEXT_EURYTHMY_FILES = RAW_DATA_DIR / "txt_files"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
FEATURES_LETTERS_DIR = PROCESSED_DATA_DIR / "segmented_by_letters"
FEATURES_ONE_SEC_DIR = PROCESSED_DATA_DIR / "segmented_by_one_second"
EXPERIMENT_DIR = DATA_DIR / "experiment"

# Raw files
MEASUREMENTS_INFO = RAW_DATA_DIR / "measurements_info.csv"
MEASUREMENTS_EURYTHMY = INTERIM_DATA_DIR / "measurements_with_eurythmy.csv"

# Model directory
MODELS_DIR = BASE_DIR / "models"

# Report directories
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Notebook directory
NOTEBOOKS_DIR = BASE_DIR / "notebooks"
