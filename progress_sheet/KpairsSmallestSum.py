class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        k_pairs = []
        candidates = [(nums1[0] + nums2[0], 0, 0)]
        visited = set([(nums1[0] + nums2[0], 0, 0)])

        while k > 0 and candidates:

            sum_, idx1, idx2 = heappop(candidates)
            k_pairs.append((nums1[idx1], nums2[idx2]))

            if idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in visited:
                heappush(candidates, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
                visited.add((idx1 + 1, idx2))
            
            if idx2 + 1 < len(nums2) and (idx1, idx2 + 1) not in visited:
                heappush(candidates, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
                visited.add((idx1, idx2 + 1))

            k -= 1
        
        return k_pairs
