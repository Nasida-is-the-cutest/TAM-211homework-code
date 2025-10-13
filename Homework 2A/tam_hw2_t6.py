import numpy as np
from scipy.optimize import fsolve

def solve_angle(P, a, k):
    """
    求解静力学平衡问题中的角度 theta。
    
    参数:
    P : float, 施加的垂直力 (lb)
    a : float, 绳索 AB 的长度 (ft), 也是弹簧的未拉伸长度 (ft)
    k : float, 弹簧的劲度系数 (lb/ft)
    
    返回:
    theta_deg : float, 平衡时绳索 AB 与水平方向的夹角 (度)
    """
    
    def equilibrium_eq(theta_rad):
        """
        平衡方程: x和y方向合力为零，消去张力T后得到的关于theta的方程。
        返回方程左边 - P，目标是使其为0。
        """
        cos_t = np.cos(theta_rad)
        sin_t = np.sin(theta_rad)
        
        # 点A的坐标 (从B点(0,0)出发)
        # A_x = a * cos_t
        # A_y = -a * sin_t
        
        # 点C的坐标 (2a, 0)
        # 弹簧AC的当前长度
        L_ac = np.sqrt((2*a - a*cos_t)**2 + (a*sin_t)**2)
        # L_ac = a * np.sqrt(5 - 4*cos_t) # 简化形式
        
        # 弹簧力大小
        F_ac = k * (L_ac - a)
        
        # 弹簧力在x和y方向的分量
        # F_ac_x = F_ac * (2*a - a*cos_t) / L_ac
        # F_ac_y = F_ac * (a*sin_t) / L_ac
        
        # 绳索张力T在x和y方向的分量: T_x = -T*cos_t, T_y = T*sin_t
        # x方向平衡: -T*cos_t + F_ac_x = 0  => T = F_ac_x / cos_t
        # y方向平衡: T*sin_t + F_ac_y - P = 0
        # 代入T: (F_ac_x / cos_t) * sin_t + F_ac_y - P = 0
        #       F_ac_x * tan_t + F_ac_y - P = 0
        
        F_ac_x = F_ac * (2 - cos_t) / (np.sqrt(5 - 4*cos_t)) # 因为 L_ac = a*sqrt(5-4cos_t), (2a - a*cos_t)/L_ac = (2-cos_t)/sqrt(5-4cos_t)
        F_ac_y = F_ac * sin_t / (np.sqrt(5 - 4*cos_t))
        
        return F_ac_x * np.tan(theta_rad) + F_ac_y - P
    
    # 初始猜测 (40度转为弧度)
    initial_guess = np.radians(40.0)
    
    # 求解方程
    theta_solution_rad = fsolve(equilibrium_eq, initial_guess)[0]
    
    # 转换为角度
    theta_solution_deg = np.degrees(theta_solution_rad)
    
    return theta_solution_deg

# --- 主程序 ---
if __name__ == "__main__":
    # 输入变量
    P = 50.0  # lb
    a = 2.0   # ft
    k = 15.0  # lb/ft
    
    # 求解
    theta = solve_angle(P, a, k)
    
    print(f"平衡时的角度 θ = {theta:.2f}°")