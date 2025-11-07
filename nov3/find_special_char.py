import re

def find_special_character(input_string):
  """
  Checks if a string contains any special characters.

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains any special characters, False otherwise.
  """
  # regex to find special characters
  regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

  if(regex.search(input_string) == None):
    return False
  else:
    return True

# Example usage
string1 = input("Enter a string: ")
string2 = "This string has a special character @"

if find_special_character(string1):
  print(f"'{string1}' contains special characters.")
else:
  print(f"'{string1}' does not contain special characters.")

# if find_special_character(string2):
#   print(f"'{string2}' contains special characters.")
# else:
#   print(f"'{string2}' does not contain special characters.")