#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter
island_perimeter2 = __import__('test').island_perimeter2

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    grid2 = [
        [0,0,0,0,0,0],
        [0,1,1,1,0,0],
        [0,1,1,1,0,0],
        [0,1,1,1,0,0]
    ]

    grid3 = [[0], [0], [0]]

    print(island_perimeter(grid))
    print(island_perimeter(grid2))
    print(island_perimeter(grid3))
    print('########################')
    print(island_perimeter2(grid))
    print(island_perimeter2(grid2))
    print(island_perimeter2(grid3))
