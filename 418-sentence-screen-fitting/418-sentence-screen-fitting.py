class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # sentence = ["hello", "world"], rows=2, cols=8
        # hello---
        # world---
        # hello---
        # ... => 1
        # sentence = ["a", "bcd", "e"], rows=3, cols=6
        # a-bcd-
        # e-a---
        # bcd-e-
        # a-bcd- .... => 2
        
        # sentence = ["apple", "asdf"], rows=2, cols=10
        # apple-asdf-apple-asdf-apple-adsf-....
        #       *               
        # current_char_idx // sum of length of each words + spaces between them
        
        s = ''
        for word in sentence:
            s += word + ' '
        
        curr_char_idx = 0
        for row in range(rows):
            curr_char_idx += cols
            if s[curr_char_idx % len(s)] == ' ':
                curr_char_idx += 1
            else:
                while s[(curr_char_idx-1) % len(s)] != ' ':
                    curr_char_idx -= 1
        
        return curr_char_idx // len(s)
                
        
            
            
        