def nextpermutation(narray):
    n = len(narray)

    # Find the rightmost number which
    # is smaller than the next number
    i = n - 2
    while i >= 0 & narray[i] >= narray[i + 1]:
        i -= 1

    # If no such number found, all permutations are done
    if i < 0:
        return False

    #Find the ceiling of narray
    j = n - 1
    while j > i & narray[j] <= narray[i]:
        j -= 1

    # Swap the found numbers
    temp = narray[i]
    narray[i] = narray[j]
    narray[j] = temp

    # Sort (reverse) the suffix after index i
    reverse(narray, i + 1, n - 1)

    return True

# Reverse helper method
def reverse(rarray, left, right):
    while left < right:
        rarray[left], rarray[right] = rarray[right], rarray[left]
        left += 1
        right -= 1

def findallpermutations(narray):
    narray.sort()
    result = [[], narray.copy()]

    while nextpermutation(result):
        result.append(narray.copy())

    return result