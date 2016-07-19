#!/usr/bin/env python
# coding: utf-8
""" A trivial messagebus implementing the pub/sub pattern based on zmq """
import logging
import zmq

__author__ = "jneines" 
__license__ = "MIT"
__copyright__ = "2016 "+__author__
__url__ = "https://github.com/jneines/TrivialMessageBus"

class TrivialMessageBus(object):
    """ A trivial implementation for a messagebus """
    def __init__(self, subscriber_port, publisher_port):
        """ Initialization """
        logging.debug("init")
        self.subscriber_port=subscriber_port
        self.publisher_port=publisher_port

        self.context=zmq.Context()


    def run(self):
        """ run as a proxy in a main loop """
        logging.debug("run")
        try:
            logging.debug("Creating subsciber on port {0:d}.".format(self.subscriber_port))
            self.subscriber=self.context.socket(zmq.SUB)
            self.subscriber.bind("tcp://*:{0:d}".format(self.subscriber_port))
            self.subscriber.setsockopt(zmq.SUBSCRIBE, b"")

            logging.debug("Creating publisher on port {0:d}.".format(self.publisher_port))
            self.publisher=self.context.socket(zmq.PUB)
            self.publisher.bind("tcp://*:{0:d}".format(self.publisher_port))

            logging.info("Starting proxy service.")
            zmq.proxy(self.subscriber, self.publisher)
        except Exception as e:
            logging.debug("Error message: {0}.".format(e))
            logging.info("Shutting down the trivial message bus.")
        finally:
            self.cleanup()

    def cleanup(self):
        """ cleaning up """
        logging.debug("cleanup")
        logging.debug("Closing publisher")
        self.publisher.close()
        logging.debug("Closing subscriber")
        self.subscriber.close()
        logging.debug("Terminating context")
        self.context.term()



if __name__=="__main__":
    """ A short main block to allow direct usage. """
    import argparse

    parser = argparse.ArgumentParser(description="Trivial Messagebus")
    parser.add_argument("-l", "--loglevel",
                        help="set the log level",
                        choices=["notset", "debug", "info", "warning", "error", "critical"],
                        default="critical")
    parser.add_argument("-s", "--subscriber_port",
                        help="set the port for the subscriber", type=int,
                        default=12345)
    parser.add_argument("-p", "--publisher_port",
                        help="set the port for the publisher", type=int,
                        default=12346)

    config=parser.parse_args()

    log_nlevel=getattr(logging, config.loglevel.upper(), None)

    logging.basicConfig(format="%(asctime)s - %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S", level=log_nlevel)

    tmb=TrivialMessageBus(config.subscriber_port, config.publisher_port)
    tmb.run()
