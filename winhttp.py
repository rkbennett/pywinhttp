import ctypes
import ctypes.wintypes

class WINHTTP_CURRENT_USER_IE_PROXY_CONFIG(ctypes.Structure):
    _fields_ = [
        ("AutoDetect", ctypes.wintypes.BOOL),
        ("AutoConfigUrl", ctypes.wintypes.LPWSTR),
        ("Proxy", ctypes.wintypes.LPWSTR),
        ("ProxyBypass", ctypes.wintypes.LPWSTR)
    ]

INTERNET_PORT = ctypes.c_uint
WINHTTP_AUTH_TARGET_PROXY = ctypes.wintypes.DWORD(1)
WINHTTP_NO_PROXY_NAME = None
WINHTTP_NO_PROXY_BYPASS = None
winhttp = ctypes.windll.winhttp
winhttp.WinHttpGetIEProxyConfigForCurrentUser.restypes = ctypes.wintypes.BOOL
winhttp.WinHttpGetIEProxyConfigForCurrentUser.argtypes = [
    ctypes.POINTER(WINHTTP_CURRENT_USER_IE_PROXY_CONFIG)
]
winhttp.WinHttpSetCredentials.restypes = ctypes.wintypes.BOOL
winhttp.WinHttpSetCredentials.argtypes = [
    ctypes.HANDLE,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.LPWSTR,
    ctypes.wintypes.LPWSTR,
    ctypes.wintypes.LPVOID
]
winhttp.WinHttpOpen.restypes = ctypes.wintypes.HANDLE
winhttp.WinHttpOpen.argtypes = [
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.DWORD,
]
winhttp.WinHttpConnect.restypes = ctypes.wintypes.HANDLE
winhttp.WinHttpConnect.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.LPCWSTR,
    INTERNET_PORT,
    ctypes.wintypes.DWORD
]












hSession = winhttp.WinHttpOpen(
    "Testing stuff fo sho",
    4,
    WINHTTP_NO_PROXY_NAME
    WINHTTP_NO_PROXY_BYPASS,
    0
)

if not hSession:
    raise ValueError("Failed")

hConnect = WinHttpConnect(
    hSession,
    "www.google.com",
    0,
    0
)






proxy_config = WINHTTP_CURRENT_USER_IE_PROXY_CONFIG()
resp = winhttp.WinHttpGetIEProxyConfigForCurrentUser(
    ctypes.byref(proxy_config)
)

#resp = winhttp.WinHttpSetCredentials(
#    ctypes.HANDLE(0),
#    WINHTTP_AUTH_TARGET_PROXY,
#)
