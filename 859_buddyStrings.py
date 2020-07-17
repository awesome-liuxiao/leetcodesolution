class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        A = list(A)
        B = list(B)
        
        # Edge cases 
        if not A or not B or len(A) == 1:
            return False
        
        if len(A) != len(B):
            return False
        
        # Find indices where the letters are different  
        diff = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff.append(i)
        
        # If the two words are same, and we need to make a swap,
        # we've to have at least a pair of same letter
        if len(diff) == 0:
            if len(A) > len(set(A)):
                return True
                
        # If difference is 2, then try a swap and compare
        elif len(diff) == 2:
        
            tmp = A[diff[0]]
            A[diff[0]] = A[diff[1]]
            A[diff[1]] = tmp

            if A == B:
                return True

        return False

        

X = Solution()

A = "ab"
B = "ba"
print(X.buddyStrings(A, B))

A = "ab"
B = "ab"
print(X.buddyStrings(A, B))

A = "aa"
B = "aa"
print(X.buddyStrings(A, B))

A = "aaaaaaabc"
B = "aaaaaaacb"
print(X.buddyStrings(A, B))


A = ""
B = "aa"
print(X.buddyStrings(A, B))
