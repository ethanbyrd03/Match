def match(w, i, j, N):
    if i == j:
        if N == 'A':
            return w[i] == 'a'
        elif N == 'B':
            return w[i] == 'b'
        elif N == 'C':
            return w[i] == 'a'
        else:
            return False

    if N == 'S':
        return ((match(w, i, i, 'A') and match(w, i+1, j, 'B'))
                or (match(w, i, i, 'B') and match(w, i+1, j, 'C')))
    elif N == 'A':
        for m in range(i, j):
            if match(w, i, m, 'B') and match(w, m+1, j, 'A'):
                return True
        return False
    elif N == 'B':
        for m in range(i, j):
            if match(w, i, m, 'C') and match(w, m+1, j, 'C'):
                return True
        return False
    elif N == 'C':
        for m in range(i, j):
            if match(w, i, m, 'A') and match(w, m+1, j, 'B'):
                return True
            if match(w, i, m, 'A') and match(w, m+1, j, 'C'):
                return True
        return False
    else:
        return False

