class PromptLoader:
    @staticmethod
    def load(path):
        with open(path, "r", encoding="utf-8") as file:
            return file.read()