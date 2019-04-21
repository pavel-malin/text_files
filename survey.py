class AnonymousSurvey():
    """Collect anonymous responses to polls"""

    def __init__(self, question):
        """Save the question and prepares to save the answers."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Displays the question."""
        print(self.question)

    def store_response(self, new_response):
        """Saves one answer to the question."""
        self.responses.append(new_response)

    def show_results(self):
        """Displays all repliws received."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)