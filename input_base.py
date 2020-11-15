import csv
import logger

class InputBase:
    def __init__(self):
        self.n_targets = 6
        self.reader = None
        self.n_data = 0

    def load(self, path):
        try:
            f = open(path, "r")
        except IOError:
            logger.error("csv file not found: {}".format(path))
            exit(1)

        self.reader = csv.reader(f, delimiter = ',')
        row = next(self.reader)
        self.n_data = len(row) - self.n_targets
        f.seek(0)

    def __iter__(self):
        return self

    def __next__(self):
        data = []
        labels1 = []
        labels2 = []
        while True:
            try:
                row = next(self.reader)
                labels1.append(self.__to_floats(row[:3]))
                labels2.append(self.__to_floats(row[3:6]))
                data.append(self.__to_floats(row[self.n_targets:]))
            except StopIteration:
                break

        if len(data) == 0:
            raise StopIteration
        return data, labels1, labels2

    def __to_floats(self, arr):
        arr_f = []
        for a in arr:
            arr_f.append(float(a))
        return arr_f

