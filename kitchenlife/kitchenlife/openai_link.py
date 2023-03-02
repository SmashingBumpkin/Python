import openai
from sys import exit as sysexit

def sendPrompt(myprompt, active_user, temperature = 0.01, model = "text-davinci-003"):
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
    active_user.ai_credits_used += response["usage"]["total_tokens"]
    active_user.save()
    return response["choices"][0]["text"]

def sendPromptIngredients(myprompt, active_user):
    #https://platform.openai.com/docs/guides/chat
    cont = input("\n____\n\n\nPlease type 1 to continue (will spend openai credits) ")
    if cont != "1":
        print("\nYou have terminated the program, cheapskate.\n")
        sysexit()
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": """Modify this list to return each individual ingredient seperated by '\\n'
\n100g parmesan
300g mozzarella (2 balls)
800g chopped tomatoes (2 tins)
200g spinach
1 1/2 tsp ground cumin
Chopped red onion"""},
        {"role": "assistant", "content": """parmesan
mozzarella
chopped tomatoes
spinach
cumin
red onion"""},
        {"role": "user", "content": "Now repeat modify this list of ingredients, remove anything that isn't a basic ingredient and seperating by '\\n' "+myprompt}
    ]
    )
    active_user.ai_credits_used += response["usage"]["total_tokens"]
    active_user.save()
    print(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]