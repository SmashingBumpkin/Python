import openai
from sys import exit as sysexit

def sendPrompt(myprompt, temperature = 0.01, model = "text-davinci-003"):
    cont = input("\n____\n\n\nPlease type 1 to continue (will spend openai credits) ")
    if cont != "1":
        print("\nYou have terminated the program, cheapskate.\n")
        sysexit()
    openai.api_key = "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"
    response = openai.Completion.create(
      model=model,
      prompt=myprompt,
      max_tokens=600,
      temperature=temperature
    )
    return response["choices"][0]["text"]