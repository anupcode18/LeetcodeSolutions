class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # akses tiap elemen di list
        # overwrite elemen tsb dengan elemen*element
        return sorted([x*x for x in nums])