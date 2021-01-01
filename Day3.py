def encountered_tree(rise, run):
    #rise = 1
    #run = 3
    i =0 # vertical index
    j =0 # horizontal index
    l = len(a[0]) # length of pattern before repeating
    count = 0
    for index in range(1,int(len(a)/rise)):
        i = i+rise
        j = (j+run)%l
        if a[i][j] == "#":
            count += 1
    return count

a=["..#.......#..##...#...#..#.#...","..##..#..#.....#.........#....#","...#.##..#.#......#.#....#.....","...#.....#......#...#..........",".......#.#..#..#....##....##...",".#......#......#.#..#....#.#...",".#..........#.....###.##..#.#..","....#...##...........#.........","##......#.#...#...#....##.#...#",".....#.....#.#..#....###...#..#",".#....#.........#...#.......#.#",".##......#.#.........#....#.#..","...#........###..#......##....#",".#.....###..........#...#....##","............#......#...#...#..#",".....#.#....#.#.#...........#.#","....#.....#...##.##.....###..#.",".....#.##......#.##.#...#.#.#..","##.....#.##.##....#..##......#.",".....#.....#........#........##","#..#...#.#.#..##....#....##..#.",".#......................##..#..","#.#.#................#.....#...","..#....#.#.#..##..#..#.....##..",".....###..#.............#....##","..#....#.#...#......###..#.....",".......####.....##......#......","..##...#..#...#.#..#......#....","..##..#..#.....#......##.##....",".#......#................#..#.#","...............#....#.......#..","#...........#.#.#........#.#...","...#...#..#.....##..#.##...#.#.",".#.#..#.#.....#...#..##....#.##",".........#...#.#.#....#.......#","............##.#..#.#........#.","#..#..#........#......####.....","..#.#...#...#...#.#...#..#..#..","#....................#.#.#....#",".......#.....#....#....##..#...",".......#.............##.....#..","..##..#.......#..#.........#..#","..##.#........#...#...#..#..#..","..##.#...#................#..#.","..#.....##...##......###.....#.",".....#.....#......#......#.....","....##.#.#....#.....#..........","...#...#.#.....#.###.....#....#","......##....#..##...##.#.......","......................##......#",".##......#...#...#...##.#.##.#.","#.......#...#.....#........#.#.","...............#......#.......#",".#..##...#....#.....###....##..","...#..###...#..#....#.#..#.....",".#...#....#.................#..",".......##....#..##......#.#....","....#.....#.....###...#....#...","..##..#..##........#...........","....#..#.#............#........","####.....##.........#....#.....","........#.....#......#......##.","#..........#........#....#...##","#..#...###.....##.....#.##...#.","......#....##.............#..#.","..#......###...#...#..##.....#.","#.##...#......##.###....#....#.","...............#....#.....###.#","#......#........#.#..##.#.....#","#..............#..##.#....#....",".##....###...#...#.#....#....#.",".......#...#.......#....#..##..","..##.#.....#..#...............#",".##..............#.......#...#.",".....#...#.#..#.........#..#...","........#.#.###......#..#......","..#.......###..#...#...........","............#.#.....#....#...#.","#...#..#......#..#......#......","..##..#......#..#.......#.....#","............#.##.....#.#...#...","....#.#...#.#...#........##....","........##...#...##.....#.#..#.",".#..........#.##...............","###.#..#...###..###..#........#","....#..#............#...#.#.#..",".#....###........#.......#...#.","..........#..#.....#......#....","..##..#.#....#..#.....##....#..","...#...............#......#....","......#.#.#...###.....##.#.....",".#...#.#.#.#....#.....#..#..#.#","..#.....#..##....#......#.#.#..","##.#....#.......#.#.#.......#..",".#.#.#........##.#....#........","...#..#...#.#.........#..#....#","#.#......#.#.#..#.#............","......#.....#.....#.......#..#.",".........#..#.##..#..###....#.#",".......#..........#..#.........","......#.#.##...#.#...##........","...........##..##.##....#......","..#..#...#.###...##.....#..#..#",".#...##.......#.#..........#..#","##......#...........#.#........","..#..#.....##..#.#.......#...#.",".#....#..#.....###.......#...#.","...#..#...#...###.#.###..#.....",".......#...#.##......#.#.#.#...",".#.......#...#...#...##........","...#........#....#..#.#...#.#..","..#............#.....#.#....#..","#.....#.#..#.#....#...#.#.#....","#......#......##.#...........#.",".#..#.........##.#........#....",".#....#.#...#........#......#..","....#..#..#....#..#.#.....#..#.",".##.#.....#..#.#...#.....#..###","#..#......#..##....##..#.......",".......#..##....#.###..........",".#......#..........#........#..",".........#.....#......#.#......",".....#..#.......#...#.#....#...",".#......#...#..#......#.....#.#","#.#.#..#.........#.......##....","...#..#.....#.#..#......#...#..",".##...#...#.#....#.....#.#...#.","..#......##......#....#.#..#...","....#.#.....#..#...........#...",".#........#....#....#...#......","..#.#.....#.......#.#.#.##..##.","...#..#.##.......#...#.........","....##.#.#..#.#..#.#.#..#.#.#.#","......#.......#.....#...##.#...","..#.##.....#....#...#...##.##.#","..##.........##.........#..#...",".....###......####..#.#...#....","...#....#....##.............#.#",".#.........#.......##..#.#.....","...#..#........#...............","........#........##......#.#...","##...#......#.....#.##........#",".............#.#........#......",".......##.........#.......#....","....#.......#......#..###....#.",".#.##........#.....#......#....","#...........##...#..##.........",".....#.#........#........##...#","#.........#..##.....#...#....#.",".........#...####..#....###....","###.#..##.......#....#....#.##.","...........#.....#.#...#..#....",".##......###.#.#.#....#........","....#..................#.###.#.","#..##...#......#...#......###..",".#.....#..##......#.#.#.#......","..##...#..#.......##.#.......#.","...#..#..##..##..##.#..####....","......#..#..............#.#####","....#....#..#...#...#.#........",".###...#.......#..#........#...","........#.#......##...#........",".#..#.......##.......#.....##..","...##..........##...........#..","......................#..#.#.#.","#..#.....#......#.....#....#.##","..#......#.....#....#...#.##.#.","............#...#...#......#.##","........##.......#......##.....","..#.##.....#....#..##...#......","........#.#...##.#..#...#....#.","...##............##.....#..#...","...###.##....#....#.#.#.#..#...","............#..#....#..#.....##","...#......##.......#......##..#",".......#......#........#.....#.",".#....#.##..........#..........","..###.........#..#...##.....#..","##....##..#.......###....#.#.#.","#.......#.#.##.................","..#..........#................#","....#.#....#...###...#......#..",".#..........#..#..##.....#...##",".#.....###....#.#...#.#........",".........##.........#..#.#.....",".#.....##....#......##.#....#..","###..#...#..#.........#......#.","..##.....#....#............#...",".....##.##....#.....#..#..#....",".......###...#..........#......","...#........#....#.##.#........","........###....##........##.#..","....#....#........#.....##.....",".#........#.#........#...#..#..","#..#..#......#....##.#..###....","...........#...#...#....#.#...#",".#..#.....#.##..#......##......","..#.#...............##..##.###.","...#.#...#............##.#..#..",".#.#....#....#................#","...#..#.#.##.#.#....#......#...",".........#..#.......##.##.#....","..............#..##.#.....#....","......#.........#...#...##.#..#","....##.....#.#...#.#.####.#....","#..#.#....#.##.......#....#....","...##....#...................##","##.#.......#....#.#.........#.#",".##.#..###...#.#.........#.....","...#.#.#..#...#...#.##....#..#.","....#.....###...#....##........",".............#....#....#....#..","#...#.....#.#...#.#............","#.#....#...........##.......#..","..#..#.........#....###.......#","....###..................##...#",".#........#.....##...#......#..","#..#......#..#.....#.##..#...#.","....#........#.##.#......#.....","#.#...#...............####...##","#.#.....##..#.####.............","##...##..#.##........#.#...#...","...#...........#............#..","...#..#..#........##...........","..#.##..#.#...#...#..#......#..",".....##......#...##.....##.....",".......##.....##....#..........","..........#.#...............#.#","#.#..........#..#..##..#...#..#",".#.#..#.###................#...","#...#...#....#...#....#.##.##..",".#................###.....##...",".....##.#.....##.#.....#.....##",".......#.......#......#.#......","..#....#......#.....#.....#..#.","#......#..##..####.....#.#..#..",".......#...###..#...#.....#....","#.#.#......#.............#..###",".#.#.......#..#.#..#..#...#.#..","..#.#......#......#.#....#.....","..#..###..#.#.....#....#.......","..........#........#......#..#.","##..........##....##..###.##...","...#....#.......#..##.......#..","##...#............##...#.#.#.#.","...........#...#.#....#.....##.",".#................#.......#...#","....##.#..#.#.........###.###.#","#..#...###..#...#......#..##...","..##........#.#..##.#..........","...#..#...#...............#.#..","##.##....#...#........#...#....","#..#......#.##.................",".....#..##.##.......#..........","...#.....#........#......#.....",".....#..#......#.....##...#....","#......#...###....#....###.....","................###..#..#..#.##","......#.......#..........#.#..#","###..#..#.##.............#.#...","....##.#.......#...#..##.......","..#.....##..#..#..#.#..........",".#.......#.#..#........##......","..............#.........#......","..#........##....#.#.#......##.",".#.#.........#.#...#.#.........","..........#..#.##.#....#...#.#.","............##....#.....###...#","#....#..#...#.#...#.....#....#.",".#...##.....#......#..#........",".#..#...###.#..##........#...#.","#..#...##.####.......#.....#...","#.##..#...#......#.#.......#.#.","#.#.....##...#.#...............","#...........##.##.#.........#..","...#...........#.#.#.#....#..#.","..#......#.#.#....##..#.#.....#",".........#.#.##...##...#.#.#...","...........#..#.####.#..#.#.###","#........#.#......#..#...#.....","...#....#......##...#.#........","......#.#....#.##....#....#..##",".......###......#.#.....#......","#..........##..................",".###.......##..#..##...##......","##.#..............#....#....##.","#....#.....#.##.....#..#....#.#",".......#.......#..#..#..##..#..","......#...........#..##....#...",".....#.......#..#......#..#..##",".##...#......#........#....#...",".....#..#....#...............##","..#.....#....#..#.##....#.#....","#.#......####...#..#.........#.","#.#........#..#........#...#...","..#..............#.......###.#.","...#.#....##.#......#........#.","....###.......##.#.....##.....#",".........#......#.#.......##.##",".......#.#....#.#...#...#....#.","....#....#....#.#.......##.....","#...#.....#..#.....#...........","#...#..#...#.#..#.............#","........###..#........#........",".............#....#..###..#.#.#","#...............#..#.#.........","##.....###..#......#...#....#..",".#...................##.#.##...","#..#........#.#...#..#...#.....","................#.#.........#..","#.....##.#.#...#..#.........##.","...#.....#....#..####.#........","....#.#...........#............",".....#........##..........#....","..#.......#.#.#.####..#......#.","#.......#...##.#.#..#.#.#......","##........#.#...###............","..##........#........#...#.#.#.","#.#..#.#.......#....#........#.","..............#....#.........#.","#....#.#........#.............#","..##...#..........#........#...","..#..#..#....#....#............"]
r1 = encountered_tree(1,1)
r2 = encountered_tree(1,3)
r3 = encountered_tree(1,5)
r4 = encountered_tree(1,7)
r5 = encountered_tree(2,1)
print(r1, r2, r3, r4, r5)
print(r1* r2* r3* r4* r5)