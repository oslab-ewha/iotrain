#!/usr/bin/python3

import logger
from conf_it import ConfIotrain
import conf

def __usage_iotrain():
    print("""\
Usage: iotrain.py [<options>] <path>
  <options>
   -h: help(this message)
   -e <epochs>
   -C: clear an existing model if any
   -t <model type>: ff(default), cnn
   -m <model file>
   -d <widthxheight>: access bitmap dimension
""")

class IoTrain:
    def goTrain(self):
        import input
        import model

        input = input.load()
        model_train = model.create(input)
        model_train.fit(input)

        if not conf.path_model is None:
            model_train.save(conf.path_model)

if __name__ == "__main__":
    import iotrain

    logger.init("iotrain")

    it = iotrain.IoTrain()

    ConfIotrain(__usage_iotrain)
    exit(it.goTrain())
