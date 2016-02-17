#!/bin/python

import argparse
import json
import logging
import socket
import time

import kombu


def accept(port):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', port))
    sock.listen(1)
    return sock.accept()


def main(url, port, queue_name):
    logging.debug('main called with url={}, port={}, queue={}'.format(
                  url, port, queue_name))
    while True:
        logging.info('waiting for connection on port {}'.format(port))
        send, send_addr = accept(port)
        logging.info('connection from: {}'.format(send_addr))
        try:
            logging.debug('gaining amqp connection')
            conn = kombu.Connection(url)
            logging.debug('configuring queue')
            queue = conn.SimpleQueue(queue_name)
            logging.debug('about to enter message loop')
            while True:
                try:
                    message = queue.get(block=False, timeout=1)
                except kombu.simple.SimpleQueue.Empty:
                    time.sleep(1)
                    continue
                logging.debug('Received message:')
                logging.debug(message.payload)
                s = send.send(json.dumps(message.payload))
                s += send.send('\n')
                logging.debug('sent {} bytes'.format(s))
                message.ack()
        except socket.error as e:
            logging.debug('recieved socket error, {}'.format(e))
            pass
        finally:
            logging.debug('closing connection')
            send.close()
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='read messages from an amqp broker and send them to a port')
    parser.add_argument('--port', help='the port to send on (default: 1984)',
                        type=int,
                        default=1984)
    parser.add_argument('--url', help='the amqp broker url',
                        required=True)
    parser.add_argument('--queue', help='the amqp queue name to subscribe '
                        '(default: sparkhara)',
                        default='sparkhara')
    args = parser.parse_args()
    main(args.url, args.port, args.queue)
