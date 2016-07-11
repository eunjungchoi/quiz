import unittest
import impl

class PythonTest(unittest.TestCase):

    def test_table_to_dict_list(self): #----------------- VV------
        table = [
            ['월', '일', '품명', '수량', '단가', '공급가액', '부가세', '코드', '거래처명'],
            ['01', '01', '사업용신용카드사용분', '', '', '10,364', '1,036', '00140', '한국맥도날드 서초뱅뱅점'],
            ['01', '01', '사업용신용카드사용분', '', '', '10,999', '1,101', '00406', '마이（부평점）'],
            ['01', '01', '사업용신용카드사용분', '', '', '1,818', '182', '00237', '르뽀미에도곡점']
        ]

        dic = [
            ['월':'01', '일' : '01', '품명' : '사업용신용카드사용분', '수량': '', '단가':'', '공급가액' : '10,364',
            '부가세': '1,036', '코드': '00140', '거래처명':'한국맥도날드 서초뱅뱅점' ],
            ['월':'01', '일' : '01', '품명' : '사업용신용카드사용분', '수량': '', '단가':'', '공급가액' : '10,999',
            '부가세': '1,101', '코드': '00460', '거래처명':'마이(부평점)' ],
            []
            ]

        def table_to_dic_list(table):
            header_list = table[0]
            dic_list = []
            
            for i in range(1, len(table)):
                each_list = {}
                for header, value in zip(header_list, table[i]):
                    each_list[header] = value
                dic_list.append(each_list)
            return dic_list


        dict_list = impl.table_to_dict_list(table)

        self.assertEqual('10,364', dict_list[0]['공급가액'])
        self.assertEqual('마이（부평점）', dict_list[1]['거래처명'])


    def test_filter_list(self): #------------------------------- VV  ------
        data = range(0, 100)

        filtered = impl.multiple_of_three(data)
        
        def multiple_of_three(data):
            data = [x * 3 for x in data]
            return data

        for number in filtered:
            self.assertTrue(number % 3 == 0)


    def test_json(self): #----------------- VV --------------------------
        data = '''{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}'''
        def pick_GlossTerm(data):
            results = []
            
            def _decode_dict(a_dict):
                try: results.append(a_dict['GlossTerm'])
                except KeyError: pass
                return a_dict
            json.loads(data, object_hook=_decode_dict)  
            return results[0]
        
        self.assertEqual('Standard Generalized Markup Language', impl.pick_GlossTerm(data))


    def test_sorted_distinct_list(self): #--------------------------------- VV --------------- 
        data = [1, 5, 8, 10, 4, 9, 11, 10, 8, 14, 3, 4]


        def sort_and_distinct(data):
            data = list(set(data))
            return sorted(data)

        self.assertEqual([1, 3, 4, 5, 8, 9, 10, 11, 14], impl.sort_and_distinct(data))


    def test_custom_sort(self): #----------------------------------- VV -----------------
        class Voucher:
            def __init__(self, trader, amount):
                self.trader = trader
                self.amount = amount


        data = [
            Voucher('GS마트', 125000),
            Voucher('7 Eleven', 8500),
            Voucher('신세계', 288000),
            Voucher('이마트', 80000),
        ]

        def sort_by_amount(data): 
            data.sort(key=lambda x: x.amount, reverse=True) 
            return data

        vouchers = impl.sort_by_amount(data)
        self.assertEqual('신세계', vouchers[0].trader)
        self.assertEqual('7 Eleven', vouchers[-1].trader)


    def test_dispatch_by_string(self): #---------------------------- VV -------------
        
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

        self.assertEqual(18, impl.calc('multiply', 6, 3))
        self.assertEqual(2, impl.calc('divide', 6, 3))
        self.assertEqual(9, impl.calc('add', 6, 3))
        self.assertEqual(3, impl.calc('subtract', 6, 3))


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

        def find_deepest_child(dic_tree):
            deepest_level = 0
            deepest_child = dic_tree

            if len(dic_tree):
                depth_level +=1
                deepest = dic_tree
                find_deepest_child(dic_tree)

            for key, value in dic_tree.items():

            else: 
                return deepest_child


        def find_nodes_that_contains_more_than_three_children(dic_tree):  # ------- .... ----
            parents_with_multiple_child = []

            for key, value in dic_tree.items():
                if len(dic_tree) >= 3:
                    parents_with_multiple_child.append(dic_tree):
                
                return parents_with_multiple_child.extend(find_nodes_that_contains_more_than_three_children(key))
            
            return set(parents_with_multiple_child)


        def count_of_all_distributions_of_linux(dic_tree):

            return counter


        self.assertEqual('OpenSolaris', impl.find_deepest_child(unix_tree))
        self.assertSetEqual({'Unix', 'BSD', 'Linux'}, impl.find_nodes_that_contains_more_than_three_children(unix_tree))
        self.assertEqual(7, impl.count_of_all_distributions_of_linux(unix_tree))



    def test_polymorphism(self):  #---------------------------  v ?? ---------------------
        messages = [
            impl.Notice('Welcome to chat'),
            impl.Message(userid=1, content='Hello World'),
            impl.Message(userid=2, content='Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
            impl.Message(userid=3, content='안녕하세요.'),
            impl.Message(userid=2, content='ありがとうございます。'),
        ]

        class Notice:
            def __init__(self, greeting):
                self.greeting = greeting
                self.draw(self.greeting)
                
            def draw(self):
                msg = '<li class="notice">' + self.greeting + '</li>' + '\n'
                return msg

        class Message:
            def __init__(self, userid, content):
                self.userid = userid
                self.content = content
                self.draw(self.userid, self.content)
            
            def draw(self):
                msg = '<img class="profile" src="${user_image(' + str(self.userid) + ')}">'
                msg += '<div class="message-content">' + self.content + '</div></li>'
                return msg
            

        def render_messages(messages, current_userid=1):
            final_html = messages[0]

            for message in messages[1:]:
                if message.userid == current_userid:
                    final_html += '<li class="right">' + message
                else:
                    final_html += '<li class="left">' + message

            print final_html


        self.assertEqual(
            '''<li class="notice">Welcome to chat</li>
<li class="left">
    <img class="profile" src="${user_image(1)}">
    <div class="message-content">Hello World</div>
</li>
<li class="right">
    <img class="profile" src="${user_image(2)}">
    <div class="message-content">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
</li>
<li class="left">
    <img class="profile" src="${user_image(3)}">
    <div class="message-content">안녕하세요.</div>
</li>
<li class="right">
    <img class="profile" src="${user_image(2)}">
    <div class="message-content">ありがとうございます。</div>
</li>''', impl.render_messages(messages, current_userid=2))

        