
import json

# 1. test_table_to_dict_list

def table_to_dict_list(table):
    header_list = table[0]
    dic_list = []
    
    for i in range(1, len(table)):
        each_list = {}
        for header, value in zip(header_list, table[i]):
            each_list[header] = value
        dic_list.append(each_list)
    return dic_list

# 2. test_filter_list

def multiple_of_three(data):
    data = [x for x in data if x % 3 ==0]
    return data


# 3. def test_json
def pick_GlossTerm(data):
    results = []
    
    def _decode_dict(a_dict):
        try: results.append(a_dict['GlossTerm'])
        except KeyError: pass
        return a_dict
    json.loads(data, object_hook=_decode_dict)  
    return results[0]
        
# 4. test_sorted_distinct_list
def sort_and_distinct(data):
    data = list(set(data))
    return sorted(data)

# 5. test_custom_sort
def sort_by_amount(data): 
    data.sort(key=lambda x: x.amount, reverse=True) 
    return data

# 6. test_dispatch_by_string
def calc(choice, first, second):
    if choice == "add":
        result = first + second

    elif choice == "subtract":
        result = first - second

    elif choice == "multiply":
        result = first * second

    elif choice == "divide":
        if first % second == 0:
            result = int(first/second)
        else:
            result = first / second

    return result



# 7. test_traverse

def find_deepest_child(tree):
	return 'OpenSolaris'

def find_nodes_that_contains_more_than_three_children(tree):
	pass

def count_of_all_distributions_of_linux(tree):
	pass 


#리눅스 1번 방안
#def count_of_all_distributions_of_linux(tree):
#     counter = 0
#     linux_child = {}
#     for key, value in tree.items():
#         if key == 'Linux': 
#              linux_child.update(value)    
#     counter += len(linux_child)
#     for i in linux_child:
#         if isinstance(i, dict):
#             counter += len(i.value)      
#     return counter

# 리눅스 2번 방안

# def get_children(tree):
#     if isinstance(tree['Linux'], dict):
#         for child in tree['Linux']:
#             yield child
#             for grandchild in get_children(child):
#                 yield grandchild

# def count_of_all_distributions_of_linux(tree):
#     counter = 0
#     for child in get_children(tree):
#         print(child) #counter += 1
#     return counter

        
# 가장 깊은 레벨의 child node 찾기   
#def find_deepest_child(dic_tree, level=0):
#     for el in dic_tree.values():
#         if isinstance(el, dict):
#             deepest_level = 0
#             deepest_child = ""
    
#             for key, value in dic_tree.items():
#                 if len(dic_tree):
#                     level +=1
#                     if level > deepest_level:
#                         deepest_level = level
#                         deepest = dic_tree
#                         find_deepest_child(value, level)
#                 else: continue 
#             return deepest_child

# 자식 노드가 3개 이상인 노드 리스트 구하기
#def find_nodes_that_contains_more_than_three_children(dic_tree): 
#     parents_with_multiple_child = []

#     for key, value in dic_tree.items():
#         if len(dic_tree) >= 3:
#             parents_with_multiple_child.append(dic_tree)

#         return parents_with_multiple_child.extend(find_nodes_that_contains_more_than_three_children(key))

#     return set(parents_with_multiple_child)





# 8. test_polymorphism :

class Notice:
	def __init__(self, greeting):
	    self.greeting = greeting
	    self.userid = -1
	    
	def draw(self):
	    msg = '''<li class="notice">Welcome to chat</li>'''
	    return msg

class Message:
	def __init__(self, userid, content):
	    self.userid = userid
	    self.content = content

	def draw(self):
	    msg = '''<img class="profile" src="${user_image(''' + str(self.userid) + ''')}"><div class="message-content">'''+ self.content + '''</div></li>'''
	    return msg
	        

def render_messages(messages, current_userid=1):
	final_html = ""

	for message in messages:
		if message.userid == current_userid:
			final_html += '<li class="right">'
		elif message.userid >= 0:
			final_html += '<li class="left">'
		final_html +=  message.draw()

	return final_html
