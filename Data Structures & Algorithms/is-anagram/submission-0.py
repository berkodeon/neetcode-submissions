class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map = {}
        for character in s:
            new_count = count_map.setdefault(character, 0) + 1
            count_map[character] = new_count
        
        count_map2 = {}
        for character in t:
            new_count2 = count_map2.setdefault(character, 0) + 1
            count_map2[character] = new_count2
        
        return count_map == count_map2
