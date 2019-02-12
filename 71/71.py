class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return "/"
        
        stack = []
        items = path.split('/')
        for item in items:
            if len(item) == 0:
                continue
                
            if item == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            
            elif item == ".":
                continue
            else:
                stack.append(item)
                
        ans = ""
        for path in stack:
            ans += "/"
            ans += path
            
        return ans if ans else "/"

