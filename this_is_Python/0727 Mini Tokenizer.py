import string
from collections import Counter
import re

#Mini Tokenizer
stopwords = {'in', 'she', 'the', 'is', 'and', 'to', 'of', 'for', 'on', 'a'}
text = "Sunny started learning Python in 2024. She enjoys solving real-world problems!"
text = text.lower()
cleaned = [word.strip(string.punctuation) for word in text.split()]
filtered = [word for word in cleaned if word not in stopwords]
count = Counter(filtered)
print(count)

#Keyword Highlighter

text = "She is learning python and building projects with AI."
keywords = ['python', 'ai']

# def highlight_keywords(text, keywords):
#     for kw in keywords:
#         text = text.replace(kw, f'**{kw}**')
#         return text
# highlighted = highlight_keywords(text, keywords)
# print(highlighted)

# def highlight_keywords(text, keywords):
#     def replacer(match):
#         return f"**{match.group(0)}**"
#
#     unique_keywords = set(kw.lower() for kw in keywords)
#     for kw in unique_keywords:
#         pattern = re.compile(rf'\b{re.escape(kw)}\b', re.IGNORECASE)
#         text = pattern.sub(replacer, text)
#     return text
#
# highlighted = highlight_keywords(text, keywords)
# print(highlighted)

def highlight_keywords_custom(text, keywords, mode='markdown'):
    def get_wrapper(word):
        if mode == 'html':
            return f'<mark>{word}</mark>'
        else:
            return f'**{word}**'

    unique_keywords = set(kw.lower() for kw in keywords)
    for kw in unique_keywords:
        pattern = re.compile(rf'\b{re.escape(kw)}\b', re.IGNORECASE)
        text = pattern.sub(lambda m: get_wrapper(m.group(0)), text)
    return text

highlighted = highlight_keywords_custom(text, keywords, mode='html')
print(highlighted)

def highlight_keywords_custom(text, keywords, mode='html'):
    def get_wrapper(word):
        if mode == 'html':
            return f'<mark>{word}</mark>'
        else:
            return f'**{word}**'

    unique_keywords = set(kw.lower() for kw in keywords)
    for kw in unique_keywords:
        pattern = re.compile(rf'\b{re.escape(kw)}\b', re.IGNORECASE)
        text = pattern.sub(lambda m: get_wrapper(m.group(0)), text)
    return text

# 测试
text = "Sunny enjoys solving AI problems with Python. She uses python daily."
keywords = ["python", "solving"]

highlighted = highlight_keywords_custom(text, keywords, mode='html')
print(highlighted)


def highlight_keywords_custom(text, keywords):
    def get_wrapper(word):
        return f'<mark>{word}</mark>'  # 或者换成 span 自定义颜色

    for kw in set(keywords):
        pattern = re.compile(rf'\b{re.escape(kw)}\b', re.IGNORECASE)
        text = pattern.sub(lambda m: get_wrapper(m.group(0)), text)
    return text

text = "Sunny enjoys solving AI problems with Python. She uses Python daily."
keywords = ['python', 'solving']

highlighted = highlight_keywords_custom(text, keywords)

# 把高亮后的内容保存成 HTML 文件
with open("highlighted.html", "w", encoding="utf-8") as f:
    f.write(f"<html><body><p>{highlighted}</p ></body></html>")

print("✅ 已保存为 highlighted.html，用浏览器打开查看高亮效果。")