


import unittest

class PythonTest(unittest.TestCase):

	maxDiff = None

	def test_traverse(self):
	    unix_tree = {
	        'Unix': {
	            'PWB/Unix': {
	                'System III': {
	                    'HP-UX': None
	                },
	                'System V': {
	                    'UnixWare': None,
	                    'Solaris': {
	                        'OpenSolaris': None
	                    }
	                }
	            },
	            'BSD': {
	                'Unix 9': None,
	                'FreeBSD': None,
	                'NetBSD': None,
	                'MacOS': None
	            },
	            'Xenix': {
	                'Sco Unix': {
	                    'OpenServer': None
	                },
	                'AIX': None,
	            },
	        },
	        'Linux': {
	            'Debian': {
	                'Ubuntu': None,
	                'Linux Mint': None
	            },
	            'Redhat': {
	                'CentOS': None,
	                'Fedora': None
	            },
	            'Gentoo': None
	        }
	    }

# 가장 깊은 레벨의 child node 찾기 

def find_deepest_child(dic_tree):
    result = _find_deepest_child(dic_tree)
    deepest_child, depth = result
    return deepest_child


def _find_deepest_child(dic_tree):
    ''' 트리 구조일 때, 전체 하위 노드 중 가장 depth가 깊은 자식노드의 이름과 depth level를 가져오는 것 '''
    ''' 딕셔너리 타입의 트리가 들어올 때, 가장 depth가 큰 노드의 이름과 그 depth의 튜플을 리턴한다. 
    
    recursive하게 돈다.
    입력을 None일 수 없다.
    
    '''
    max_depth_child = None
    max_depth       = -1

    for key, value in dic_tree.items():
        #
        if value == None:
            (child_key, child_depth) = (key, 1)    
        else:
            (child_key, child_depth) = _find_deepest_child(value)

        #
        (child_key, child_depth) = _find_deepest_child(value) if value is not None else (key, 1)
        #
        child_depth += 1
        if child_depth > max_depth:
            max_depth_child = child_key
            max_depth       = child_depth

    return (max_depth_child, max_depth)


# 좀더 중급 버전 :
#     def get_deep_child(key, value):
#         if value == None:
#             (child_key, child_depth) = (key, 1)    
#         else:
#             (child_key, child_depth) = _find_deepest_child(value)
#         return (child_key, child_depth)
    
#     results = [get_deep_child(k,v) for k,v in dic_tree.items()]
#     max_result = max(results, key=lambda (child_key, child_depth): child_depth)
#     return max_result

def find_nodes_that_contains_more_than_three_children(dic_tree):
    parents_of_multi_child = []
    
    for child_key, subtree in dic_tree.items():
        if subtree == None:
            continue
            
        # check direct children
        if len(subtree) >= 3:
            parents_of_multi_child.append(child_key)

        # ask descendants of subtree
        descendants3 = find_nodes_that_contains_more_than_three_children(subtree)
        parents_of_multi_child.extend(descendants3)

    return parents_of_multi_child



	    # def find_nodes_that_contains_more_than_three_children(unix_tree):

	    # def count_of_all_distributions_of_linux(unix_tree): 

	    # 아래의 unitest를 통과시킬 수 있도록, 위에 3가지 함수를 짜야하는데, 어렵군요. 재귀함수나 트리 순회 같은 걸 해야 할 것 같은 느낌인데...ㅠ

	    self.assertEqual('OpenSolaris', find_deepest_child(unix_tree))
	    self.assertSetEqual({'Unix', 'BSD', 'Linux'}, find_nodes_that_contains_more_than_three_children(unix_tree))
	    self.assertEqual(7, count_of_all_distributions_of_linux(unix_tree))


if __name__ == '__main__':
    unittest.main()


