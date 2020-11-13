from input import Input

class InputTrainFF(Input):
    def __next__(self):
        data, labels = super().__next__()
        return [data], [labels]
