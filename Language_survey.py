from survey import AnonymousSurvey

# Identifying the issue with creating an instance of AnonymousSurvey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Output a question and save answers.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Displays the results of surveys.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
