
class IModules:
    def setup(self, modelargs) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, prompt, text) -> dict:
        """Extract text from the currently loaded file."""
        pass
