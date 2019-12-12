class ClimbStairs(object):
    
    def climb_stairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        one_step = 1
        two_step = 2
        steps = 0
        for i in range(3, n + 1):
            steps = one_step + two_step
            one_step = two_step
            two_step = steps
        return steps

if __name__ == "__main__":
    climbStairs = ClimbStairs()
    result = climbStairs.climb_stairs(5)
    print(result)