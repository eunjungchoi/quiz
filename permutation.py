
def permutation(char_list):
    final_list = []

    if len(char_list) == 0:
        return []
    if len(char_list) == 1:
        return char_list
    
    each_list =[]
    for i, key in enumerate(char_list):
        #each_list = []
        each_list.append(key)
        
        new_char_list = char_list[:]
        new_char_list.pop(i)
        
        each_list.extend(permutation(new_char_list))
    
    final_list.append(each_list)
    
    return final_list

print(permutation([]))

print(permutation(['a']))


print(permutation(['a', 'b']))

# sorted(a) == sorted([
#     ['a', 'b'],
#     ['b', 'a']
# ])

print(permutation(['a', 'b', 'c']))
# sorted(a) == sorted([
#     ['a', 'b', 'c'],
#     ['a', 'c', 'b'],
#     ['b', 'a', 'c'],
#     ['b', 'c', 'a'],
#     ['c', 'a', 'b']
# ])


# if __name__ == '__main__':
#     unittest.main()