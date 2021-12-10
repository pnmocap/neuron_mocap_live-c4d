import c4d
from neuron_defs import *
from neuron_utils import *
import neuron_connection
import neuron_recorder

class NeuronCommandDialog(c4d.gui.GeDialog):
    
    def CreateLayout(self):
        self.SetTitle(f"{PLUGIN_NAME_COMMAND} {PLUGIN_VERSION}")

        if self.GroupBegin(id = ID_DLGCTRL_GROUP_MAIN, flags = c4d.BFH_SCALEFIT | c4d.BFV_TOP, cols = 1, rows = 3):
            self.GroupBorderSpace(0, 0, 0, 9)
            if self.GroupBegin(id = ID_DLGCTRL_GROUP_CONNECTION, flags = c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, cols = 2, rows = 5, title = "Connection Settings"):
                self.GroupBorderSpace(25, 9, 25, 9)
                self.GroupBorderNoTitle(c4d.BORDER_WITH_TITLE_BOLD)

                self.AddStaticText(id = ID_DLGCTRL_LABEL_PROTOCOL, flags = c4d.BFH_SCALEFIT, name = "Protocol")
                self.AddComboBox(id = ID_DLGCTRL_COMBO_BOX_PROTOCOL, flags = c4d.BFH_SCALEFIT)
                self.AddChild(ID_DLGCTRL_COMBO_BOX_PROTOCOL, ID_DLGCTRL_COMBO_BOX_PROTOCOL_TCP, "TCP")
                self.AddChild(ID_DLGCTRL_COMBO_BOX_PROTOCOL, ID_DLGCTRL_COMBO_BOX_PROTOCOL_UDP, "UDP")
                if neuron_connection.GetProtocol() == "TCP":
                    self.SetInt32(ID_DLGCTRL_COMBO_BOX_PROTOCOL, ID_DLGCTRL_COMBO_BOX_PROTOCOL_TCP)
                else:
                    self.SetInt32(ID_DLGCTRL_COMBO_BOX_PROTOCOL, ID_DLGCTRL_COMBO_BOX_PROTOCOL_UDP)

                self.AddStaticText(id = ID_DLGCTRL_LABEL_IP, flags = c4d.BFH_SCALEFIT, name = "IP")
                self.AddEditText(id = ID_DLGCTRL_EDIT_IP, flags = c4d.BFH_SCALEFIT)
                self.SetString(ID_DLGCTRL_EDIT_IP, neuron_connection.GetServerIp())

                self.AddStaticText(id = ID_DLGCTRL_LABEL_IP, flags = c4d.BFH_SCALEFIT, name = "Port")
                self.AddEditText(id = ID_DLGCTRL_EDIT_PORT, flags = c4d.BFH_SCALEFIT)
                self.SetString(ID_DLGCTRL_EDIT_PORT, str(neuron_connection.GetServerPort()))

                self.AddStaticText(id = ID_DLGCTRL_LABEL_SKELETON, flags = c4d.BFH_SCALEFIT, name = "Skeleton")
                self.AddComboBox(id = ID_DLGCTRL_COMBO_BOX_SKELETON, flags = c4d.BFH_SCALEFIT)
                self.AddChild(ID_DLGCTRL_COMBO_BOX_SKELETON, ID_DLGCTRL_COMBO_BOX_SKELETON_AXIS_STUDIO, "Axis Studio")
                self.AddChild(ID_DLGCTRL_COMBO_BOX_SKELETON, ID_DLGCTRL_COMBO_BOX_SKELETON_AXIS_LEGACY, "Axis Legacy")
                if neuron_connection.GetSkeleton() == "Axis Legacy":
                    self.SetInt32(ID_DLGCTRL_COMBO_BOX_SKELETON, ID_DLGCTRL_COMBO_BOX_SKELETON_AXIS_LEGACY)
                else:
                    self.SetInt32(ID_DLGCTRL_COMBO_BOX_SKELETON, ID_DLGCTRL_COMBO_BOX_SKELETON_AXIS_STUDIO)

                self.AddButton(id = ID_DLGCTRL_BUTTON_CONNECT, flags = c4d.BFH_SCALEFIT, name = "Connect")
                self.AddButton(id = ID_DLGCTRL_BUTTON_DISCONNECT, flags = c4d.BFH_SCALEFIT, name = "Disconnect")

                self.Enable(ID_DLGCTRL_COMBO_BOX_PROTOCOL, not neuron_connection.IsConnecting())
                self.Enable(ID_DLGCTRL_EDIT_IP, not neuron_connection.IsConnecting())
                self.Enable(ID_DLGCTRL_EDIT_PORT, not neuron_connection.IsConnecting())
                self.Enable(ID_DLGCTRL_COMBO_BOX_SKELETON, not neuron_connection.IsConnecting())
                self.Enable(ID_DLGCTRL_BUTTON_CONNECT, not neuron_connection.IsConnecting())
                self.Enable(ID_DLGCTRL_BUTTON_DISCONNECT, neuron_connection.IsConnecting())

                self.GroupEnd() # connection group

            if self.GroupBegin(id = ID_DLGCTRL_GROUP_SKELETON, flags = c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, cols = 1, rows = 2, title = "Skeleton Building"):
                self.GroupBorderSpace(25, 9, 25, 9)
                self.GroupBorderNoTitle(c4d.BORDER_WITH_TITLE_BOLD)

                self.AddButton(id = ID_DLGCTRL_BUTTON_CREATE_AXIS_STUDIO_SKELETON, flags = c4d.BFH_SCALEFIT, name = "Create Axis Studio Skeleton")
                self.AddButton(id = ID_DLGCTRL_BUTTON_CREATE_AXIS_LEGACY_SKELETON, flags = c4d.BFH_SCALEFIT, name = "Create Axis Legacy Skeleton")
                self.GroupEnd() # skeleton group

            if self.GroupBegin(id = ID_DLGCTRL_GROUP_RECORDING, flags = c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, cols = 2, rows = 1, title = "Recording"):
                self.GroupBorderSpace(25, 9, 25, 9)
                self.GroupBorderNoTitle(c4d.BORDER_WITH_TITLE_BOLD)

                self.AddButton(id = ID_DLGCTRL_BUTTON_BEGIN_RECORD, flags = c4d.BFH_SCALEFIT, name = "Begin Record")
                self.AddButton(id = ID_DLGCTRL_BUTTON_END_RECORD, flags = c4d.BFH_SCALEFIT, name = "End Record")

                self.Enable(ID_DLGCTRL_GROUP_RECORDING, neuron_connection.IsConnecting())
                self.Enable(ID_DLGCTRL_BUTTON_BEGIN_RECORD, not neuron_recorder.IsRecording())
                self.Enable(ID_DLGCTRL_BUTTON_END_RECORD, neuron_recorder.IsRecording())

                self.GroupEnd() # record group

            self.GroupEnd() # main group

        return True

    def Command(self, id, msg):
        if id == ID_DLGCTRL_EDIT_IP:
            neuron_connection.SetServerIp(self.GetString(ID_DLGCTRL_EDIT_IP))
        elif id == ID_DLGCTRL_EDIT_PORT:
            neuron_connection.SetServerPort(int(self.GetString(ID_DLGCTRL_EDIT_PORT)))
        elif id == ID_DLGCTRL_COMBO_BOX_SKELETON:
            sub_id = self.GetInt32(ID_DLGCTRL_COMBO_BOX_SKELETON)
            if sub_id == ID_DLGCTRL_COMBO_BOX_SKELETON_AXIS_LEGACY:
                neuron_connection.SetSkeleton("Axis Legacy")
            else:
                neuron_connection.SetSkeleton("Axis Studio")
        elif id == ID_DLGCTRL_BUTTON_CONNECT:
            self.Connect()
        elif id == ID_DLGCTRL_BUTTON_DISCONNECT:
            self.Disconnect()
        elif id == ID_DLGCTRL_BUTTON_CREATE_AXIS_STUDIO_SKELETON:
            self.CreateSkeleton("axis_studio_skeleton.c4d")
        elif id == ID_DLGCTRL_BUTTON_CREATE_AXIS_LEGACY_SKELETON:
            self.CreateSkeleton("axis_legacy_skeleton.c4d")
        elif id == ID_DLGCTRL_BUTTON_BEGIN_RECORD:
            self.BeginRecord()
        elif id == ID_DLGCTRL_BUTTON_END_RECORD:
            self.EndRecord()
        elif id == ID_DLGCTRL_COMBO_BOX_PROTOCOL:
            sub_id = self.GetInt32(ID_DLGCTRL_COMBO_BOX_PROTOCOL)
            if sub_id == ID_DLGCTRL_COMBO_BOX_PROTOCOL_TCP:
                neuron_connection.SetProtocol("TCP")
            else:
                neuron_connection.SetProtocol("UDP")
        return True

    def Connect(self):
        if not neuron_connection.Connect():
            c4d.gui.MessageDialog("Connect failed: {0}".format(neuron_connection.GetErrorMessage()))
        self.Enable(ID_DLGCTRL_COMBO_BOX_PROTOCOL, not neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_GROUP_RECORDING, neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_EDIT_IP, not neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_EDIT_PORT, not neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_COMBO_BOX_SKELETON, not neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_BUTTON_CONNECT, not neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_BUTTON_DISCONNECT, neuron_connection.IsConnecting())

    def Disconnect(self):
        if neuron_recorder.IsRecording():
            self.EndRecord()
        neuron_connection.Disconnect()
        self.Enable(ID_DLGCTRL_COMBO_BOX_PROTOCOL, not neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_GROUP_RECORDING, neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_EDIT_IP, not neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_EDIT_PORT, not neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_COMBO_BOX_SKELETON, not neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_BUTTON_CONNECT, not neuron_connection.IsConnecting())
        self.Enable(ID_DLGCTRL_BUTTON_DISCONNECT, neuron_connection.IsConnecting())

    def BeginRecord(self):
        neuron_recorder.BeginRecord()
        self.Enable(ID_DLGCTRL_BUTTON_BEGIN_RECORD, not neuron_recorder.IsRecording())
        self.Enable(ID_DLGCTRL_BUTTON_END_RECORD, neuron_recorder.IsRecording())

    def EndRecord(self):
        neuron_recorder.EndRecord()
        self.Enable(ID_DLGCTRL_BUTTON_BEGIN_RECORD, not neuron_recorder.IsRecording())
        self.Enable(ID_DLGCTRL_BUTTON_END_RECORD, neuron_recorder.IsRecording())

    def CreateSkeleton(self, template_file):
        c4d.documents.MergeDocument(
            doc=c4d.documents.GetActiveDocument(),
            name=GetResPath(template_file),
            loadflags=c4d.SCENEFILTER_OBJECTS,
            thread=None
        )
        c4d.EventAdd()

