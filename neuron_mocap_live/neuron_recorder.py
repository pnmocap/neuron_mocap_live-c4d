__all__ = (
    "Recording",
    "BeginRecord",
    "EndRecord",

)

import c4d
import time

m_recording = False
m_start_time = None

def IsRecording():
    global m_recording
    return m_recording

def BeginRecord():
    global m_start_time, m_recording, m_fps
    m_start_time = time.time()
    m_recording = True

def EndRecord():
    global m_recording 
    m_recording = False

def GetKeyTime():
    global m_start_time, m_fps
    if m_start_time is None:
        return c4d.BaseTime(0)
    return c4d.BaseTime((time.time() - m_start_time) * 1000, 1000)