#!/usr/bin/python
import io, os, sys
import web

from batcountry import BatCountry
from PIL import Image
import numpy as np

import config

from web.wsgiserver import CherryPyWSGIServer

CherryPyWSGIServer.ssl_certificate = config.ssl_certificate
CherryPyWSGIServer.ssl_private_key = config.ssl_private_key

urls = (
    '/dream', 'dream'
)

class dream:
    def POST(self):
        data = web.input(auth_code='', image={})
        if data.auth_code == '':
            raise web.Forbidden()

        if data.auth_code != config.auth_code:
            raise web.Forbidden()

        if 'image' not in data:
            raise web.BadRequest()

        
        input_image = Image.open(data['image'].file)

        bc = BatCountry(os.environ['CAFFE_ROOT'] + '/models/bvlc_googlenet')

        result_data = bc.dream(np.float32(input_image),
            end='inception_3b/5x5_reduce')

        bc.cleanup()

        result_image = Image.fromarray(np.uint8(result_data))
        result = io.BytesIO()
        result_image.save(result, 'PNG')
        result.seek(0)

        web.header('Content-type', 'image/png') 
        return result.read()


if __name__ == "__main__":

    if config.auth_code == 'code':
        # :|
        sys.exit('Config error: You must set the auth code in config.py to something unique and unguessable.')

    app = web.application(urls, globals())
    app.run()
