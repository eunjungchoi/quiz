

def test_json(self):
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
                                    "GlossSeeAlso": ["GML", "XML", {"GlossTerm": "abc"}]
                                },
                                "GlossSee": "markup"
                            }
                        }
                    }
                }
            }'''
    
d = '''[
    {
        "a": [3], 
        "b": 2
    }, 
    [1,2,3], 
    "x"
]'''
    
    
data2 = {
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
                                "GlossSeeAlso": [
                                    "GML", 
                                    "XML",
                                    "GlossTerm"
                                ]
                            },
                            "GlossSee": "markup"
                        }
                    }
                }
            }
        } 


import collections

def traverse_json_object(j, check=lambda x: False, check_None=None, check_dict=None, check_list=None):
#     if j is None:
#         check_None(j)
#     if isinstance(j, int):
#         check_int(j)
#     if isinstance(j, bool):
#         check_bool(j)
#     if isinstance(j, str):
#         check_str(j)

    if isinstance(j, collections.Iterable):
        if isinstance(data2, dict): 
            if check_dict is not None: check_dict(data2)
            for x in j.values():
                traverse_json_object(x)
        elif isinstance(data2, list):
            check_list(data2)
            for x in j:
                traverse_json_object(x)
    else:
        result = check(j)
        if result:
            return result

    
traverse_json_object(j, 
                     check_dict=lambda x: print("I am parsing:", x), 
                     check_list=lambda x: print ("I am a list:", x))

        
def check42(j):
    if j == '42':
        return True
    return False
        

    
def pick_GlossTerm_from_dict(data2):
    #print('- checking', data2)
    if data2 == None:
        return None
    
    if isinstance(data2, dict): 
        for key, value in data2.items():
            if key == "GlossTerm":
                return value

            if isinstance(value, dict) or isinstance(value, list):
                aa = pick_GlossTerm_from_dict(value)
                if aa != None:
                    return aa
    
    if isinstance(data2, list):
        for item in data2:
            bb = pick_GlossTerm_from_dict(item)
            if bb != None:
                return bb   
            
    return None



# stackoverflow에서 찾은 답 ----------------------------------------

def pick_GlossTerm(data):
    results = []
    
    def _decode_dict(a_dict):
        try: 
            x = a_dict['GlossTerm']
            results.append(x)
        except KeyError: 
            pass
        #a_dict['ok'] = 3
        return a_dict
    
    data2 = json.loads(data), object_hook=_decode_dict)
    
    return results[0]

traverse_json_object(data2, check=check42)

o        
#
pick_GlossTerm_from_dict(data2)


