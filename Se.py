# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))