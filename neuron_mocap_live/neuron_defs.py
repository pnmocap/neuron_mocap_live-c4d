PLUGIN_ID_COMMAND = 1058716
PLUGIN_NAME_COMMAND = "Neuron Mocap Live"
PLUGIN_VERSION = "1.0.0 Preview"

PLUGIN_ID_TAG = 1058715
PLUGIN_NAME_TAG = "Neuron Mocap Live"

PLUGIN_ID_MESSAGE = 1058717
PLUGIN_NAME_MESSAGE = "Neuron Mocap Message"

ID_COREMESSAGE_FRAME_ARRIVED = PLUGIN_ID_MESSAGE 

ID_DLGCTRL_GROUP_MAIN = 1000

ID_DLGCTRL_GROUP_CONNECTION = 1001
ID_DLGCTRL_LABEL_IP = 1002
ID_DLGCTRL_EDIT_IP = 1003
ID_DLGCTRL_LABEL_PORT = 1004
ID_DLGCTRL_EDIT_PORT = 1005
ID_DLGCTRL_LABEL_SKELETON = 1006
ID_DLGCTRL_COMBO_BOX_SKELETON = 1007
ID_DLGCTRL_COMBO_BOX_SKELETON_AXIS_STUDIO = 1008
ID_DLGCTRL_COMBO_BOX_SKELETON_AXIS_LEGACY = 1009
ID_DLGCTRL_BUTTON_CONNECT = 1200
ID_DLGCTRL_BUTTON_DISCONNECT = 1201
ID_DLGCTRL_LABEL_PROTOCOL = 1202
ID_DLGCTRL_COMBO_BOX_PROTOCOL = 1203
ID_DLGCTRL_COMBO_BOX_PROTOCOL_UDP = 1204
ID_DLGCTRL_COMBO_BOX_PROTOCOL_TCP = 1205

ID_DLGCTRL_GROUP_SKELETON = 2000
ID_DLGCTRL_BUTTON_CREATE_AXIS_STUDIO_SKELETON = 2001
ID_DLGCTRL_BUTTON_CREATE_AXIS_LEGACY_SKELETON = 2002

ID_DLGCTRL_GROUP_RECORDING = 3000
ID_DLGCTRL_BUTTON_BEGIN_RECORD = 3001
ID_DLGCTRL_BUTTON_END_RECORD = 3002

ID_TAG_CHARACTER_GROUP = 2000
ID_TAG_CHARACTER_NAME = 2001
ID_TAG_SET_T_POSE = 2002
ID_TAG_GOTO_T_POSE = 2003

ID_TAG_JOINTS_CONTROL_GROUP = 2004
ID_TAG_DETECT_JOINTS = 2005
ID_TAG_CLEAR_JOINTS = 2006
ID_TAG_SCALE_ROOT_POSITION = 2007

ID_TAG_JOINTS_GROUP = 3001
ID_TAG_CHARACTER_JOINTS = 3002

ID_TAG_T_POSE_MATRIX = 4001

ID_TAG_CHARACTER_JOINTS_NAME = 5001

NEURON_JOINTS = [
    'Hips',
    'RightUpLeg',
    'RightLeg',
    'RightFoot',
    'LeftUpLeg',
    'LeftLeg',
    'LeftFoot',
    'Spine',
    'Spine1',
    'Spine2',
    'Spine3',
    'Neck',
    'Neck1',
    'Head',
    'RightShoulder',
    'RightArm',
    'RightForeArm',
    'RightHand',
    'RightHandThumb1',
    'RightHandThumb2',
    'RightHandThumb3',
    'RightInHandIndex',
    'RightHandIndex1',
    'RightHandIndex2',
    'RightHandIndex3',
    'RightInHandMiddle',
    'RightHandMiddle1',
    'RightHandMiddle2',
    'RightHandMiddle3',
    'RightInHandRing',
    'RightHandRing1',
    'RightHandRing2',
    'RightHandRing3',
    'RightInHandPinky',
    'RightHandPinky1',
    'RightHandPinky2',
    'RightHandPinky3',
    'LeftShoulder',
    'LeftArm',
    'LeftForeArm',
    'LeftHand',
    'LeftHandThumb1',
    'LeftHandThumb2',
    'LeftHandThumb3',
    'LeftInHandIndex',
    'LeftHandIndex1',
    'LeftHandIndex2',
    'LeftHandIndex3',
    'LeftInHandMiddle',
    'LeftHandMiddle1',
    'LeftHandMiddle2',
    'LeftHandMiddle3',
    'LeftInHandRing',
    'LeftHandRing1',
    'LeftHandRing2',
    'LeftHandRing3',
    'LeftInHandPinky',
    'LeftHandPinky1',
    'LeftHandPinky2',
    'LeftHandPinky3'
]

NEURON_JOINTS_INDEX_MAP = { 
    NEURON_JOINTS[i] : i for i in range(0, len(NEURON_JOINTS))
}