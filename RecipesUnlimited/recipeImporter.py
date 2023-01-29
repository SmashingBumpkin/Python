# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:59:51 2023

@author: Charl
"""

import cv2
import pytesseract
import openai
import sys
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def sendPrompt(myprompt, temperature = 0.01):
    cont = input("\n____\n\n\nPlease type 1 to continue (will spend openai credits) ")
    if cont != "1":
        print("\nYou have terminated the program, cheapskate.\n")
        sys.exit()
    openai.api_key = "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"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=myprompt,
      max_tokens=600,
      temperature=temperature
    )
    return response["choices"][0]["text"]

myimg = cv2.imread('PXL_20230122_160513413.jpg')
text = pytesseract.image_to_string(myimg)
print(text)

myprompt = ("The following excerpt is a jumbled up recipe. Reformat this recipe "+
            "to be the name, the description, the ingredients and then the method."
            + "\n\n" + text)

recipe = sendPrompt(myprompt)

