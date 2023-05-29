import logging
from .module import ModelA

def register_model(factory):
    logging.info("ModelA model registered")
    factory.register_model('ModelA', ModelA)