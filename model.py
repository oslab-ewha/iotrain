from keras.layers import Dense
import conf
import os

def create(input):
    if conf.model_type == 'ff':
        from model_ff import TrainModelFF
        clsModel = TrainModelFF
    else:
        from model_cnn import TrainModelCNN
        clsModel = TrainModelCNN

    if not conf.clearModel and conf.path_model and os.path.exists(conf.path_model):
        model = clsModel(conf.path_model)
    else:
        model = clsModel(input.n_data)

    return model
