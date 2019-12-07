def oneEditAway(s1, s2):

    if(abs(len(s1) - len(s2)) > 1):
        return False
    flag = 0
    if(len(s1) == len(s2)):

        for i in range(len(s1)):
            if(flag > 1):
                return False
            if(s1[i] != s2[i]):
                flag += 1
        return True

    if (len(s1) > len(s2)):
        greater = s1
        smaller = s2
    else:
        greater = s2
        smaller = s1

    j, k = 0, 0
    for i in range(len(smaller)):
         if(smaller[j] != greater[k]):
            flag = flag + 1
            if(flag > 1):
                return False
            if(greater[k+1] != smaller[j]):
                return False
            else:
                k = k + 1
                flag = flag + 1
                continue
         j = j + 1
         k = k + 1
    return True

print(oneEditAway('abde', 'abgde'))