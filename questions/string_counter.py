from collections import defaultdict
from collections import Counter
from typing import Tuple
import operator

def count_chars1(text: str):
  counter = defaultdict(int)

  for char in list(text):
    if char == ' ': continue
    counter[char] += 1
  # counterの最大値のkey, 最大値のvalueを返す
  return [max(counter, key=counter.get), max(counter.values())]

# 別の実装
def count_chars2(text: str) -> Tuple[str, int]:
  counter = []

  for char in text:
    if not char.isspace():
      # counter[('t', 1)] というインデックス
      counter.append((char, text.count(char)))
  # itemgetter(0)を指定すると、counterのkeyを取得し
  # itemgetter(1)を指定すると、counterのvalueを取得
  return max(counter, key=operator.itemgetter(1))

# 別の実装 リスト内フォーカスで処理
def count_chars3(text: str):
  counter = [(c, text.count(c)) for c in text if not c.isspace()]
  return max(counter, key=operator.itemgetter(1))

# 別の実装 
def count_chars4(text: str):
  counter = {}

  for char in text:
    if not char.isspace():
      # counter[char]の有無を確認し、なければ0で初期化して+1
      counter[char] = counter.get(char, 0) + 1
  max_key = max(counter, key=counter.get)
  return max_key, counter[max_key]

# 別の実装 
def count_chars5(text: str):
  counter = Counter()

  for char in text:
    if not char.isspace():
      counter[char] += 1
  max_key = max(counter, key=counter.get)
  return max_key, counter[max_key]


text = 'This is a pen. This is an apple. Applepen.'
result = count_chars1(text)
print(result)

result = count_chars2(text)
print(result)