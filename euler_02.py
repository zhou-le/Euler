#coding: utf-8
#date: 2018/7/30  19:47
#author: zhou_le
l = []
def fibo(fst, sec):
    sum_fibo = fst + sec
    if sum_fibo % 2 == 0:
        l.append(sum_fibo)
    if sum_fibo > 4000000:
        return sum(l)
    return fibo(sec, sum_fibo)
print(fibo(0,1))