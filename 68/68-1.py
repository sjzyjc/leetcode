class Solution:
    def fullJustify(self, words, maxWidth):
        if not words or maxWidth <= 0:
            return []
        
        i = 0
        ans = []
        while i < len(words):
            line, cur_len = [words[i]], len(words[i])
            j = i + 1
            while j < len(words) and cur_len + 1 + len(words[j]) <= maxWidth:
                line.append(words[j])
                cur_len += (len(words[j]) + 1)
                j += 1
                
            i = j
            if i == len(words):
                line_str = " ".join(line)
                ans.append(line_str + " " * (maxWidth - len(line_str)))
                break
            else:
                ave_space = (maxWidth - cur_len) // (len(line) - 1) if len(line) != 1 else maxWidth - cur_len
                extra = (maxWidth - cur_len) - ave_space * (len(line) - 1)
                tmp = ''
                for index, word in enumerate(line):
                    tmp += word
                    
                    if index + 1 <= extra:
                        tmp += ' ' * (ave_space + 2)
                    else:
                        tmp += ' ' * (ave_space + 1)
                        
                ans.append(tmp[:maxWidth])   
              
        return ans
