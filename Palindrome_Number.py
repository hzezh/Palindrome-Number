
def isPalindrome(self, input_number: int) -> bool:
  input_str = str(input_number)
  reversed_str = ''
  str_length = len(input_str)-1

  if (input_str[0] != input_str[str_length]):
    return False

  for index in range(str_length, -1,-1):
    reversed_str = reversed_str + input_str[index]
  return input_str == reversed_str
