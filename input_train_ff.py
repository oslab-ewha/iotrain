from input import Input

class InputTrainFF(Input):
    def __next__(self):
        data, labels1, labels2 = super().__next__()
        return [data], [labels1], [labels2]
