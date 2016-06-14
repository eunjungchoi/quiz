

import unittest

class PythonTest(unittest.TestCase):

	maxDiff = None

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
										"GlossSeeAlso": ["GML", "XML"]
					                },
									"GlossSee": "markup"
					            }
					        }
					    }
					}
				}'''

 # 1. 위의 data는 현재 string으로 저장되어 있습니다. 
 # 2. 이를 딕셔너리로 변경하는 작업이 선행돼야 하는데, 이 부분은 아직 코드로 구현하지 못했습니다. 
 # 3. 대신, 스트링 타입을 일단 수동으로 딕셔너리로 변경하여, '딕셔너리 타입이 주어질 때'에 적용되는 함수로 짜보았습니다. 
 # 4. 아래 data2는 앞뒤로  ''', ''' 이 제거된 상태입니다. 

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
                                    "XML"
                                ]
                            },
                            "GlossSee": "markup"
                        }
                    }
                }
            }
        } 

		self.assertEqual('Standard Generalized Markup Language', pick_GlossTerm(data2))


def pick_GlossTerm(data):
    
    if data == None:
        return None
    
    if isinstance(data, dict): 
        for key, value in data.items():
            if key == "GlossTerm":
                return value

            if isinstance(value, dict) or isinstance(value, list):
                aa = pick_GlossTerm(value)
                if aa != None:
                    return aa
    
    if isinstance(data, list):
        for item in data:
            bb = pick_GlossTerm(item)
            if bb != None:
                return bb   
            
    return None




if __name__ == '__main__':
    unittest.main()



# 아래는 제가 테스트때 제출했던 코드로, stackoverflow에서 발견한 비슷한 코드를 약간 수정해서 붙여놨던 코드입니다. 
# 그때는 이해하지 못하고 그저 가져다 쓰기만 했었는데, 시험 후 아래 코드가 어떤 맥락인지 대략적인 의미를 따로 찾아보았습니다. 

# --------------------------------------------
# def pick_GlossTerm(data):
#     results = []
    
#     def _decode_dict(a_dict):
#         try: results.append(a_dict['GlossTerm'])
#         except KeyError: pass
#         return a_dict
#     json.loads(data, object_hook=_decode_dict)  
#     return results[0]


