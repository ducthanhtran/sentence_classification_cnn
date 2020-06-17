#!/usr/bin/env python3
from pathlib import Path
import tarfile
import urllib.request


def download_raw_files(url: str, data_name: str, root_path: str) -> None:
    root_dir = Path(root_path)
    data_dir = root_dir.joinpath(data_name)
    data_dir.mkdir(parents=True, exist_ok=True)

    raw_dir = data_dir.joinpath("raw")
    raw_dir.mkdir(exist_ok=True)
    
    raw_file = raw_dir.joinpath(Path(url).name) 
    with urllib.request.urlopen(url) as response, open(raw_file, 'wb') as out:
        data = response.read()
        out.write(data)
