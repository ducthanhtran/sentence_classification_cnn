#!/usr/bin/env python3
from typing import List

import tensorflow as tf


class DataSet(object):
    def __init__(self, train_data_path: str, dev_data_path: str, test_data_paths: List[str], compression: str = 'GZIP') -> None:
        self.train = tf.data.TextLineDataset(train_data_path, compression_type=compression)
        self.dev = tf.data.TextLineDataset(dev_data_path, compression_type=compression)
        self.test = tf.data.TextLineDataset(test_data_paths, compression_type=compression)
