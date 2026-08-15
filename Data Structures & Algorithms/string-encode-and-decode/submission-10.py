class Solution:
    def encode(self, strs: List[str]) -> str:
        output = ""

        for string in strs:
            output += string + '~'
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        pointer = 0

        while pointer < len(s):
            hash_index = s.find('~', pointer)
            output.append(s[pointer:hash_index])
            pointer = hash_index + 1
        return output