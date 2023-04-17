import queue

with open('./labirynt.txt') as plik:
    maze = plik.readlines()
    for a in range(20):
        maze[a] = list(maze[a].rstrip('\n'))

    visited = [[False] * 20] * 20


def getMoves(x, y):
    moves = []
    for i in range(-1, 1):
        if x + i >= 0 and y - 1 >= 0:
            #print(i)
            if maze[x + i][y - 1] != '#' and not visited[x + i][y - 1]:
                tmp = [x + i, y - 1]
                # print(i)
                moves.append(tmp)

    for i in range(-1, 1):
        if x + i >= 0 and y + 1 <= 20:
            #print(i)
            if maze[x + i][y + 1] != '#' and not visited[x + i][y + 1]:
                tmp = [x + i, y + 1]
                # print(i)
                moves.append(tmp)

    if x - 1 >= 0:
        if maze[x - 1][y] != '#' and not visited[x - 1][y]:
            tmp = [x - 1, y]
            moves.append(tmp)

    if x + 1 >= 0:
        if maze[x + 1][y] != '#' and not visited[x + 1][y]:
            tmp = [x + 1, y]
            moves.append(tmp)

    #print(moves)
    return moves


def solve(sx, sy, gx, gy):
    q = queue.Queue()
    q.put([sx, sy])

    newPath = []

    while q.qsize() > 0:

        newPath.append(q.get())
        path = newPath

        print(path)
        sx = path[len(path) - 1][0]
        sy = path[len(path) - 1][1]
        if sx == gx and sy == gy:
            return path
        moves = getMoves(sx, sy)
        visited[sx][sy] = True
        for m in moves:
            #print(m)
            newPath.append(m)
            print(newPath)
            print(q.put(newPath))
            print(newPath)


        #    q.put(newPath)


if __name__ == '__main__':
    for a in maze:
        print(a)
    for a in visited:
        print(a)
    print(maze[0][6])
    solve(0, 0, 20, 20)
    # print(visited)
