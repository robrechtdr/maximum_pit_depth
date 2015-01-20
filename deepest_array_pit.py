def solution(A):
    depths = _get_pit_depths(A)
    return max(depths)

def _get_pit_depths(A):
    depths = []
    for i, n in enumerate(A):
        for j, o in enumerate(A):
            for k, p in enumerate(A):
                if i < j < k:
                    triplet = (n, o, p)
                    if _is_pit(A, i, j, k):
                        depth = _get_depth(triplet)
                        depths.append(depth)
    return depths


def _is_pit(A, p, q, r):
    if _is_consecutively_ch("decr", A, p, q) and _is_consecutively_ch("incr", A, q, r):
        return True
    else:
        return False


def _is_consecutively_ch(change, A, a, b):
    first = A[a]
    for n in A[a:b + 1]:
        if change == "incr":
            if first > n:
                return False
        elif change == "decr":
            if first < n:
                return False
        first = n

    else:
        return True


def _get_depth(pit):
    return min(pit[0] - pit[1], pit[2] - pit[1])


A = [0, 1, 3, -2, 0, 1, 0, -3, 2, 3]
print solution(A)
#4
