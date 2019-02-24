class Solution:

    # 방법 1
    def singleNumber(self, nums: 'List[int]') -> 'int':
        """
        1.다음과 같은 사전 d => {num : count} 를 만든다.
        2.1번에서 만든 사전 d에서 count == 1인 num을 반환한다.
        """
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for num in d:
            if d[num] == 1:
                return num

    ## 방법 2
    def singleNumber(self, nums: 'List[int]') -> 'int':
        v = nums[0]
        for num in nums[1:]:
            v = v ^ num

        for num in nums:
            if v ^ num == 0:
                return num