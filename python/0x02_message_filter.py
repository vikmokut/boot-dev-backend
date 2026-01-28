def filter_messages(messages):
  """Filter a string of words for targeted word

  Args:
    messages: A list of strings

  Return:
    A list of filtered messages
    The number of swear words caught in each message
  """
  new_messages = list()
  list_of_swears = list()
  count_of_swears = 0
  j = 0
  for message in messages:
    current_msg = message.split()
    for word in current_msg:
      if word == "dang":
        count_of_swears += 1
        current_msg.pop(j)
        j += 1 # solves problem of skip after pop() operation
        # to resolve: repeated swear word bug (e.g. "dang dang this")
        continue
      j += 1
    list_of_swears.append(count_of_swears)
    new_messages.append(" ".join(current_msg))
    j = 0
    count_of_swears = 0
  return new_messages, list_of_swears
