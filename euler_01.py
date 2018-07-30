#coding: utf-8
#date: 2018/7/30  19:07
#author: zhou_le

# 求1000以下3和5的倍数之和

print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))