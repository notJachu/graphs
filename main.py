import queue

with open('./labirynt.txt') as plik:
    maze = plik.readlines()
    for a in range(20):
        maze[a] = list(maze[a].rstrip('\n'))

    visited = []

    for i in range(20):
        tmp = []
        for j in range(20):
            tmp.append(False)
        visited.append(tmp)


def getMoves(x, y):
    moves = []
    for i in range(-1, 2):
        if 0 <= x + i < 20 and y - 1 >= 0:
            # print(i)
            if maze[x + i][y - 1] != '#' and not visited[x + i][y - 1]:
                tmp = [x + i, y - 1]
                # print(i)
                moves.append(tmp)

    for i in range(-1, 2):

        if 0 <= x + i < 20 and y + 1 < 20:
            # print(i)
            if maze[x + i][y + 1] != '#' and not visited[x + i][y + 1]:
                tmp = [x + i, y + 1]
                # print(i)
                moves.append(tmp)

    if 0 <= x - 1 < 20:
        if maze[x - 1][y] != '#' and not visited[x - 1][y]:
            tmp = [x - 1, y]
            moves.append(tmp)

    if 0 <= x + 1 < 20:
        if maze[y][x + 1] != '#' and not visited[x + 1][y]:
            tmp = [x + 1, y]
            moves.append(tmp)

    print("valid moves", moves)
    return moves


def solve(sx, sy, gx, gy):
    q = queue.Queue()
    q.put([[sx, sy]])

    while not q.empty():

        s = q.get()
        print("entire path ", s)
        print("last node ", s[-1])
        lastNode = s[-1]

        visited[lastNode[0]][lastNode[1]] = True

        valid = getMoves(lastNode[0], lastNode[1])

        for v in valid:
            if v[0] == gx - 1 and v[1] == gy - 1:
                print("PATH TO EXIT", s)
                return s
            p = []
            for k in s:
                p.append(k)
            p.append(v)
            print("new q", p)
            print("old q", s)
            q.put(p)
            #print("new q", s)


if __name__ == '__main__':
    for a in maze:
        print(a)
    # visited[0][1] = True
    for a in visited:
        print(a)
    print(maze[0][6])
    path = solve(0, 0, 20, 20)
    for c in path:
        maze[c[0]][c[1]] = '*'
    #getMoves(0, 1)
    # print(visited)
    for a in maze:
        print(a)
