def next_permutation(old_string,remainder):
    permutations = []
    for i in range(len(remainder)):
        new_string = old_string+remainder[i]
        new_remainder = remainder[:i]+remainder[i+1:]
        permutations.append([new_string,new_remainder])
    return permutations

def permutate_string(string,remainder):
    if remainder=='':
        return [string]
    else:
        results = []
        for new_string,new_remainder in next_permutation(string,remainder):
            results.extend(permutate_string(new_string,new_remainder))
        return results

print(permutate_string('','abcd'))
