traverse


좀더 중급 버전 :
    def get_deep_child(key, value):
        if value == None:
            (child_key, child_depth) = (key, 1)    
        else:
            (child_key, child_depth) = _find_deepest_child(value)
        return (child_key, child_depth)

    results = [get_deep_child(k,v) for k,v in dic_tree.items()]
    max_result = max(results, key=lambda (child_key, child_depth): child_depth)
    return max_result




#(child_key, child_depth) = _find_deepest_child(value) if value is not None else (key, 1)
