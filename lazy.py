from collections import deque

TEST = """ 5
4
30
30
1
1
3
20
20
20
11
1
2
3
4
5
6
7
8
9
10
11
6
9
19
29
39
49
59
10
32
56
76
8
44
60
47
85
71
91 """

#raw_input = iter(TEST.splitlines()).next

def solve(list_of_boxes):
    list_of_boxes.sort()
    d = deque(list_of_boxes)

    trips = 0
    while d:
        heavy_item = d.pop()
        if heavy_item < 50:
            boxes_needed = 50/heavy_item + (50 % heavy_item != 0) - 1
            for _ in range(boxes_needed):
                try:
                    d.popleft()
                except IndexError:
                    return trips # we've run out, can't make another trip - return

        trips += 1

    return trips

T = int(raw_input())
for case in range(1, T+1):
    items = []
    num_items = int(raw_input().strip())
    for item in range(num_items):
        items.append(int(raw_input().strip()))
    result = solve(items)
    print "Case #%s: %s" % (case, result)
