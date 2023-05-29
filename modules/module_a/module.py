import logging
from modules_management.imodule import IModule


class ModelA(IModule):
    def setup(self):
        # implement setup for ModelA
        logging.debug("setup called")
        pass

    def generate(self, prompt, text):
        # implement generate for ModelA
        logging.debug("generate called")
        return "generated string from ModelA"