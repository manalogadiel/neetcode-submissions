class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "L8"
        return "#GADIEL".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "L8":
            return []
        return s.split("#GADIEL")
        
