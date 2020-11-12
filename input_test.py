from input import Input

class InputTest(Input):
    def __init__(self, n_targets, n_chunk):
        super().__init__(n_targets, n_chunk)

    def __next__(self):
        data, labels = super().__next__()
        return data, labels
