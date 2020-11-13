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
        import input
        import model

        input = input.load()
        model_pred = model.create(input)
        model_pred.predict(input)

if __name__ == "__main__":
    from iopredict import IoPredict

    logger.init("testtrain")

    ip = IoPredict()
    conf.Conf("", __usage_iopredict)
    exit(ip.predict())
