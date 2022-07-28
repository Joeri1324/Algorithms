def insert(key_idx, input_list):
  key = input_list[key_idx]
  
  for idx in range(key_idx - 1, -1, -1):
    element = input_list[idx]

    if element > key:
      input_list[idx] = key
      input_list[idx + 1] = element
    else:
      break

  return input_list

def insertion_sort(input):
  for idx in range(1, len(input)):
    input = insert(idx, input)

  return input

print(insertion_sort([5, 2, 5, 7, 4, 6, 1, 3, 10]))
