from typing import List
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        domainCntDict = {}
        for li in cpdomains:
            tmpStr = "".join(li)
            cnt, domain = tmpStr.split()
            subDomains = domain.split(".")
            subLen = len(subDomains)
            for i in range(subLen):
                tmpDomain = ""
                for j in range(i,subLen):
                    tmpDomain += subDomains[j]+"."
                tmpDomain = tmpDomain[:len(tmpDomain)-1]

                if tmpDomain in domainCntDict:
                    domainCntDict[tmpDomain] += int(cnt)
                else:
                    domainCntDict[tmpDomain]=int(cnt)

        for element in domainCntDict:
            res.append(str(domainCntDict[element])+" "+element)
        print(res)
        return res


x = Solution()

cpdomains = ["9001 discuss.leetcode.com"]
x.subdomainVisits(cpdomains)

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
x.subdomainVisits(cpdomains)