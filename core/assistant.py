class Assistant:
    """
    Handles the interaction between the user and Jarvis.

    Responsibilities:
    - Read user input
    - Display streamed responses
    - Save conversation history
    """

    def __init__(self, brain, conversation_manager):
        self.brain = brain
        self.conversation_manager = conversation_manager

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

            # Save the user's message
            self.conversation_manager.add_user_message(user_input)

            # Ask the Brain for a streamed response
            response_stream = self.brain.think(user_input)

            print("\nJarvis: ", end="", flush=True)

            # Collect the streamed response while printing it
            response_chunks = []

            for chunk in response_stream:
                print(chunk, end="", flush=True)
                response_chunks.append(chunk)

            print("\n")

            # Combine all chunks into one complete response
            full_response = "".join(response_chunks)

            # Save the assistant's response
            self.conversation_manager.add_assistant_message(full_response)