import conf

class ConfIotrain(conf.Conf):
    def __init__(self, usage):
        conf.epochs = 10
        conf.clearModel = False

        super().__init__('e:C', usage)

    def handleOpt(self, o, a):
        if o == '-e':
            conf.epochs = int(a)
        elif o == '-C':
            conf.clearModel = True
