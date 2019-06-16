# coding:utf-8
"""
desc: 基础学习
"""
import numpy as np

# 数组创建
# a = np.array([1, 2, 3])
# print(a)
# print(a.shape)
# print(a.dtype)
# print(a.itemsize)
# print(a.size)
# print(a.data)

# b = np.zeros(10)
# c = np.ones((1, 2))
# print(b)
# print(c)

# 数组计算
# i = np.array([[1, 2], [3, 4]])
# j = np.array([[5, 6], [7, 8]])
# print(i + j)
# print(i - j)
# print(i - 1)
# print(i * j)
# print( i / j)
# print(j.dot(i))

# 索引和切片
# arr = np.arange(10)
# print(arr)
# print(arr[0])
# print(arr[1:6])
# arr_slice = arr[1:6]
# arr_slice[1:3] = 5
# print(arr_slice)
# print(arr)
# arr_copy = arr[1:6].copy()
# arr_copy[1:3] = 6
# print(arr_copy)
# print(arr)

# arr_2d = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
# print(arr_2d[0])
# print(arr_2d[0, 1])
# arr_2d_slice = arr_2d[1]
# print(arr_2d_slice)
# arr_2d_slice[0] = 1
# print(arr_2d_slice)
# print(arr_2d)

# 切片索引
# arr_test = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
# print(arr_test[:2])
# print(arr_test[:2, 1:])
# print(arr_test[1, :1])
# arr_slice_test = arr_test[:2, 1:]
# arr_slice_test[0] = 0
# print( arr_slice_test)
# print(arr_test)

# 布尔索引
# x = np.array([[0, 1], [2, 3], [3, 4]])
# print(x)
# print(x > 1)

# 花式索引
# array = np.empty((4, 3))
# for i in range(4):
#     array[i] = i
# print(array)
# print(array[np.ix_([3, 0],[2, 1])])

# 形状转换
# arr = np.arange(12)
# print(arr)
# arr1 = arr.reshape(3, 4)
#
# for item in arr1:
#     print(item)
# for item in arr1.flat:
#     print(item)
#
# print(arr1.flatten())
# print(arr1.flatten(order="K"))
# arr.flatten()[10] = 0
# print(arr)
#
# print(arr.ravel())
# arr.ravel()[10] = 0
# print(arr)

# 转置与轴对换
# arr = np.arange(12).reshape((2, 2, 3))
# print(arr)
# print(arr.T)
# print(arr.transpose((1, 0, 2)))
# print(arr.swapaxes(1, 2))


# 一元func
# arr = np.arange(10)
# print(np.sqrt(arr))
# print(np.square(arr))

# 二元func
# arr1 = np.arange(10)
# arr2 = np.arange(10)
# print(np.add(arr1, arr2))


