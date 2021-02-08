import numpy as np
import math
from sympy import *

# Calculate rotation matrix about X given an angle in radians
def r_x(theta):
	return np.array(([1,0,0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]))

# Calculate rotation matrix about Y given an angle in radians
def r_y(theta):
	return np.array(([np.cos(theta), 0, np.sin(theta)], [0, 1, 0],[-np.sin(theta), 0, np.cos(theta)]))

# Calculate rotation matrix about Z given an angle in radians
def r_z(theta):
	return np.array(([np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]))

# Calculate Euler parameters given a rotation matrix
def euler_from_rotation(r):
	e_4 = .5 * np.sqrt(1 + r[0,0] + r[1,1] + r[2,2])
	e_1 = (r[2,1] - r[1,2]) / (4 * e_4)
	e_2 = (r[0,2] - r[2,0]) / (4 * e_4)
	e_3 = (r[1,0] - r[0,1]) / (4 * e_4)

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

def symbolic_T_from_d_and_h():
	alpha = Symbol("alpha")
	a = Symbol("a")
	d = Symbol("d")
	theta = Symbol("theta")
	return Matrix([[cos(theta), -sin(theta), 0, a],
				   [sin(theta) * cos(alpha), cos(theta)*cos(alpha), -sin(alpha), -sin(alpha) * d],
				   [sin(theta)*sin(alpha), cos(theta)*sin(alpha), cos(alpha), cos(alpha) * d],
				   [0, 0, 0, 1]])

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

def main():
	print("Hello World")

	#print(T_from_d_and_h([math.radians(90), 0, 4, math.radians(90)]))

	# ans = hw2_p3c()
	# ans = hw2_p1()
	# ans = hw3_p1()
	# ans = h3_p2c()
	ans = symbolic_T_from_d_and_h()
	print(ans)



if __name__ == '__main__':
	main()