

def permutation(char_list):
    if len(char_list) == 0:
        return []
    if len(char_list) == 1:
        return [char_list]

    
    final_list = []
    for i, key in enumerate(char_list):

        # copy all from char_list except key
        new_char_list = char_list[:]
        new_char_list.pop(i)
        #new_char_list = [k for k in char_list if k != key]
        
        all_subperms = permutation(new_char_list) # [[b,c], [c,b]]
        
        #
        for subperm in all_subperms:
#             each_list = [key]
#             each_list.extend(subperms[j]) # [a,b,c]   
            each_list = ([key] + subperm) # a + [b,c]
            final_list.append(each_list) # [[a,b,c]
    
    return final_list

print(permutation([]))

print(permutation(['a']))

print(permutation([1, 2]))

# sorted(a) == sorted([
#     ['a', 'b'],
#     ['b', 'a']
# ])

print(sorted(permutation(['a', 'b', 'c'])) == sorted([
    ['a', 'b', 'c'],
    ['a', 'c', 'b'],
    ['b', 'a', 'c'],
    ['b', 'c', 'a'],
    ['c', 'a', 'b'],
    ['c', 'b', 'a']
]))



t = (1,2,3)
t2 = (t[0], t[1], t[2], 4)
