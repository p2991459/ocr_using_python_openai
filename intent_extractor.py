import re

with open('reformatted.txt') as f:
    text = f.read()
def get_intentRadiology(text):
    result = re.search(r'EXAM: (.+?)\n', text)
    intent = "Can't found intent for the given Report"
    if result:
        intent = result.group(1)
    return intent
print(get_intentRadiology(text))