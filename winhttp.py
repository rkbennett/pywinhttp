import ctypes
import ctypes.wintypes
 
winhttp = ctypes.windll.winhttp
 
WINHTTP_ACCESS_TYPE_AUTOMATIC_PROXY = 4
WINHTTP_NO_PROXY_NAME = None
WINHTTP_NO_PROXY_BYPASS = None
WINHTTP_FLAG_ASYNC = 0
 
winhttp.WinHttpOpen.restype = ctypes.wintypes.HANDLE
winhttp.WinHttpOpen.argtypes = [
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.DWORD,
]
 
winhttp.WinHttpConnect.restype = ctypes.wintypes.HANDLE
winhttp.WinHttpConnect.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.LPCWSTR,
    ctypes.c_uint,
    ctypes.wintypes.DWORD
]
 
winhttp.WinHttpOpenRequest.restype = ctypes.wintypes.HANDLE
winhttp.WinHttpOpenRequest.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.DWORD
]
 
winhttp.WinHttpSendRequest.restype = ctypes.wintypes.BOOL
winhttp.WinHttpSendRequest.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.LPVOID,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.DWORD,
    ctypes.c_void_p
]
 
winhttp.WinHttpReceiveResponse.restype = ctypes.wintypes.BOOL
winhttp.WinHttpReceiveResponse.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.LPVOID
]
 
winhttp.WinHttpReadData.restype = ctypes.wintypes.BOOL
 
 
hInternet = winhttp.WinHttpOpen(
    ctypes.wintypes.LPCWSTR("Testing"),
    WINHTTP_ACCESS_TYPE_AUTOMATIC_PROXY,
    WINHTTP_NO_PROXY_NAME,
    WINHTTP_NO_PROXY_BYPASS, 
    WINHTTP_FLAG_ASYNC
)
 
hConnect = winhttp.WinHttpConnect(
    hInternet,
    "raw.githubusercontent.com",
    0,
    0
)
 
hRequest = winhttp.WinHttpOpenRequest(
    ctypes.c_void_p(hConnect),
    ctypes.c_wchar_p("GET"),
    ctypes.c_wchar_p("/operatorequals/httpimport/master/httpimport.py"),
    ctypes.c_wchar_p(None),
    ctypes.c_wchar_p(None),
    ctypes.c_wchar_p(None),
    ctypes.wintypes.DWORD(0x00000000)
)
 
headerBuffer = ctypes.c_void_p()
 
resp = winhttp.WinHttpSendRequest(
    hRequest,
    None,
    0,
    headerBuffer,
    0,
    0,
    0
)
 
resp = winhttp.WinHttpReceiveResponse(
    hRequest,
    None
)
 
 
bytesAvailable = ctypes.c_ulong(0)
 
winhttp.WinHttpQueryDataAvailable.restype = ctypes.wintypes.BOOL
resp = winhttp.WinHttpQueryDataAvailable(
    ctypes.wintypes.HANDLE(hRequest),
    ctypes.byref(bytesAvailable)
)
 
payload = b""
 
while bytesAvailable.value:
    readBuffer = (ctypes.c_ubyte * bytesAvailable.value)()
    bytesToRead = ctypes.wintypes.DWORD(bytesAvailable.value)
    bytesRead = ctypes.wintypes.DWORD(0)
    resp = winhttp.WinHttpReadData(
        ctypes.c_void_p(hRequest),
        ctypes.byref(readBuffer),
        bytesToRead,
        ctypes.byref(bytesRead)
    )
    payload += bytes(readBuffer)
    resp = winhttp.WinHttpQueryDataAvailable(
        ctypes.wintypes.HANDLE(hRequest),
        ctypes.byref(bytesAvailable)
    )
 
 
payload = payload.decode()
