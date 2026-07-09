class Assistant:
    """
    Handles the interaction between the user and Jarvis.
    """

    def __init__(
        self,
        brain,
        conversation_manager,
        memory_manager,
    ):
        self.brain = brain
        self.conversation_manager = conversation_manager
        self.memory_manager = memory_manager

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
                print("\nJarvis: Goodbye!\n")
                break

            self.conversation_manager.add_user_message(user_input)

            response_stream = self.brain.think(user_input)

            print("\nJarvis: ", end="", flush=True)

            response_chunks = []

            for chunk in response_stream:
                print(chunk, end="", flush=True)
                response_chunks.append(chunk)

            print("\n")

            full_response = "".join(response_chunks)

            self.conversation_manager.add_assistant_message(full_response)

            # Process long-term memory after responding
            self.memory_manager.process(user_input)