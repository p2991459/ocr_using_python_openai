import openai

# f = open("text.txt")
# text = f.read()
# openai.api_key = "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"
# completions = openai.Completion.create(
#     engine="text-davinci-003",
#     prompt=f"reformat the given text\n\n text: {text}",
#     max_tokens=3000,
#     temperature=0.2,
# )
#
# print(completions["choices"][0]["text"])
#
# reformatted_text = completions["choices"][0]["text"]
# f = open("reformatted.txt", "w")
# f.write(reformatted_text)


def textFormattor(raw_text):
    openai.api_key = "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"
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"reformat the given text\n\n text: {raw_text}",
        max_tokens=3000,
        temperature=0.2,
    )
    reformatted_text = completions["choices"][0]["text"]
    f = open("reformatted.txt", "w")
    f.write(reformatted_text)
    return  "formatted_text is saved in reformatted_text file"
