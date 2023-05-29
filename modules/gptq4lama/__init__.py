import logging
from .module import GptqForLlama

def register_model(factory):
    logging.info("GptqForLlama model registered")
    factory.register_model('GptqForLlama', GptqForLlama)