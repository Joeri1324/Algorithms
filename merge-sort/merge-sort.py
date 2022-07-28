def combine(input1, input2):
  if input1[0] < input2[0]:
    return input1 + input2
  else:
    return input2 + input1

def merge(input1, input2, output = []):
  if len(input1) == 0:
    return combine(input2, output)

  if (len(input2)) == 0:
    return combine(input1, output)

  if input1[0] < input2[0]:
    return merge(input1[1:], input2, output + [input1[0]])
  else:
    return merge(input1, input2[1:], output + [input2[0]])

def merge_sort(input):
  if len(input) == 1:
    return input

  mid_point = int(round(len(input) / 2))
  sub_array_1 = input[0:mid_point]
  sub_array_2 = input[mid_point:]
  sorted_sub_array_1 = merge_sort(sub_array_1)
  sorted_sub_array_2 = merge_sort(sub_array_2)

  return merge(sorted_sub_array_1, sorted_sub_array_2)


sorted = merge_sort([3, 4, 5, 1, 2, 7])
print(sorted)
