class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for directory in path:
            if directory == ".." and stack:
                stack.pop()
            elif directory not in {"", ".", ".."}:
                stack.append(directory)

        return "/" + "/".join(stack)

        
