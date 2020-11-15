from keras.models import Model
from keras.layers import Dense
import conf

class TrainModelBase:
    def __init__(self, arg):
        if type(arg) is int:
            self.__build_model(arg)
        else:
            self.__load_model(arg)

    def __build_model(self, n_inputs):
        input, out_layer = self.setup_layers(n_inputs)
        out_read = Dense(3, activation='softmax')(out_layer)
        out_write = Dense(3, activation='softmax')(out_layer)
        self.model = Model(inputs = input, outputs = [out_read, out_write])
        self.model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics=['accuracy'])

    def setup_layers(self, n_inputs):
        pass

    def __load_model(self, path):
        import keras.models
        self.model = keras.models.load_model(path)

    def fit(self, input):
        for data, labels1, labels2 in input:
            self.model.fit([data], [labels1, labels2], epochs=conf.epochs)

    def save(self, path):
        self.model.save(path)

    def test(self, input_test):
        for data, labels1, labels2 in input_test:
            r = self.model.evaluate([data], [labels1, labels2])
            print(r)

    def predict(self, inputs):
        for data, labels1, labels2 in inputs:
            for i in range(0, len(data)):
                preds = self.model.predict([[data[i]]])
                labels = labels1[i] + labels2[i]
                predicted = preds[0][0].tolist() + preds[1][0].tolist()
                print(self.__to_readable_floats(labels), self.__to_readable_floats(predicted))

    def __to_readable_floats(self, floats):
        floats_readable = []
        for f in floats:
            floats_readable.append(round(f, 4))
        return floats_readable
