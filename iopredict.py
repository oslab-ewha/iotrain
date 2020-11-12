#!/usr/bin/python3

import logger
import conf

def __usage_iopredict():
    print("""\
Usage: iopredict.py [<options>] <path>
  <options>
   -h: help(this message)
   -m <model file>
""")

class IoPredict:
    def predict(self):
        from input_test import InputTest
        from model import TrainModel

        model = TrainModel(conf.path_model)

        input_pred = InputTest(3, 1)
        input_pred.load(conf.path)
        model.predict(input_pred)

if __name__ == "__main__":
    from iopredict import IoPredict

    logger.init("testtrain")

    ip = IoPredict()
    conf.Conf("", __usage_iopredict)
    exit(ip.predict())
