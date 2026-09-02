# cook your dish here
def re(n):
    if(n==1):
        return 1
    return n * re(n-1)

a=int(input())
print(re(a))