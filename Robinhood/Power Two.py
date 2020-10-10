

def pairSummingToPowerofTwo(input):

    # calculate the maximum sum
    max_val = 2 * max(a)
    integer = 0
    # generate the possible power
    checklist = []

    while True:
        if max_val > 2 ** integer:
            check_list.append(2 ** integer)
            integer += 1
        else: 
            break
    
    dict = collections.defaultdict(int)

    for i in checklist:
        for j in a:
            dict[i - j] += 1

    # res = 0
    # for j in a:
    #     if j in dict:
    #         res += dict[i-j]
    # return res

    res = set()

    for i in a:
        for j in checklist:
            if (j-i, i) not in res:
                # mathematics --> j = i + i
                res.add((i, j-i))
                # find another one in hashmap
                res += dict[j-i]
    return ans


# o(n log(max(value)))
# o(n)

