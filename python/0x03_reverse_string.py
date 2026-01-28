def reverse_list(items):
  """Reverse a list.

  Args:
    items: A list.
  
  Returns:
    A reversed list of items.
  """
  reversed_list = list()
  for i in range(1, len(items)+1):
    reversed_list.append(items[-i])
  return reversed_list
