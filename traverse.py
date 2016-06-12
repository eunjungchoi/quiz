


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

	    # def find_deepest_child(unix_tree):

	    # def find_nodes_that_contains_more_than_three_children(unix_tree):

	    # def count_of_all_distributions_of_linux(unix_tree): 

	    # 아래의 unitest를 통과시킬 수 있도록, 위에 3가지 함수를 짜야하는데, 어렵군요. 재귀함수나 트리 순회 같은 걸 해야 할 것 같은 느낌인데...ㅠ

	    self.assertEqual('OpenSolaris', find_deepest_child(unix_tree))
	    self.assertSetEqual({'Unix', 'BSD', 'Linux'}, find_nodes_that_contains_more_than_three_children(unix_tree))
	    self.assertEqual(7, count_of_all_distributions_of_linux(unix_tree))


if __name__ == '__main__':
    unittest.main()


