import conf

def load():
    if conf.model_type == 'ff':
        from input_base import InputBase
        input = InputBase()
    else:
        from input_cnn import InputCNN
        input = InputCNN()
    input.load(conf.path)
    return input
