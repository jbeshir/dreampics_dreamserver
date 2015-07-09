A very simple service for generating deepdream images on request, made by gluing bat-country and web.py together. Depends on both those two things being installed, along with their dependencies.

To setup:

- Ensure bat-country and web.py and everything they depend on are available.
- Download the bvlc_googlenet caffe model.
- Set the PYTHONPATH environmental variable as required to run bat-country's demo.py successfully.
- Clone this repository to some location.
- Set the CAFFE_HOME environmental variable to the location that Caffe is installed to.
- Set the DREAMSERVER_HOME environmental variable to the location that this repository was cloned to.
- Get a TLS certificate for the hostname you're planning on running on.
- Copy config.py.example to config.py and fill it out, setting the auth code required to use the service.
- Run main.py.

Once you've confirmed the server works, you may optionally set up a crontab to automatically run cron.sh to keep the server running.
