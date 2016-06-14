


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

	    self.assertEqual('OpenSolaris', find_deepest_child(unix_tree))
	    self.assertSetEqual({'Unix', 'BSD', 'Linux'}, find_nodes_that_contains_more_than_three_children(unix_tree))
	    self.assertEqual(7, count_of_all_distributions_of_linux(unix_tree['Linux']))


# 가장 깊은 레벨의 child node 찾기 

def find_deepest_child(dic_tree):
    ''' 
    아래 _find_deepest_child(dic_tree) 함수와 함께 사용된다.
    _find_deepest_child 함수는 튜플을 반환한다. depth를 함께 재귀함수에 넣어 카운트하기 위해서다. 
    문제의 해답은 deepest_child만 리턴해야 하기 때문에, 이를 처리하기 위한 함수를 따로 빼준다. 
    '''
    result = _find_deepest_child(dic_tree)
    deepest_child, depth = result
    return deepest_child


def _find_deepest_child(dic_tree):
	''' 
	딕셔너리 타입의 트리가 들어올 때, 가장 depth가 큰 노드의 이름과 그 depth의 튜플을 리턴한다. 
	recursive하게 돈다.
	'''
	max_depth_child = None
	max_depth       = -1

	for key, value in dic_tree.items():
		if value == None:
		    (child_key, child_depth) = (key, 1)    
		else:
		    (child_key, child_depth) = _find_deepest_child(value)

		
		(child_key, child_depth) = _find_deepest_child(value) if value is not None else (key, 1)
		
		child_depth += 1

		if child_depth > max_depth:
			max_depth_child = child_key
			max_depth = child_depth

	return (max_depth_child, max_depth)


# 자식 노드가 3개 이상인 노드 리스트 구하기

def find_nodes_that_contains_more_than_three_children(dic_tree):
    parents_of_multi_child = []
    
    for child_key, subtree in dic_tree.items():
        if subtree == None:
            continue
            
        if len(subtree) >= 3:
            parents_of_multi_child.append(child_key)

        descendants3 = find_nodes_that_contains_more_than_three_children(subtree)
        parents_of_multi_child.extend(descendants3)

    return set(parents_of_multi_child)


# 'Linux'의 모든 자식 노드 수 구하기 

# 함수를 호출할 때, argument에 unix_tree['Linux']라고 입력했을 때만 동작합니다. 
# root node를 인풋값으로 넣었을 때 그 아래의 모든 자식 노드들이 나오게 짰습니다. 
# unix_tree를 인자로 넣어서 Linux 노드를 한번 찾은 다음에, 그 자식노드를 짜게 하려다보니, 재귀함수를 도는 과정에서 조금 복잡해져서 
# 이 문제는 아래와 같이 인자를 linux 노드부터 넣는다는 조건부로 풀었습니다. 
# self.assertEqual 에 테스트하는 인수에도 unix_tree['Linux']를 세팅해두었습니다. 


def count_of_all_distributions_of_linux(dic_tree):

    if dic_tree == None:
        return 0

    counter = 0
    for key, subtree in dic_tree.items():
        subtree_count = count_of_all_distributions_of_linux(subtree)
        counter += subtree_count + 1
        
    return counter



if __name__ == '__main__':
    unittest.main()


