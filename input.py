import csv
import logger

class Input:
    def __init__(self, n_targets, n_chunk):
        self.n_targets = n_targets
        self.n_chunk = n_chunk
        self.reader = None
        self.n_data = 0

    def load(self, path):
        try:
            f = open(path, "r")
        except IOError:
            logger.error("csv file not found: {}".format(path))
            return False

        self.reader = csv.reader(f, delimiter = ',')
        row = next(self.reader)
        self.n_data = len(row) - self.n_targets
        f.seek(0)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        data = []
        labels = []
        for i in range(self.n_chunk):
            row = next(self.reader)
            if row is None:
                break
            labels.append(self.__to_floats(row[:self.n_targets]))
            data.append(self.__to_floats(row[self.n_targets:]))
        if len(data) == 0:
            raise StopIteration
        return [data], [labels]

    def __to_floats(self, arr):
        arr_f = []
        for a in arr:
            arr_f.append(float(a))
        return arr_f
