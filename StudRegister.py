import re
text = "Python is an interpreted high-level general-purpose programming language."
fiveWord = re.findall(r"\b\w{5}\b", text)
print("Following are the words with five Letters:")
for strWord in fiveWord:
  print(strWord)
