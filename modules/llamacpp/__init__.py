import logging
from .module import LlamaCpp

def register_model(factory):
    logging.info("LlamaCpp model registered")
    factory.register_model('LlamaCpp', LlamaCpp)