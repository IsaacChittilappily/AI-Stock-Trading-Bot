# custom hashing function which takes in a string as an input and outputs a unique set of numbers

def hash(string: str, length: int) -> int:

  # this hash shouldn't be used for short strings, so I've implemented length validation
  if len(string) <= 7:
    raise ValueError('The string you want to hash must be at least 7 digits long') 
  
  hashed, sum = '', 0
  
  # loop through the string
  for char in string:

    # sum up the ascii binary values
    sum += ord(char)

    # create a string of all the values multipled by a large prime
    hashed += str(ord(char)*1026029)
    
  # returns a scrambled version of the string divided by the sum of the ascii values
  return int(str(int(hashed[1:-1:2]) // sum)[:length])
