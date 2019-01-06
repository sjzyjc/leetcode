class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        if emails is None:
            return 0
        
        ans = set()
        for email in emails:
            name, domain = email.split('@')
            new_name = ''
            for char in name:
                if char == '.':
                    continue
                
                if char == '+':
                    break
                
                new_name += char
                    
            ans.add(new_name + '@' + domain)
            
        return len(ans)
            