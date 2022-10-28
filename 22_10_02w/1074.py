# Z ( 시간초과 )
#
#
n, x, y = map(int, input().split())
c = -1
find = False


def re(nn, nx, ny):
    # print(nn, nx, ny)
    global c
    global find
    if find:
        return 0
    if nn > 1:
        re(nn-1, nx, ny)
        re(nn-1, nx, ny+2**(nn-1))
        re(nn-1, nx+2**(nn-1), ny)
        re(nn-1, nx+2**(nn-1), ny+2**(nn-1))
    else:
        if (nx == x and ny == y) or (nx == x and ny+1 == y) or (nx+1 == x and ny == y) or (nx+1 == x and ny+1 == y):
            if nx == x and ny == y:
                c += 1
                find = True
                print(c)
                return 0
                # print(nn, nx, ny)
            else:
                c += 1
            if nx == x and ny+1 == y:
                c += 1
                find = True
                print(c)
                return 0
                # print(nn, nx, ny)
            else:
                c += 1
            if nx+1 == x and ny == y:
                c += 1
                print(c)
                find = True
                return 0
                # print(nn, nx, ny)
            else:
                c += 1
            if nx+1 == x and ny+1 == y:
                c += 1
                print(c)
                find = True
                return 0
                # print(nn, nx, ny)
            else:
                c += 1
        else:
            c += 4


re(n, 0, 0)
