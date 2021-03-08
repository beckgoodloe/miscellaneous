import numpy as np
import math
from sympy import *
import matplotlib.pyplot as plt


# Calculate rotation matrix about X given an angle in radians
def r_x(theta):
    return np.array(([1, 0, 0], [0, np.cos(theta), -np.sin(theta)],
                     [0, np.sin(theta), np.cos(theta)]))


# Calculate rotation matrix about Y given an angle in radians
def r_y(theta):
    return np.array(([np.cos(theta), 0, np.sin(theta)], [0, 1, 0],
                     [-np.sin(theta), 0, np.cos(theta)]))


# Calculate rotation matrix about Z given an angle in radians
def r_z(theta):
    return np.array(([np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0], [0, 0, 1]))


# Calculate Euler parameters given a rotation matrix
def euler_from_rotation(r):
    e_4 = .5 * np.sqrt(1 + r[0, 0] + r[1, 1] + r[2, 2])
    e_1 = (r[2, 1] - r[1, 2]) / (4 * e_4)
    e_2 = (r[0, 2] - r[2, 0]) / (4 * e_4)
    e_3 = (r[1, 0] - r[0, 1]) / (4 * e_4)

    print(e_1**2 + e_2**2 + e_3**2 + e_4**2)

    return [e_1, e_2, e_3, e_4]


# Calculate Transformation matrix (T) given a row of d&h parameters [alpha(i-1), a(i-1), d(i), th(i)]
# theta and alpha should be in radians
def T_from_d_and_h(l):
    alpha, a, d, theta = l
    return np.array(([np.cos(theta), -np.sin(theta), 0, alpha],
                     [np.sin(theta)*np.cos(alpha), np.cos(theta) * np.cos(alpha), -np.sin(alpha), -np.sin(alpha)*d],
                     [np.sin(theta)*np.sin(alpha), np.cos(theta)*np.sin(alpha), np.cos(alpha), np.cos(alpha)*d],
                     [0,0,0,1]))


# Calculate Transformation matrix (T) given a row of d&h parameters [alpha(i-1), a(i-1), d(i), th(i)]
# theta and alpha should be in radians
def symbolic_T_from_d_and_h(l):
    alpha, a, d, theta = l
    if(isinstance(alpha, str)):
        alpha = Symbol(alpha)
    if(isinstance(a, str)):
        a = Symbol(a)
    if(isinstance(d, str)):
        d = Symbol(d)
    if(isinstance(theta, str)):
        theta = Symbol(theta)

    M = Matrix([[cos(theta), -sin(theta), 0, a],
                   [sin(theta) * cos(alpha), cos(theta)*cos(alpha), -sin(alpha), -sin(alpha) * d],
                   [sin(theta)*sin(alpha), cos(theta)*sin(alpha), cos(alpha), cos(alpha) * d],
                   [0, 0, 0, 1]])
    return M

#######################################################################################################


# Homework 2 Problem 1
def hw2_p1():
    phi = math.radians(30)
    psi = math.radians(-45)
    theta = math.radians(60)
    R_x = r_x(psi)
    R_y = r_y(theta)
    R_z = r_z(phi)
    R_total = np.dot(R_x, np.dot(R_z, R_y))
    print(R_total)
    print(euler_from_rotation(R_total))


# Homework 2 Problem 3 Part c
def hw2_p3c():
    T43 = np.array(([.5, -np.sqrt(3)/2, 0, 1],[0, 0, -1, 0],[np.sqrt(3)/2, .5, 0, 0],[0, 0, 0, 1]))
    T30 = np.array(([-.25, -.433, .866, .866], [.433, .75, .5, .5], [-.866, .5, 0, 2], [0, 0, 0, 1]))
    print(np.dot(T30,T43))


# Homework 3 Problem 1
def hw3_p1():
    r1 = r_y(math.radians(-30))
    r2 = r_x(math.radians(-30))
    R_satellite_to_earth = np.dot(r1, r2)

    v_satellite_wrt_ground = np.array(([0, -5, 3]))
    omega_satellite = np.array(([0, 0, .5]))
    p_astronaut_wrt_satellite = np.array(([2, 4, 0]))
    v_astronaut_wrt_satellite = np.array(([-.4, 1, .2]))

    return v_satellite_wrt_ground + np.dot(R_satellite_to_earth, np.cross(omega_satellite, p_astronaut_wrt_satellite)) + np.dot(R_satellite_to_earth, v_astronaut_wrt_satellite)


def h3_p2c():
    q = np.array(([np.pi/4, .25, -np.pi/6]))
    q_dot = np.array(([.8, .1, -.3]))

    th1, d2, th3 = q
    l1 = 1
    l3 = 1

    J = np.array(([-l3*np.sin(th1)*np.cos(th3) - l1*np.sin(th1), 0, -l3 * np.cos(th1) * np.sin(th3)],
                  [l3*np.cos(th1) * np.cos(th3) + l1 * np.cos(th1), 0, -l3 * np.sin(th1) * np.sin(th3)],
                  [0, 1, l3*np.cos(th3)],
                  [0, 0, np.sin(th1)],
                  [0, 0, -np.cos(th1)],
                  [1, 0, 0]))

    return np.dot(J, q_dot)


def h4_p1a():
    T10 = symbolic_T_from_d_and_h([0, 0, 0 ,'th1'])
    T21 = symbolic_T_from_d_and_h([math.radians(90), 0, 'L1', 'th2'])
    T32 = symbolic_T_from_d_and_h([math.radians(90), 0, 'd3', math.radians(90)])
    T43 = symbolic_T_from_d_and_h([0, 'L2', 0, 0])
    T40 = T10 * T21 * T32 * T43

    return T40


def h6_p1():
    a01 = 0
    a11 = 1
    a21 = 2
    a31 = 3
    a02 = 4
    a12 = 5
    a22 = 6
    a32 = 7
    b01 = 8
    b11 = 9
    b21 = 10
    b31 = 11
    b02 = 12
    b12 = 13
    b22 = 14
    b32 = 15
    A = np.zeros((16, 16))

    # 1
    A[0, a01] = 1

    # 2
    A[1, a02] = 1

    # 3
    A[2, a01] = 1
    A[2, a11] = 3
    A[2, a21] = 9
    A[2, a31] = 27

    # 4
    A[3, a02] = 1
    A[3, a12] = 3
    A[3, a22] = 9
    A[3, a32] = 27

    # 5
    A[4, b01] = 1

    # 6
    A[5, b02] = 1

    # 7
    A[6, b01] = 1
    A[6, b11] = 3
    A[6, b21] = 9
    A[6, b31] = 27

    # 8
    A[7, b02] = 1
    A[7, b12] = 3
    A[7, b22] = 9
    A[7, b32] = 27

    # 9
    A[8, a11] = 1

    # 10
    A[9, a12] = 1

    # 11
    A[10, b11] = 1
    A[10, b21] = 6
    A[10, b31] = 27

    # 12
    A[11, b12] = 1
    A[11, b22] = 6
    A[11, b32] = 27

    # 13
    A[12, a11] = 1
    A[12, a21] = 6
    A[12, a31] = 27
    A[12, b11] = -1

    # 14
    A[13, a12] = 1
    A[13, a22] = 6
    A[13, a32] = 27
    A[13, b12] = -1

    # 15
    A[14, b12] = 1
    A[14, b22] = 6
    A[14, b32] = 27
    A[14, b11] = 5
    A[14, b21] = 30
    A[14, b31] = 135

    # 16
    A[15, a12] = 1
    A[15, a22] = 6
    A[15, a32] = 27
    A[15, a11] = -5
    A[15, a21] = -30
    A[15, a31] = -135

    b = np.array([5, 10, 5, 5, 5, 5, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    coeffs = np.dot(np.linalg.inv(A), b)

    f_SV = np.reshape(coeffs[0:8], (2, 4))
    f_VG = np.reshape(coeffs[8:], (2, 4))

    resolution = 100

    time = np.linspace(0, 3, resolution)
    np.reshape(time, (1, -1))
    time = np.vstack((np.ones((time.shape)), np.vstack((time, np.vstack((time ** 2, time ** 3))))))

    x = []
    y = []
    for i in range(0, resolution):
        temp = np.dot(f_SV, time[:, i])
        x.append(temp[0])
        y.append(temp[1])

    for i in range(0, resolution):
        temp = np.dot(f_VG, time[:, i])
        x.append(temp[0])
        y.append(temp[1])

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    plt.ylim(0, 10.1)
    plt.xlim(0, 10.1)
    # plt.axis('equal')

    circle1 = plt.Circle((2.5, 7.5), 2.5, color='b', fill=False)
    circle2 = plt.Circle((7.5, 2.5), 2.5, color='r', fill=False)

    plt.gca().add_patch(circle1)
    plt.gca().add_patch(circle2)

    major_ticks = np.arange(0, 10.1, 1)
    minor_ticks = np.arange(0, 10.2, .2)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    plt.grid(color='lightgrey', which='major', linestyle='-', linewidth=.5)
    plt.grid(color='lightgrey', which='minor', linestyle='--', linewidth=.5)

    plt.plot(x, y)

    x_1 = [5, 4]
    y_1 = [10, 1]
    plt.scatter(x_1, y_1, c='red')

    # plt.show()

    # plt.clf()

    # time = np.linspace(0, 6, 2 * resolution)

    # fig, axs = plt.subplots(2)
    # fig.suptitle('X and Y Trajectories')
    # axs[0].plot(time, x)
    # axs[1].plot(time, y)

    # axs[1].set_xlabel("Time")

    # axs[0].set_ylabel("X Position")
    # axs[1].set_ylabel("Y Position")

    # plt.show()





def main():
    print("Hello World")

    # print(T_from_d_and_h([math.radians(90), 0, 4, math.radians(90)]))

    # ans = hw2_p3c()
    # ans = hw2_p1()
    # ans = hw3_p1()
    # ans = h3_p2c()
    # l2 = Symbol("l2")
    # th1 = Symbol("th1")
    # th2 = Symbol("th2")
    # d3 = Symbol("d3")
    # M = Matrix([[l2 * cos(th1) - d3 * sin(th1) * sin(th2), d3 * cos(th1) * cos(th2), cos(th1) * sin(th2)],
    #             [l2 * sin(th1) + d3 * cos(th1) * sin(th2), d3 * sin(th1) * cos(th2), sin(th1) * sin(th2)],
    #             [0, d3 * sin(th2), -cos(th2)]])
    # print(M.det())
    h6_p1()



if __name__ == '__main__':
    main()