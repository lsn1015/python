import re
import string

text = """
Python is widely used in machine learning, AI, data science, and web development.
Sunny studies Python every day to build powerful applications in the real world.
"""
text = text.lower()
words = [word.strip(string.punctuation) for word in text.split()]

keywords = input('please enter the keywords: ').lower()
highlighted = [word.upper() if word == keywords else word for word in words]
N = 10
for i in range(0,len(highlighted), N):
    print(' '.join(highlighted[i:i+N]))


text = "Hello! I'm Sunny. I love learning Python, AI. Do you?"
t = re.split(r'[.!?]', text)
cleaned = [s.strip() for s in t if s.strip()]
print(cleaned)