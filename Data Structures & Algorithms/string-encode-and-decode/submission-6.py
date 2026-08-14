class Solution:
    def encode(self, strs: List[str]) -> str:
        output = ""

        for string in strs:
            length = len(string)
            output += str(length) + '#' + string
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        pointer = 0

        while pointer < len(s):
            hash_index = s.find('#', pointer)
            length = int(s[pointer:hash_index])
            start = hash_index + 1
            end = start + length
            output.append(s[start:end])
            pointer = end
        return output