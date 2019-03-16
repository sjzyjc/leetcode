class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words or not maxWidth:
            return []
        
        left = 0
        right = 0
        ans = []
        while right < len(words):
            total_word_len = 0
            break_count = -1
            while right < len(words) and total_word_len + break_count + len(words[right]) + 1 <= maxWidth:
                total_word_len += len(words[right])
                break_count += 1
                right += 1
            
            if right == len(words): #last line
                line = words[left]
                for i in range(left + 1, right):
                    line += " " + words[i]
                    
                line += (maxWidth - len(line)) * " "
                ans.append(line)
                break
                
            #not last line
            remain = maxWidth - total_word_len - break_count
            line = words[left]

            #on avarage for each space's extra ' '
            space_len = remain // break_count if break_count != 0 else 0
            extras = remain - space_len * break_count
            
            for i in range(left + 1, right):
                if i - (left + 1) < extras:
                    line += " " + " " * (space_len + 1) + words[i]
                else:
                    line += " " + " " * space_len + words[i]
                    
            line += " " * (maxWidth - len(line))   
            ans.append(line)
                    
            #move to next line
            left = right
            
        return ans