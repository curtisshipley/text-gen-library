import logging
from .module import KoboldCpp

def register_model(factory):
    logging.info("KoboldCpp model registered")
    factory.register_model('KoboldCpp', KoboldCpp)