#!/usr/bin/python3

import logger
from conf import Conf

def __usage_traintest():
    print("""\
Usage: traintest.py [<options>] <path>
  <options>
   -h: help(this message)
   -m <model file>
""")

class TrainTest:
    def testTrain(self, conf):
        from input_test import InputTest
        from model import TrainModel

        model = TrainModel(conf.path_model)

        input_test = InputTest(3, 100)
        input_test.load(conf.path)
        model.test(input_test)

if __name__ == "__main__":
    import traintest

    logger.init("testtrain")

    tt = traintest.TrainTest()

    exit(tt.testTrain(Conf("", __usage_traintest)))


