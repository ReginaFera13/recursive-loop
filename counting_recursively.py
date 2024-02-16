def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n-1)

count_down(5)
 
def count_up(n, start=0):
    if start == n:
        return start
    print(start)
    count_up(n, start+1)


count_up(5)
