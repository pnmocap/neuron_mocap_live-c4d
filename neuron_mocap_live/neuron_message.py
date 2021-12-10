import c4d
from neuron_defs import *

class NeuronMessageData(c4d.plugins.MessageData):
    def CoreMessage(self, id, bc):
        if id == ID_COREMESSAGE_FRAME_ARRIVED:
            c4d.DrawViews(c4d.DRAWFLAGS_ONLY_ACTIVE_VIEW)
        return True