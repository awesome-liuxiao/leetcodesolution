class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split("/")
        print(dirs)
        simPath = ""
        for dir in dirs:
            if not dir or dir == '.':
                continue
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        print(stack)
        simPath = '/'+'/'.join(stack)
        print(simPath)

x = Solution()

path = "/home/"
x.simplifyPath(path)

path = "/../"
x.simplifyPath(path)

path = "/home//foo/"
x.simplifyPath(path)

path = "/a/./b/../../c/"
x.simplifyPath(path)

path = "/a/../../b/../c//.//"
x.simplifyPath(path)

path = "/a//b////c/d//././/.."
x.simplifyPath(path)