n,m,k=map(int,input().split())

data=list(map(int,input().split()))

data.sort()

first=data[n-1]
second=data[n-2]

block_size=k+1
block_weight=first*k+second

num_of_block=int(m/block_size)
remainder=m%block_size

result=num_of_block*block_weight
result+=remainder*first

print(result)