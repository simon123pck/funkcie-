def spoluhlaskovy(ret):
    spoluh= 'h, ch, k, g, d, t, n, l, c, j,b, m, p, r, s, v, z'
    for i in range(len(ret)):
        if ret[i] in spoluh:
            return False
    return True


ret = input('zadaj retazec')
print(spoluhlaskovy(ret))

