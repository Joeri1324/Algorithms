def binary_search(sorted_list, key):
  if len(sorted_list) == 1:
    return sorted_list[0] == key

  mid_point = int(round(len(sorted_list) / 2))

  if key < sorted_list[mid_point]:
    return binary_search(sorted_list[:mid_point], key)
  else:
    return binary_search(sorted_list[mid_point:], key)


print(binary_search([1,2, 5, 6], 7))
print(binary_search([1,2, 5, 6], 6))
