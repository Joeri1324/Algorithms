def selection_sort(input):
  for idx1 in range(len(input) - 1):
    smallest_idx = idx1
    for idx2 in range(idx1, len(input)):
      if input[idx2] < input[smallest_idx]:
        smallest_idx = idx2
    
    temp = input[idx1]
    input[idx1] = input[smallest_idx]
    input[smallest_idx] = temp

  return input

sorted = selection_sort([3, 4, 5, 1, 100, 2, 7])
print(sorted)
