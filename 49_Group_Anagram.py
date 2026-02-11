class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}
        
        for s in strs:
            sorted_chars = sorted(s)
            key = "".join(sorted_chars)
            
            if key not in anagram_map:
                anagram_map[key] = []
            
            anagram_map[key].append(s)
       
        return list(anagram_map.values())