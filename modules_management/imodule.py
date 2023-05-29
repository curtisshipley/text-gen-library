
class IModule:
    def setup(self, modelargs) -> str:
        """Load in the file for extracting text."""
        pass

    def generate(self, prompt, text) -> dict:
        """Extract text from the currently loaded file."""
        pass
