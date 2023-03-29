#!/usr/bin/env python3

import os
import sys
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
if openai.api_key is None:
    print("Please set the OPENAI_API_KEY environment variable.")
    sys.exit(1)

item = " ".join(sys.argv[1:])
content = "What is the HS Code for {item}".format(item=item)

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}])
for choice in completion.choices:
    print(choice.message.content)
