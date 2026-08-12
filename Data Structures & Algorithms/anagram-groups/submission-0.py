class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_to_strs = {}
        for string in strs:
            anagram_key = ''.join(sorted(string))
            anagram_to_strs.setdefault(anagram_key, []).append(string)
        
        return [grouped_strings for grouped_strings in anagram_to_strs.values()]
