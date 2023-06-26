import openai_link

questionsSoFar = []
failedTests = True

while failedTests:
    prompt = input("Enter a value: ")
    if prompt == "exit":
        break
    response = openai_link.sendPromptFrank(questionsSoFar, prompt)
    questionsSoFar.extend([{"role": "user", "content": prompt},
                            {"role": "assistant", "content": response}])
    print(response)
    if openai_link.wasQuestionSuccessful("Did A find out that B heard the time from the TV?", prompt, response):
        failedTests = False

