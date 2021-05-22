from typing import List
from collections import Counter

def remove_min_count(x: List[int], y: List[int]) -> None:
    # Counterが使えない場合
    # count_x = {}
    # count_y = {}

    # for i in x:
    #   count_x[i] = count_x.get(i, 0) + 1
    # for i in y: 
    #   count_y[i] = count_y.get(i, 0) + 1
    
    counter_x = Counter(x)
    counter_y = Counter(y)

    for key_x, value_x in counter_x.items():
      value_y = counter_y.get(key_x)
      if value_y:
        if value_x < value_y:
          # xからiを取り出して、iとkey_xが一致しなければiを返す
          x[:] = [i for i in x if i != key_x]
        elif value_x > value_y:
          y[:] = [i for i in y if i != key_y]

# 2つの配列の重複する数のうち、出現回数が少ない方を削除する
arr_x = [1, 2, 3, 4, 4, 5, 5, 8, 10], 
arr_y = [5, 5, 5, 6, 7, 8, 8, 10]
result = remove_min_count(arr_x, arr_y)
print(result)