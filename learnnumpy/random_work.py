# coding:utf-8
"""
dec: 随机漫步
"""
import numpy as np
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
# 各步的累计和
walk = steps.cumsum()
walk_min = walk.min()
walk_max = walk.max()

# 第一次到达8的时间
walk_8 = (np.abs(walk) >= 8).argmax()
print(walk_8)
print(walk1)


