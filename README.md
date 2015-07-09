A very simple service for generating deepdream images on request, made by gluing bat-country and web.py together. Depends on both those two things being installed, along with their dependencies.

To setup, in brief:

- Install dependencies.
- Set PYTHONPATH and CAFFE_ROOT environmental variables as required to run bat-country's demo.py successfully.
- Get a TLS certificate for the hostname you're planning on running on.
- Copy config.py.example to config.py and fill it out, setting the auth code required to use the service.
- Run main.py.
