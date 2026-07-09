class Assistant:
    def __init__(self, brain):
        self.brain = brain

    def start(self):
        print("=================================")
        print("        Jarvis v0.1")
        print("=================================")
        print("Type 'exit' to quit.\n")

        while True:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "exit":
                print("Jarvis: Goodbye!")
                break

            response = self.brain.think(user_input)

            print(f"\nJarvis: {response}\n")