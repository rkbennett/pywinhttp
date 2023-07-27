import ctypes
import ctypes.wintypes

winhttp = ctypes.windll.winhttp

WINHTTP_ACCESS_TYPE_AUTOMATIC_PROXY = 4
WINHTTP_NO_PROXY_NAME = None
WINHTTP_NO_PROXY_BYPASS = None
WINHTTP_FLAG_ASYNC = 0
WINHTTP_AUTH_TARGET_PROXY = 1
WINHTTP_AUTH_SCHEME_NEGOTIATE = 16
WINHTTP_AUTOLOGON_SECURITY_LEVEL_LOW = ctypes.wintypes.DWORD(1)
WINHTTP_AUTOLOGON_SECURITY_LEVEL_MEDIUM = ctypes.wintypes.DWORD(0)
WINHTTP_AUTOLOGON_SECURITY_LEVEL_HIGH = ctypes.wintypes.DWORD(2)
WINHTTP_OPTION_AUTOLOGON_POLICY = 77
WINHTTP_QUERY_RAW_HEADERS = WINHTTP_QUERY_EX_ALL_HEADERS = 21
WINHTTP_QUERY_RAW_HEADERS_CRLF = 22
WINHTTP_QUERY_CUSTOM = 65535
WINHTTP_QUERY_FLAG_WIRE_ENCODING = 16777216

errors = {
    6: "ERROR_INVALID_HANDLE",
    12001: "ERROR_WINHTTP_OUT_OF_HANDLES",
    12002: "ERROR_WINHTTP_TIMEOUT",
    12004: "ERROR_WINHTTP_INTERNAL_ERROR",
    12005: "ERROR_WINHTTP_INVALID_URL",
    12006: "ERROR_WINHTTP_UNRECOGNIZED_SCHEME",
    12007: "ERROR_WINHTTP_NAME_NOT_RESOLVED",
    12009: "ERROR_WINHTTP_INVALID_OPTION",
    12011: "ERROR_WINHTTP_OPTION_NOT_SETTABLE",
    12012: "ERROR_WINHTTP_SHUTDOWN",
    12015: "ERROR_WINHTTP_LOGIN_FAILURE",
    12017: "ERROR_WINHTTP_OPERATION_CANCELLED",
    12018: "ERROR_WINHTTP_INCORRECT_HANDLE_TYPE",
    12019: "ERROR_WINHTTP_INCORRECT_HANDLE_STATE",
    12029: "ERROR_WINHTTP_CANNOT_CONNECT",
    12030: "ERROR_WINHTTP_CONNECTION_ERROR",
    12032: "ERROR_WINHTTP_RESEND_REQUEST",
    12037: "ERROR_WINHTTP_SECURE_CERT_DATE_INVALID",
    12038: "ERROR_WINHTTP_SECURE_CERT_CN_INVALID",
    12044: "ERROR_WINHTTP_CLIENT_AUTH_CERT_NEEDED",
    12045: "ERROR_WINHTTP_SECURE_INVALID_CA",
    12057: "ERROR_WINHTTP_SECURE_CERT_REV_FAILED",
    12100: "ERROR_WINHTTP_CANNOT_CALL_BEFORE_OPEN",
    12101: "ERROR_WINHTTP_CANNOT_CALL_BEFORE_SEND",
    12102: "ERROR_WINHTTP_CANNOT_CALL_AFTER_SEND",
    12103: "ERROR_WINHTTP_CANNOT_CALL_AFTER_OPEN",
    12150: "ERROR_WINHTTP_HEADER_NOT_FOUND",
    12152: "ERROR_WINHTTP_INVALID_SERVER_RESPONSE",
    12153: "ERROR_WINHTTP_INVALID_HEADER",
    12154: "ERROR_WINHTTP_INVALID_QUERY_REQUEST",
    12155: "ERROR_WINHTTP_HEADER_ALREADY_EXISTS",
    12156: "ERROR_WINHTTP_REDIRECT_FAILED",
    12157: "ERROR_WINHTTP_SECURE_CHANNEL_ERROR",
    12166: "ERROR_WINHTTP_BAD_AUTH_PROXY_SCRIPT",
    12167: "ERROR_WINHTTP_UNABLE_TO_DOWNLOAD_SCRIPT",
    12169: "ERROR_WINHTTP_SECURE_INVALID_CERT",
    12170: "ERROR_WINHTTP_SECURE_CERT_REVOKED",
    12172: "ERROR_WINHTTP_NOT_INITIALIZED",
    12175: "ERROR_WINHTTP_SECURE_FAILURE",
    12178: "ERROR_WINHTTP_AUTO_PROXY_SERVICE_ERROR",
    12179: "ERROR_WINHTTP_SECURE_CERT_WRONG_USAGE",
    12180: "ERROR_WINHTTP_AUTODETECTION_FAILED",
    12181: "ERROR_WINHTTP_HEADER_COUNT_EXCEEDED",
    12182: "ERROR_WINHTTP_HEADER_SIZE_OVERFLOW",
    12183: "ERROR_WINHTTP_CHUNKED_ENCODING_HEADER_SIZE_OVERFLOW",
    12184: "ERROR_WINHTTP_RESPONSE_DRAIN_OVERFLOW",
    12185: "ERROR_WINHTTP_CLIENT_CERT_NO_PRIVATE_KEY",
    12186: "ERROR_WINHTTP_CLIENT_CERT_NO_ACCESS_PRIVATE_KEY"
}

securityLevels = {
    "low": WINHTTP_AUTOLOGON_SECURITY_LEVEL_LOW,
    "medium": WINHTTP_AUTOLOGON_SECURITY_LEVEL_MEDIUM,
    "high": WINHTTP_AUTOLOGON_SECURITY_LEVEL_HIGH
}

class WINHTTP_HEADER_NAME(ctypes.Union):
    _fields_ = [
        ("pwszName",ctypes.c_wchar_p),
        ("pszName",ctypes.c_char_p),
    ]

class WINHTTP_HEADER_VALUE(ctypes.Union):
    _fields_ = [
        ("pwszValue",ctypes.c_wchar_p),
        ("pszValue",ctypes.c_char_p),
    ]

class WINHTTP_EXTENDED_HEADER(ctypes.Structure):
    _anonymous_ = (
        "WINHTTP_HEADER_NAME", 
        "WINHTTP_HEADER_VALUE"
    )

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

winhttp.WinHttpQueryHeaders.restype = ctypes.wintypes.BOOL
winhttp.WinHttpQueryHeaders.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.LPCWSTR,
    ctypes.c_void_p,
    ctypes.wintypes.LPDWORD,
    ctypes.wintypes.LPDWORD
]

winhttp.WinHttpQueryDataAvailable.restype = ctypes.wintypes.BOOL
winhttp.WinHttpQueryDataAvailable.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.LPDWORD
]

winhttp.WinHttpReadData.restype = ctypes.wintypes.BOOL
winhttp.WinHttpReadData.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.LPVOID,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.LPDWORD
]

winhttp.WinHttpCloseHandle.restype = ctypes.wintypes.BOOL
winhttp.WinHttpCloseHandle.argtypes = [
    ctypes.wintypes.HANDLE
]

winhttp.WinHttpSetOption.restype = ctypes.wintypes.BOOL
winhttp.WinHttpSetOption.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.LPVOID,
    ctypes.wintypes.DWORD
]

winhttp.WinHttpSetCredentials.restype = ctypes.wintypes.BOOL
winhttp.WinHttpSetCredentials.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.LPCWSTR,
    ctypes.wintypes.LPVOID
]

class request(object):
    def __init__(self):
        self.hInternet = None
        self.hConnect = None
        self.hRequest = None
        self.headers = None
        self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"


    def raise_error(self, error_code):
        if error_code in errors:
            raise WindowsError(f"[{error_code}] {errors[error_code]}")
        else:
            raise WindowsError(f"[{error_code}] Unknown error")

    def Request(self, url, userAgent=None, data=None, securityLevel="medium"):
        if userAgent:
            self.userAgent = userAgent

        if not data:
            self.method = "GET"

        if securityLevel.lower() not in ["low", "medium", "high"]:
            self.securityLevel = securityLevels["medium"]
        else:
            self.securityLevel = securityLevels[securityLevel.lower()]

        spliturl = url.split('http://')[-1].split('https://')[-1].split('/')
        hostname = spliturl[0]
        path = "/" + "/".join(spliturl[1:])

        self.hInternet = winhttp.WinHttpOpen(
            ctypes.wintypes.LPCWSTR(self.userAgent),
            WINHTTP_ACCESS_TYPE_AUTOMATIC_PROXY,
            WINHTTP_NO_PROXY_NAME,
            WINHTTP_NO_PROXY_BYPASS, 
            WINHTTP_FLAG_ASYNC
        )

        if not self.hInternet or int(self.hInternet) < 1:
            self.raise_error(ctypes.GetLastError())

        self.hConnect = winhttp.WinHttpConnect(
            self.hInternet,
            hostname,
            0,
            0
        )

        if not self.hConnect or int(self.hConnect) < 1:
            self.raise_error(ctypes.GetLastError())

        self.hRequest = winhttp.WinHttpOpenRequest(
            ctypes.c_void_p(self.hConnect),
            ctypes.c_wchar_p(self.method),
            ctypes.c_wchar_p(path),
            ctypes.c_wchar_p(None),
            ctypes.c_wchar_p(None),
            ctypes.c_wchar_p(None),
            ctypes.wintypes.DWORD(0x00000000)
        )

        if not self.hRequest or self.hRequest < 1:
            self.raise_error(ctypes.GetLastError())

        result = winhttp.WinHttpSetOption(
            self.hRequest,
            WINHTTP_OPTION_AUTOLOGON_POLICY,
            ctypes.byref(self.securityLevel),
            ctypes.sizeof(self.securityLevel)
        )

        #result = winhttp.WinHttpSetCredentials(
        #    self.hRequest,
        #    WINHTTP_AUTH_TARGET_PROXY,
        #    WINHTTP_AUTH_SCHEME_NEGOTIATE,
        #    None,
        #    None,
        #    None
        #)

        if not result:
            self.raise_error(ctypes.GetLastError())

    def read(self):
        headerBuffer = ctypes.c_void_p()

        result = winhttp.WinHttpSendRequest(
            self.hRequest,
            None,
            0,
            headerBuffer,
            0,
            0,
            0
        )

        if not result:
            self.raise_error(ctypes.GetLastError())

        result = winhttp.WinHttpReceiveResponse(
            self.hRequest,
            None
        )

        if not result:
            self.raise_error(ctypes.GetLastError())

        try:
            winhttp.WinHttpQueryHeadersEx.restype = ctypes.wintypes.DWORD
            headerStruct = WINHTTP_EXTENDED_HEADER()
            headerCount = ctypes.wintypes.DWORD()
            headerBuffer = (ctypes.c_ubyte * 9999)()
            result = winhttp.WinHttpQueryHeadersEx(
                ctypes.wintypes.HANDLE(self.hRequest),
                ctypes.wintypes.DWORD(WINHTTP_QUERY_EX_ALL_HEADERS),
                ctypes.c_ulonglong(0),
                ctypes.c_uint(0),
                ctypes.wintypes.PDWORD(None),
                None, #byref(winhttp_header),
                ctypes.byref(headerBuffer),
                ctypes.wintypes.PDWORD(ctypes.sizeof(headerBuffer)),
                ctypes.wintypes.HANDLE(headerStruct),
                ctypes.byref(headerCount)
            )
        except AttributeError as e:
            headerBuffer = (ctypes.c_ubyte * 9999)()
            result = winhttp.WinHttpQueryHeaders(
                self.hRequest,
                WINHTTP_QUERY_RAW_HEADERS_CRLF,
                None,
                ctypes.byref(headerBuffer),
                ctypes.wintypes.DWORD(ctypes.sizeof(headerBuffer)),
                None
            )

        if not result:
            self.raise_error(ctypes.GetLastError())

        rawHeaders = bytes(headerBuffer)[0:1998].decode('utf-16').rstrip('\0').split('\r\n')[1:-2]
        self.responseHeaders = [{header.split(':')[0]:header.split(':')[1].lstrip()} for header in rawHeaders]

        bytesAvailable = ctypes.c_ulong(0)

        result = winhttp.WinHttpQueryDataAvailable(
            self.hRequest,
            bytesAvailable
        )

        if not result:
            self.raise_error(ctypes.GetLastError())

        payload = b""

        while bytesAvailable.value:
            readBuffer = (ctypes.c_ubyte * bytesAvailable.value)()
            bytesToRead = bytesAvailable.value
            bytesRead = ctypes.wintypes.DWORD(0)
            result = winhttp.WinHttpReadData(
                self.hRequest,
                readBuffer,
                bytesToRead,
                bytesRead
            )
            if not result:
                self.raise_error(ctypes.GetLastError())
            payload += bytes(readBuffer)
            result = winhttp.WinHttpQueryDataAvailable(
                self.hRequest,
                bytesAvailable
            )
            if not result:
                self.raise_error(ctypes.GetLastError())

        return payload.decode()

    def close(self):
        result = winhttp.WinHttpCloseHandle(
            self.hInternet
        )

        self.hInternet = None

        if not result:
            raise_error(ctypes.GetLastError())
