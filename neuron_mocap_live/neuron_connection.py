__all__ = (
    "SetProtocol", 
    "SetServerIp",
    "SetServerPort",
    "SetSkeleton",
    "Initialize",
    "GetErrorMessage",
    "Finalize",
    "Connect",
    "IsConnecting",
    "Disconnect", 
    "MCPAvatar",
    "GetAvatar",
    "MCPJointTag"
)

from mocap_api import *
import c4d
import time
from neuron_defs import *

m_mocap_app = None
m_protocol = "UDP"
m_skeleton = "Axis Studio"
m_ip = "127.0.0.1"
m_port = 7001
m_connecting = False
m_error_msg = str()
m_poll_thread = None
m_avatar_dict = dict()

class PollThread(c4d.threading.C4DThread):
    def Main(self):
        global m_mocap_app
        global m_avatar_dict
        while not self.TestBreak():
            mcp_evts = m_mocap_app.poll_next_event()
            avatar_updated = False
            for mcp_evt in mcp_evts:
                if mcp_evt.event_type == MCPEventType.AvatarUpdated:
                    avatar = MCPAvatar(mcp_evt.event_data.avatar_handle)
                    avatar_name = avatar.get_name()
                    c4d.threading.GeThreadLock()
                    m_avatar_dict[avatar_name] = avatar
                    c4d.threading.GeThreadUnlock()
                    avatar_updated = True

            if avatar_updated:
                c4d.SpecialEventAdd(ID_COREMESSAGE_FRAME_ARRIVED)
            time.sleep(0.001)

def GetAvatar(name):
    global m_avatar_dict
    c4d.threading.GeThreadLock()
    avatar = m_avatar_dict.get(name)
    c4d.threading.GeThreadUnlock()
    return avatar

def SetProtocol(protocol):
    global m_protocol
    m_protocol = protocol

def GetProtocol():
    global m_protocol
    return m_protocol

def SetServerIp(ip):
    global m_ip
    m_ip = ip

def GetServerIp():
    global m_ip
    return m_ip

def SetServerPort(port):
    global m_port
    m_port = port

def GetServerPort():
    global m_port
    return m_port

def SetSkeleton(skeleton):
    global m_skeleton
    m_skeleton = skeleton
    
def GetSkeleton():
    global m_skeleton
    return m_skeleton

def Initialize():
    global m_mocap_app
    m_mocap_app = MCPApplication()
    m_mocap_app.enable_event_cache()
    render_settings = MCPRenderSettings()
    render_settings.set_unit(MCPUnit.Centimeter)
    m_mocap_app.set_render_settings(render_settings)

def GetErrorMessage():
    global m_error_msg
    return m_error_msg

def Finalize():
    global m_mocap_app
    if IsConnecting():
        Disconnect()
    if m_mocap_app.is_opened():
        m_mocap_app.close()
    m_mocap_app = None

def Connect():
    global m_protocol, m_ip, m_port, m_skeleton, m_mocap_app 
    global m_error_msg, m_connecting, m_poll_thread

    settings = MCPSettings()
    if m_protocol == 'TCP':
        settings.set_tcp(m_ip, m_port)
    else:
        settings.set_udp(m_port)

    if m_skeleton == 'Axis Studio':
        settings.set_bvh_data(MCPBvhData.Binary)
    else:
        settings.set_bvh_data(MCPBvhData.BinaryLegacyHumanHierarchy)

    settings.set_bvh_rotation(MCPBvhRotation.YXZ)

    m_mocap_app.set_settings(settings)
    if m_mocap_app.is_opened():
        m_mocap_app.close()

    if m_poll_thread:
        m_poll_thread.End()
        m_poll_thread.Wait()
        m_poll_thread = None

    status, msg = m_mocap_app.open()
    if status:
        m_connecting = True
        m_error_msg = str()
        m_poll_thread = PollThread()
        m_poll_thread.Start()
    else:
        m_connecting = False
        m_error_msg = msg
    
    return m_connecting

def IsConnecting():
    global m_connecting
    return m_connecting

def Disconnect():
    global m_mocap_app, m_connecting, m_poll_thread, m_avatar_dict
    m_connecting = False
    m_mocap_app.close()
    if m_poll_thread:
        m_poll_thread.End()
        m_poll_thread.Wait(False)
        m_poll_thread = None
    m_avatar_dict.clear()