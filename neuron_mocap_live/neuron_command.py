import c4d
from neuron_defs import *
from neuron_command_dialog import *

class NeuronCommandData(c4d.plugins.CommandData):
    def __init__(self):
        self._dlg = None

    def Execute(self, doc):
        if self._dlg is None:
            self._dlg = NeuronCommandDialog()
        self._dlg.Open(dlgtype = c4d.DLG_TYPE_ASYNC)
        return True

    def RestoreLayout(self, secret):
        c4d.WriteConsole("restore layout \n")
        return True


