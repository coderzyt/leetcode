递归代码模板:
```python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 

    # process logic in current level 
    process(level, data...) 

    # drill down 
    self.recursion(level + 1, p1, ...) 

    # reverse the current level status if needed
```

分治代码模板:
```python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```

动态规划和分治或者递归没有本质的区别 (关键看有无最优子结构)
共性: 找到重复子问题
差异性: 最优子结构, 中途可以淘汰次优解

1. 最优子结构： opt[n] = best_of(opt[n-1] + opt[n-2] + ...)
2. 储存中间结构 opt[i]
3. 递推公式 状态转移方程 DP(Dynamic Programing)
Fib: opt[i] = opt[i-1] + opt[i-2]
二维路径: opt[i,j] = opt[i+1,j] + opt[i,j+1]且判断opt[i,j]是否为空地
