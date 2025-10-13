# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 16:19:25 2025

@author: 1
"""

import numpy as np
def solve_linear_system(coefficients, constants):
    """
    解多元一次方程组 Ax = b
    
    参数:
        coefficients: 系数矩阵A，形状为(n, n)
        constants: 常数项向量b，形状为(n,)
        
    返回:
        如果有唯一解，返回解向量x
        如果无解，返回None
        如果有无穷多解，返回字符串"无穷多解"
    """
    # 确保输入是numpy数组
    A = np.array(coefficients, dtype=np.float64)
    b = np.array(constants, dtype=np.float64)
    n = len(b)
    
    # 构建增广矩阵
    augmented = np.hstack((A, b.reshape(n, 1)))
    
    # 高斯消元过程
    for col in range(n):
        # 找到主元（当前列中绝对值最大的元素）
        pivot_row = np.argmax(np.abs(augmented[col:, col])) + col
        
        # 如果主元为0，矩阵奇异，方程组可能无解或无穷多解
        if np.isclose(augmented[pivot_row, col], 0):
            # 检查增广部分是否有非零元素
            for row in range(col, n):
                if not np.isclose(augmented[row, -1], 0):
                    return None  # 无解
            return "无穷多解"  # 无穷多解
        
        # 交换当前行和主元行
        augmented[[col, pivot_row]] = augmented[[pivot_row, col]]
        
        # 归一化主元行
        pivot = augmented[col, col]
        augmented[col] /= pivot
        
        # 消去其他行的当前列
        for row in range(n):
            if row != col and not np.isclose(augmented[row, col], 0):
                factor = augmented[row, col]
                augmented[row] -= factor * augmented[col]
    
    # 提取解
    solution = augmented[:, -1]
    return solution



w  = 500.0 # lb
a  = 1.0 # ft
b  = 1.5 # ft
c  = 5.0 # ft
length_ac=(a**2+c**2+b**2)**0.5
length_ab=(a**2+c**2+(2*a-b)**2)**0.5
length_ad=(c**2+b**2)**0.5
#w=fab*(2*a-b)/length_ac+fac*b/length_ac+fad*b/length_ad
#0=fab*a/length_ab-fac*a/length_ac
#0=fab*c/length_ab+fac*c/length_ac-fad*c/length_ad
coeffe=[
        [(2*a-b)/length_ab,b/length_ac,b/length_ad],
        [a/length_ab,-a/length_ac,0],
        [c/length_ab,c/length_ac,-c/length_ad],
        ]
constant=[w,0,0]

solution1 = solve_linear_system(coeffe, constant)
if solution1 is None:
    print("方程组无解")
elif isinstance(solution1, str):
    print(solution1)
else:
    print(f"解为: Fab = {solution1[0]:.5f}, Fac = {solution1[1]:.5f}, Fad = {solution1[2]:.5f}")

































