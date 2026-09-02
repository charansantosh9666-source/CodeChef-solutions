def calculate_power(base, exponent):
    ans=1
    #write your code here
    while exponent>0:
        ans=ans*base
        exponent=exponent-1
    return ans
    
    
def main():
    base, exponent = map(int, input().split())
    result = calculate_power(base, exponent)
    print(result)


main()
