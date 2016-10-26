def canWinNim(n):
    if n < 0:
        return False

    if n == 0:
        return True
    else:
        return canWinNim(n-3) or canWinNim(n-2) or canWinNim(n-1)

print(canWinNim(11))
