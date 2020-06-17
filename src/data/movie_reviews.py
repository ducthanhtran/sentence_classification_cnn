from utils import download_raw_files


DATA_NAME = "movie_review"
ROOT_DIR = "./data/"
URL = "http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz"


if __name__ == "__main__":
    download_raw_files(URL, DATA_NAME, ROOT_DIR)

