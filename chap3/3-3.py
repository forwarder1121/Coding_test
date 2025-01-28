n,m=map(int,input().split())
candidates=[]
for _ in range(n):
    row=list(map(int,input().split()))
    result=min(row)
    candidates.append(result) 
print(max(candidates))

# 2 4 
# 7 3 1 8
# 3 3 3 4
