#!/usr/bin/env python3
from typing import List

import tensorflow as tf


DELIMITER = '|||'


class DataSet(object):
    def __init__(self, train_data_path: str, dev_data_path: str, test_data_paths: List[str], compression: str = 'GZIP') -> None:
        self.train = self._split_label(tf.data.TextLineDataset(train_data_path, compression_type=compression))
        self.dev = self._split_label(tf.data.TextLineDataset(dev_data_path, compression_type=compression))
        self.test = self._split_label(tf.data.TextLineDataset(test_data_paths, compression_type=compression))

    @staticmethod
    def _split_label(data: tf.data.Dataset) -> tf.data.Dataset:

        def splitter(x):
            # Format: '<LABEL>|||<SENTENCE>'
            splitted = tf.strings.split(x, DELIMITER)
            return tf.strings.to_number(splitted[0], tf.int32), splitted[1]

        return data.map(splitter)
