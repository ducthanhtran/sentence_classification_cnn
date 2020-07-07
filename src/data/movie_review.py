#!/usr/bin/env python3
from utils import DataSet


TRAIN = "./data/movie_review/final/train.gz"
DEV = "./data/movie_review/final/dev.gz"
TEST = "./data/movie_review/final/test.gz"


if __name__ == "__main__":
    dataset = DataSet(TRAIN, DEV, [TEST])
    
