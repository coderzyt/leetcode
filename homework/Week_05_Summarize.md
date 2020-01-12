1. 最优子结构： opt[n] = best_of(opt[n-1] + opt[n-2] + ...)
2. 储存中间结构 opt[i]
3. 递推公式 状态转移方程 DP(Dynamic Programing)
Fib: opt[i] = opt[i-1] + opt[i-2]
二维路径: opt[i,j] = opt[i+1,j] + opt[i,j+1]且判断opt[i,j]是否为空地
