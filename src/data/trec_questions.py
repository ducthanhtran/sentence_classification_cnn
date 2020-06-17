from utils import download_raw_files


DATA_NAME = "trec_questions"
ROOT_DIR = "./data/"
URLS = [
    "https://cogcomp.seas.upenn.edu/Data/QA/QC/train_1000.label",
    "https://cogcomp.seas.upenn.edu/Data/QA/QC/train_2000.label",
    "https://cogcomp.seas.upenn.edu/Data/QA/QC/train_3000.label",
    "https://cogcomp.seas.upenn.edu/Data/QA/QC/train_4000.label",
    "https://cogcomp.seas.upenn.edu/Data/QA/QC/train_5500.label",
    "https://cogcomp.seas.upenn.edu/Data/QA/QC/TREC_10.label",
]


if __name__ == "__main__":
    for url in URLS:
        download_raw_files(url, DATA_NAME, ROOT_DIR)

