

class ModelFactory:
    def __init__(self):
        self.models = {}

    def register_model(self, type, class_reference):
        self.models[type] = class_reference

    def create_model(self, type):
        if type not in self.models:
            raise ValueError("Invalid type")
        return self.models[type]()