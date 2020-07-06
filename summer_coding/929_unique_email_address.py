class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
            result = []
            
            for e in emails:
                tmp = e.split("@")
                local_name = tmp[0].split("+")[0] # Ignore everything after the first plus sign
                actual_name = local_name.replace(".", "")
                
                email = actual_name + "@" + tmp[1]
                result.append(email)
                
            return len(set(result))