from input_base import InputBase
import conf

class InputCNN(InputBase):
    def __next__(self):
        data, labels = super().__next__()
        return self.__get_2d_inputs(conf.width, conf.height, data), labels

    def __get_2d_inputs(self, x, y, arr):
        arr2d = []
        for a in arr:
            arr_row = []
            for i in range(0, x):
                arr_col = []
                for j in range(0, y):
                    arr_col.append([a[i * y + j]])
                arr_row.append(arr_col)
            arr2d.append(arr_row)
        return arr2d
