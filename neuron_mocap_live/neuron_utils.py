import os

def GetResPath(res_name):
    return os.path.join(os.path.dirname(__file__), "res", res_name)
