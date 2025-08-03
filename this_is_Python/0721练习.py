import string
from collections import Counter
text = """
Sunny plans to apply for KAIST in 2026. She is working hard to improve her Python and AI skills.
She practices coding every day and loves solving real-world problems with algorithms.
"""
text = text.lower()
clean = [i.strip(string.punctuation) for i in text.split()]
count = Counter(clean)
n = []
for i in count.values():
    n.append(i)
m = sorted(n, reverse=True)
max_num = [w for w, c in count.items() if m[0] == c or m[1] == c or m[2] == c]
s = set(clean)
print(f'1: ')
print(f'cleaned word list, lowercase, no punctuations: ', clean)
print(f'the words frequency:', count.items())
print(f'top 3 frequency word:', max_num)
print(f'how many differ words in the text:', len(s))

tagged = []
for word in clean:
    if word.endswith('ing'):
        tag = 'VBG'
    elif word.endswith('ed'):
        tag = 'VBD'
    elif word == 'to':
        tag = 'TO'
    elif word in ('in', 'on', 'at'):
        tag = 'PREP'
    elif word.capitalize() in text:
        tag = 'NNP'
    else:
        tag = 'OTHER'
    tagged.append((word, tag))
print(f'2.POS Tagging')
print(tagged)

text = """
Sunny is preparing for her application to KAIST. She started learning Python in 2025 and has been improving steadily.
She enjoys solving problems and building projects that involve AI.
"""

# 要求：
# - 清洗文本（去除标点，转为小写）
# - 找出所有以 ing 或 ed 结尾的单词，输出为一个列表
text = text.lower()
clean = [word.strip(string.punctuation) for word in text.split()]
tag1 = []
for i in clean:
    if i.endswith('ing'):
        tag1.append(i)
    elif i.endswith('ed'):
        tag1.append(i)
    else:
        pass
print(f'NO.2 Part:', tag1)
# 目标：找出所有出现次数大于1的词，并从中排除 "a", "to", "the", "in", "for", "is", "and" 这些常见词

# 输出：一个关键词列表（无重复，按出现频率从高到低排序）

# 提示：
# - 使用 Counter
# - 记得用集合或列表排除 stopwords
word_num = Counter(clean)
new_word = [w for w, c in word_num.items() if c > 1 and w not in ("a", "to", "the", "in", "for", "is", "and")]
print(f'appear more than one time without prep:', new_word)
n = []
for c in word_num.values():
    n.append(c)
print(sorted(n,reverse=True))
n_word = [w for w, c in word_num.items() for i in range(len(n)) if n[i] == c]
s_word = set(n_word)
d = list(s_word)
print(d)
###****
stopwords = {"a", "to", "the", "in", "for", "is", "and"}
word_count = Counter(clean)

filtered = {word: count for word, count in word_count.items() if count > 1 and word not in stopwords}

sorted_keywords = sorted(filtered.items(), key=lambda x: x[1], reverse=True)
print('2.出现频率大于1的关键词（排除停工词：')
for word, count in sorted_keywords:
    print(f'{word}:{count}')
# 输出：
# - 每个单词对应的长度（dict）
# - 所有单词的平均长度（保留两位小数）
for i in clean:
    print(dict(zip([i], [len(i)])))

words_length = {word: len(word)for word in clean}
n = 0
t = 0
for i in clean:
    n += len(i)
    t += 1
    res = n / t
print(f'{res:.2f}')
avg_len = sum(len(word) for word in clean) / len(clean)