def peakElement(arr, n):
    if n==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    for i in range(1,n-1):
        if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
            return i

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = peakElement(arr, n)
        flag = False
        if index == 0 and n==1:
            flag = True
        elif index==0 and arr[index]>arr[index+1]:
            flag = True
        elif index==n-1 and arr[index]>arr[index-1]:
            flag = True
        elif arr[index-1] < arr[index] and arr[index] > arr[index+1]:
            flag = True
        else:
            flag = False
        if flag:
            print(1)
        else:
            print(0)            
