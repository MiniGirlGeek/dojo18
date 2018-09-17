points = [(568.2,200.2),
		  (560.7,187.2),
		  (392.3,271.1),
		  (348.8,195.8), 
		  (348.8,195.8), 
		  (345.9,190.8), 
		  (303.3,117.1), 
		  (284.1,128.2), 
		  (312.9,184.8), 
		  (232.1,242.5), 
		  (241.1,258.1), 
		  (325.4,209.3), 
		  (367.8,292.4), 
		  (360.2,483.2), 
		  (429.8,483.2), 
		  (415.3,301.1)]

import random

def get_sides(points):
	sides = []
	for i in range(len(points)):
		if i != len(points) - 1:
			point1 = points[i]
			point2 = points[i + 1]
		else:
			point1 = points[i]
			point2 = points[0]
		if point1[0] != point2[0]:
			m = (point1[1] - point2[1]) / (point1[0] - point2[0])
		else:
			m = 1000000000
		c = point1[1] - m * point1[0]

		sides.append({'m': m, "c": c, 1: point1, 2: point2})
	return sides

def are_intersecting(side, ray):
	if side['m'] == ray['m']:
		return False
	x = (ray['c'] - side['c']) / (side['m'] - ray['m'])
	y = side['m'] * x + side['c']

	if is_on_side(x, y, side):
		return True
	else:
		return False

def is_on_side(x, y, side):
	if side[1][0] < side[2][0]:
		if x not in range(int(side[1][0]), int(side[2][0])):
			return False
	else:
		if x not in range(int(side[2][0]), int(side[2][0])):
			return False

	if side[1][1] < side[2][1]:
		if y not in range(int(side[1][1]), int(side[2][1])):
			return False
	else:
		if y not in range(int(side[2][1]), int(side[2][1])):
			return False

def get_ray(x, y):
	ray = {'m': 0, "c": y}
	return ray

x = random.randint(0, 800)
y = random.randint(0, 600)

def get_point_in_shape(points):
	sides = get_sides(points)
	found = False
	while not found:
		x = random.randint(0, 800)
		y = random.randint(0, 600)
		ray = get_ray(x, y)
		intersections = 0
		for side in sides:
			if are_intersecting(side, ray):
				intersections += 1
		if intersections % 2 == 1:
			found = True
		else:
			found = False

print(get_point_in_shape(points))






