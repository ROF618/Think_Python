def cuml_sum(list_of_numbers):
  total = 0
  new_list = []
  for int in list_of_numbers:
    total= int + total
    new_list.append(total)
  return print(new_list)

cuml_sum([1, 2, 3])