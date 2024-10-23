# custom hashing function which takes in a string as an input and outputs a unique set of numbers

def hash(string: str, length: int) -> int:

  assert(len(string) >= 7), 'The string you want to hash must be at least 7 digits long'
  
  hashed, sum = '', 0
  
  for char in string:

    sum += ord(char)
    hashed += str(ord(char)*1026029)
    
  return int(str(int(hashed[1:-1:2]) // sum)[:length])



print(hash('e422wtu', 20))