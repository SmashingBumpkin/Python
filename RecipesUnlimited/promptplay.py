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

def sendEditPrompt(edit_input, instruction, temperature = 0.01, model = "text-davinci-edit-001"):
    cont = input("\n____\n\n\nPlease type 1 to continue (edit) (will spend openai credits) ")
    if cont != "1":
        print("\nYou have terminated the program, cheapskate.\n")
        sysexit()
    openai.api_key = "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"
    response = openai.Edit.create(
        model=model,
        input = edit_input,
        instruction = instruction,
        temperature=temperature
    )
    print(response)
    return response["choices"][0]["text"]

inny = """400g linguine or spaghetti pasta    
120g streaky bacon
1 onion
1 dried chilli
1can (450g) chopped tomatoes
3 tbsp olive oil
salt and pepper
dash of maggi or worcester sauce
1 tsp sugar
chopped parsley and parmesan to serve"""

instruct = "Seperate the given string into individual ingredients, without any quantities, seperated by \\n"
print(sendEditPrompt(inny, instruct))