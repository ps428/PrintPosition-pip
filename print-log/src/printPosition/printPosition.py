from inspect import currentframe, getframeinfo

import builtins as __builtin__


def printPosition(*args, **kwargs):
    cf = currentframe()
    frameinfo = getframeinfo(cf.f_back)
    __builtin__.print("\u001b[33m","\b@"+frameinfo.filename,"\b:",  frameinfo.lineno,"\u001b[0m")
    __builtin__.print(*args, **kwargs)
