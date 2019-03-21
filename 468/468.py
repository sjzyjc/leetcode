class Solution:
    def validIPAddress(self, IP: str) -> str:
        if not IP:
            return "Neither"
        
        
        if self.isIPv4(IP):
            return "IPv4"
        
        if self.isIPv6(IP):
            return "IPv6"
        
        return "Neither"
    
    
    def isIPv4(self, ip):
        tmp = ""
        count = 0
        for index, charr in enumerate(ip):
            #print(tmp)
            if not (charr.isdigit() or charr == '.'):
                return False
        
            if charr == '.':
                count += 1
                if not tmp or int(tmp) > 255:
                    return False
                
                tmp = ""
            else:
                if index > 0 and ip[index - 1] == "0":
                    return False
                
                tmp += charr
                
        return (tmp and 0 <= int(tmp) <= 255) and count == 3
    
    def isIPv6(self, ip):
        tmp = ""
        count = 0
        for index, charr in enumerate(ip):
            if not (charr.isdigit() or charr == ':' or(charr.isalpha() and 0 <= ord(charr.lower()) - ord('a') < 6)):
                return False
            
            if charr == ':':
                count += 1
                if not tmp or len(tmp) > 4:
                    return False
                
                tmp = ""
                
            else:
                tmp += charr
                
        return count == 7 and tmp and len(tmp) <= 4
                
        
                        
                