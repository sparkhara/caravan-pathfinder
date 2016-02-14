caravan pathfinder
==================

this application assists in pushing data to the whirlwind caravan. it
will read messages from an amqp message broker queue and send those
messages to a local socket.

installation
------------

this application is intended to be built as an openshift
source-to-image image. for more information on source-to-image, please
see https://github.com/openshift/source-to-image

to build and run this application with s2i and docker, use the
following commands (or something similar to your settings):

::

    $ s2i build https://github.com/sparkhara/caravan-pathfinder \
      openshift/python-27-centos7 caravan-pathfinder-centos7

    (... lots of build exhaust ...)

    $ docker run --rm -i -t -p 1984:1984 \
      -e PATHFINDER_BROKER_URL=amqp://127.0.0.1/ \
      caravan-pathfinder-centos7

    (log output from caravan-pathfinder)

when started it will wait until a connection is made to the local
socket before processing will begin.
