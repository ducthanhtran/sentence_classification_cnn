from pathlib import Path
import tarfile
import urllib.request


DATA_RAW_DIR = "./data/raw/"
DATA_EXTRACTED_DIR = "./data/extracted"

DATA_URLS = [
    "http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz"
]


if __name__ == "__main__":
    raw_dir = Path(DATA_RAW_DIR)
    raw_dir.mkdir(parents=True, exist_ok=True)
    
    for url in DATA_URLS:
        out_file = raw_dir.joinpath(Path(url).name)
        with urllib.request.urlopen(url) as response, open(out_file, 'wb') as out:
            data = response.read()
            out.write(data)
    
    extracted_dir = Path(DATA_EXTRACTED_DIR)
    extracted_dir.mkdir(parents=True, exist_ok=True)
    
    for data in raw_dir.iterdir():
        target_dir = extracted_dir.joinpath(Path(data).name)
        target_dir.mkdir(exist_ok=True)

        f = tarfile.open(data)
        f.extractall(path=target_dir)

