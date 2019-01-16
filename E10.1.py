t = [[1,2], [3], [4, 5, 6]]
def nested_sum(list_int):
  list_of_int = []
  total = 0
  for i in list_int:
    list_of_int.extend(i)
  for int in list_of_int:
    total = total + int
  print(total)
nested_sum(t)