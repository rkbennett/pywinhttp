# pywinhttp

## winhttp wrapper in Python

`pywinhttp` enables the use of winhttp api functionality in python. Namely, auto-authentication and resolution for proxies.

## Basic Usage

### Post request example

```python
import json
from winhttp import Request, opener
req = Request("https://foobarbaz.com", userAgent="foobarbaz", headers={"foo":"bar"}, http_version=1.0, method="POST")
data = json.dumps({"foo":"bar"}).encode()
resp = opener(req, data=data, timeout=15, verfiy=False)
```

### Get request example

```python
from winhttp import Request, opener
req = Request("https://foobarbaz.com", userAgent="foobarbaz")
resp = opener(req, timeout=10)
```

## Request Options

* `url` - first positional argument, which is the url/uri of the target
* `userAgent` - user agent of request, defaults to `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36`
* `securityLevel` - security level for request (one of `high`, `medium`, or `low`)
* `headers` - a `dict` of headers as key value pairs
* `http_version` - version of http to use (must be one of 1.0 or 1.1)
* `method` - one of (`GET`, `POST`, or `PUT`), defaults to `GET` unless `data` is provided to the `opener` then defaults to `POST`

## Opener Options

* `target` - first positional argument, one of a winhttp.Request object or a url/uri string of a target
* `data` - a bytes object which is used in `POST` and `PUT` requests
* `timeout` - timeout in seconds for the request (defaults to 60s)
* `verify` - `bool` whether or not to verify certificate/s of the target