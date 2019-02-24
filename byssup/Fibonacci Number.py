class Solution:

    # 방법 1
    def fib(self, N):
        """
        1. l 이라는 피보나치 리스트를 만든다.
        2. 1번에서 만든 피보나치 리스트에서 N번째 값을 반환한다.
        """
        l = [0, 1]
        for i in range(N-1):
            l.append(l[-1] + l[-2])
        return l[N]

    # 방법 2
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        l = [-1 for _ in range(31)]
        l[0] = 0
        l[1] = 1
        for i in range(2, N + 1):
            l[i] = l[i - 2] + l[i - 1]
        return l[N]

