
"""which is used in the following way: in any string, two consecutive characters can be
replaced by the value that appears in the table, using the first character as row and the
second character as column. For example, you can change the sequence ca to a b, since
M[c, a]=b.
Implement a Backtracking algorithm that, starting from a string of text and using the
information stored in a substitution table M, is able to find a way to make the substitutions
that allow reducing the text string to a final character, if possible.
Example: With the string text = acabada and the final character = d, a possible form of
substitution is the following (the sequences that are replaced are marked for clarity):
acabada  acacda  abcda  abcd  bcd  bc  d."""
M=[ 
    ["_","a","b","c","d"],
    ["a","b","b","a","d"],
    ["b","c","a","d","a"],
    ["c","b","a","c","c"],
    ["d","d","c","d","b"]
  ]

def backtrack_substitution(text,characterToFind, M):
    # Base case: if the text is reduced to a single character
    if len(text) == 1 and text[0] == characterToFind:
        return True
    
    # Recursive function to perform backtracking
    def backtrack(text):
        # If the text is reduced to a single character
        if len(text) == 1 and text[0] == characterToFind:
            return True
        
        # Iterate through the text to find pairs of characters to substitute
        for i in range(len(text)-1):
            char1 = text[i]
            char2 = text[i+1]

            # Find the indices of the characters in the substitution table
            index1 = M[0].index(char1)
            index2 = M[0].index(char2)
            # Get the substitution character from the table
            substitution_char = M[index1][index2]
            # Create a new text with the substitution
            new_text = text[:i] + substitution_char + text[i+2:]

            # Recursively call backtrack with the new text
            if backtrack(new_text):
                return True
            
        # If no valid substitution is found, return False   
        return False
    # Start backtracking from the original text
    result = backtrack(text)
    return result

# Example usage
text = "abbababa"
characterToFind = "d"
result= backtrack_substitution(text, characterToFind, M)
if result:
    print(f"Yes, it is possible to reduce '{text}' to '{characterToFind}'")
else:
    print(f"No, it is not possible to reduce '{text}' to '{characterToFind}'")
        
    

