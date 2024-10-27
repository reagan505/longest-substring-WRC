
def longest_substring_without_repeating(s):

  char_index = {} #keeps track of the most recent index of each character in the string.
  left = 0 #start of the current window.
  max_length = 0 #keeps track of the longest substring found without repeating characters.

  for right in range(len(s)): #iterates over the indices of the string [s]
    if s[right] in char_index and char_index[s[right]] >= left:
      left = char_index[s[right]] + 1

    char_index[s[right]] = right

    max_length = max(max_length, right - left + 1)

  return max_length

#example used
s = "mbinoherihioh"
print (longest_substring_without_repeating(s))