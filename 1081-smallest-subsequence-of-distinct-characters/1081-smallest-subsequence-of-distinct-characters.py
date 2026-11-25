class Solution:
    def smallestSubsequence(self, s: str) -> str:
        arr = []
        freq = Counter(s)
        for ch in s:
            freq[ch] -= 1
            if ch in arr:
                continue
            while arr and arr[-1] > ch and freq[arr[-1]]:
                arr.pop()
            arr.append(ch)
        return "".join(arr)