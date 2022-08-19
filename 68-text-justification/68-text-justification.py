class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [[words[0]]]
        
        currline = len(words[0])
        for word in words[1:]:
            currline += 1 + len(word)
            if currline <= maxWidth:
                lines[-1].append(word)
            else:
                currline = len(word)
                lines.append([word])
        
        # lines = [["This", "is", "an"], ["example", "of", "text"], ["justifications."]]
        
        answer = []
        for line in lines[:-1]:
            remaining = maxWidth - sum([len(w) for w in line])
            num_divisions = len(line) - 1 
            spaces = [0] * num_divisions

            linestr = line[0]

            if num_divisions > 0:
                for i in range(remaining):
                    spaces[i % num_divisions] += 1
                
                for i in range(num_divisions):
                    linestr += ' ' * spaces[i] + line[i+1]
            else:
                linestr += ' ' * (maxWidth - len(linestr))
            
            answer.append(linestr)
        
        lastline = lines[-1][0]
        for w in lines[-1][1:]:
            lastline += ' ' + w
        lastline += ' ' * (maxWidth - len(lastline))
        answer.append(lastline)
        
        return answer
