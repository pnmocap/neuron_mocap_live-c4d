import sys, os, importlib
import c4d

sys.path.insert(0, os.path.dirname(__file__))

from neuron_command import *
from neuron_defs import *
from neuron_tag import *
from neuron_message import *
import neuron_connection

def PluginMessage(id, data):
    if id == c4d.C4DPL_RELOADPYTHONPLUGINS or id == c4d.C4DPL_ENDACTIVITY:
        neuron_connection.Finalize()
        return True
    return False


def RegisterNeuronMocapLive():
    bmp = c4d.bitmaps.BaseBitmap()
    bmp.InitWith(GetResPath("neuron.png"))

    c4d.plugins.RegisterCommandPlugin(
        id = PLUGIN_ID_COMMAND, 
        str = PLUGIN_NAME_COMMAND,
        info = 0,
        icon = bmp,
        help = None,
        dat = NeuronCommandData()
    )
    
    c4d.plugins.RegisterTagPlugin(
        id = PLUGIN_ID_TAG,
        str = PLUGIN_NAME_TAG,
        info = c4d.TAG_EXPRESSION | c4d.TAG_VISIBLE,
        g = NeuronTagData,
        description = "tpyneurontag",
        icon = bmp
    )

    c4d.plugins.RegisterMessagePlugin(
        id = PLUGIN_ID_MESSAGE,
        str = PLUGIN_NAME_MESSAGE,
        info = 0,
        dat = NeuronMessageData()
    )

    neuron_connection.Initialize()

if __name__ == "__main__":
    RegisterNeuronMocapLive()

