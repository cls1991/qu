# coding: utf8

"""
    quick-url: Simply upload image, then return a unique url.
               Currently only qiniu is supported.
"""

import ConfigParser

from qiniu import (
    Auth, etag, put_file
)

access_key = '$ACCESS_KEY'
secret_key = '$SECRET_KEY'

q = Auth(access_key, secret_key)

bucket_name = '$BUCKET_NAME'

key = 'sample.png'

token = q.upload_token(bucket_name, key, 3600)

local_file = '/somewhere/6747182.png'

ret, info = put_file(token, key, local_file)
print(ret)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(local_file)
