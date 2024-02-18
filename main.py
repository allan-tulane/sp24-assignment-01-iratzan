"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  ### TODo
  if x <= 1:
    return x
  else:
    return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
  ### TODO
  startval = -1
  stopval = -1
  longest_run = [0]

  for i in range(len(mylist)):
    if mylist[i] == key and startval == -1:
      startval = i

    if mylist[i] != key and mylist[i-1] == key:
      stopval = i
      longest_run.append(stopval - startval)
      startval = -1
      stopval = -1

    if mylist[i] == key and len(mylist)-1 == i:
      stopval = i + 1
      longest_run.append(stopval - startval)

  return max(longest_run)

class Result:
  """ done """
  def __init__(self, left_size, right_size, longest_size, is_entire_range):
    self.left_size = left_size               # run on left side of input
    self.right_size = right_size             # run on right side of input
    self.longest_size = longest_size         # longest run in input
    self.is_entire_range = is_entire_range   # True if the entire input matches the key

  def __repr__(self):
    return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
        (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

def to_value(v):
  if isinstance(v, Result):
    return v.longest_size
  else:
    return int(v)

def longest_run_recursive(mylist, key):
  def helper(lst, key):
      n = len(lst)
      if n == 0:
          return Result(0, 0, 0, False)
      if n == 1:
          if lst[0] == key:
              return Result(1, 1, 1, True)
          else:
              return Result(0, 0, 0, False)

      mid = n // 2
      left_result = helper(lst[:mid], key)
      right_result = helper(lst[mid:], key)


      is_entire_range = left_result.is_entire_range and right_result.is_entire_range and left_result.right_size + right_result.left_size == n


      middle_run = 0
      if lst[mid-1] == key and lst[mid] == key:
          middle_run = left_result.right_size + right_result.left_size

      longest_size = max(left_result.longest_size, right_result.longest_size, middle_run)


      left_size = left_result.left_size
      if left_result.is_entire_range:
          left_size += right_result.left_size

      right_size = right_result.right_size
      if right_result.is_entire_range:
          right_size += left_result.right_size

      return Result(left_size, right_size, longest_size, is_entire_range)


  return helper(mylist, key).longest_size