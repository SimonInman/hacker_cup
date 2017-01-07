from math import atan2, degrees

TEST = """ 5
0 55 55
12 55 55
13 55 55
99 99 99
87 20 40"""

#raw_input = iter(TEST.splitlines()).next

def is_black(percent, x, y):
	x = x - 50
	y = y - 50 #recentre at 50,50
	if percent == 0:
		return False
	if not in_circle(x,y):
		return False

	#this is from 0 to 360, anticlockwise, zero at positive x axis
	canonical_degree = (degrees(atan2(y,x)) + 360) % 360

	degree_from_top_clockwise = (90 - canonical_degree) % 360

	return degree_from_top_clockwise <= percent * 360/float(100)


def in_circle(x,y):
	radius = (x)**2 + (y)**2
	if radius > 2500:
		return False
	else:
		return True

T = int(raw_input())
for case in range(1, T+1):
    percent, x, y = map(int, raw_input().strip().split())
    result = "black" if is_black(percent, x, y) else "white"
    print "Case #%s: %s" % (case, result)
