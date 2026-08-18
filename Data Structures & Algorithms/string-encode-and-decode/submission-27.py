class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "Latina"
        return "#GADIEL".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "Latina":
            return []
        return s.split("#GADIEL")
        
