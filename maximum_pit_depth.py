# tc: O(n**4)
# sc: O(n)
def get_maximum_pit_depth(A):
    """Get the depth of the deepest pit.
    """
    depths = _get_pit_depths(A)
    return max(depths)


# tc: O(n**4)
# sc: O(n)
def _get_pit_depths(A):
    """Get the depths of all occuring pits in the array.
    """
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


# tc: O(n)
# sc: O(1)
def _is_pit(A, p, q, r):
    """Check whether the triplet defined by p, q and r in the array is a pit.
    """
    if _is_consecutively_ch("decr", A, p, q) and _is_consecutively_ch("incr", A, q, r):
        return True
    else:
        return False


# tc: O(n)
# sc: O(1)
def _is_consecutively_ch(direction, A, a, b):
    """
    Check whether the values in the array from item with index a to item with
    index b are consecutively changing in a given direction.
    """
    first = A[a]
    for n in A[a:b + 1]:
        if direction == "incr":
            if first > n:
                return False
        elif direction == "decr":
            if first < n:
                return False
        first = n

    else:
        return True


# tc: O(1)
# sc: O(1)
def _get_depth(pit):
    """Get the depth of a given pit.
    """
    return min(pit[0] - pit[1], pit[2] - pit[1])
