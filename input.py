import csv
import logger

class Input:
    def __init__(self, n_targets, n_chunk):
        self.n_targets = n_targets
        self.n_chunk = n_chunk
        self.reader = None
        self.n_data = 0

    def load(self, path):
        if self.n_chunk == 0:
            self.n_chunk = self.__linecounts(path)
        try:
            f = open(path, "r")
        except IOError:
            logger.error("csv file not found: {}".format(path))
            exit(1)

        self.reader = csv.reader(f, delimiter = ',')
        row = next(self.reader)
        self.n_data = len(row) - self.n_targets
        f.seek(0)

    def __linecounts(self, path):
        count = 0
        for line in open(path): count += 1
        return count

    def __iter__(self):
        return self

    def __next__(self):
        data = []
        labels = []
        for i in range(self.n_chunk):
            try:
                row = next(self.reader)
            except StopIteration:
                break
            labels.append(self.__to_floats(row[:self.n_targets]))
            data.append(self.__to_floats(row[self.n_targets:]))
        if len(data) == 0:
            raise StopIteration
        return data, labels

    def __to_floats(self, arr):
        arr_f = []
        for a in arr:
            arr_f.append(float(a))
        return arr_f
