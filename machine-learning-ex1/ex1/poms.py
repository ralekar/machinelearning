def climbStairs(n):
        steps = [1,2]
        if n == 1:
        	return 1
        if n == 2:
           return 2
           	
        result = [0 for i in range(0,n+1)]
        result[0] = 0
        result[1] = 1
        result[2] = 2
        for i in range(3,n+1):
            for step in steps:
                    result[i]+=result[i-step]
        return result[-1]   


print climbStairs(1)        