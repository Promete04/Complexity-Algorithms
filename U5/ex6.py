

M=[ 
    ["_","a","b","c","d"],
    ["a","b","b","a","d"],
    ["b","c","a","d","a"],
    ["c","b","a","c","c"],
    ["d","d","c","d","b"]
  ]

def backtrack_substitution(text, M):
    # Base case: if the text is reduced to a single character
    if len(text) == 1:
        return True, text
    
    def valid_character(c):
        # Check if the character is valid (a, b, c, d)
        return c in ["a", "b", "c", "d"]
    

