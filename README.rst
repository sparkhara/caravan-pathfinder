caravan pathfinder
==================

this application assists in pushing data to the whirlwind caravan. it
will read messages from an amqp message broker queue and send those
messages to a local socket.

installation
------------

1. ``pip install -r requirements.txt``
2. ``python caravan_pathfinder.py -h``

usage
-----

to begin the pathfinder, run the following:

::

    $ python caravan_pathfinder.py --port 1984 --url amqp://127.0.0.1/ \
      --queue my_topic

when started it will wait until a connection is made to the local
socket before processing will begin.
