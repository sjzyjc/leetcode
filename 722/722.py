class Solution(object):
    def removeComments(self, source):
        in_block = False
        ans = []
        for line in source:
            if not in_block:
                newline = []
                
            i = 0
            while i < len(line):
                if line[i:i+2] == '/*' and not in_block:
                    in_block = True
                    i += 2
                    continue
                elif line[i:i+2] == '*/' and in_block:
                    in_block = False
                    i += 2
                    continue
                elif line[i:i+2] == '//' and not in_block:
                    break
                elif not in_block:
                    newline.append(line[i])
                
                i += 1
                
            if newline and not in_block:
                ans.append("".join(newline))
                
            print(ans, newline, in_block)

        return ans