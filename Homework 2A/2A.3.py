# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 13:55:58 2025

@author: 1
"""

import numpy as np
W  = 10.0 # kg
alpha  = 45.0/180*np.pi # deg
beta  = 50.0/180*np.pi # deg
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
coeffe=[
        [0,0,0,np.sin(beta)],
        [0,0,1,0],
        [0.6,np.cos(alpha),-1,0],
        [-0.8,np.sin(alpha),0,0],
        ]
constant=[W*9.8,W*9.8/np.tan(beta),0,0]

solution1 = solve_linear_system(coeffe, constant)
if solution1 is None:
    print("方程组无解")
elif isinstance(solution1, str):
    print(solution1)
else:
    print(f"解为: FAC = {solution1[0]:.2f}, FBC = {solution1[1]:.2f}, FCD = {solution1[2]:.2f},FDE = {solution1[3]:.2f}")