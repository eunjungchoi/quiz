

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
		self.assertEqual('Standard Generalized Markup Language', pick_GlossTerm(data))



if __name__ == '__main__':
    unittest.main()


# stackoverflow에서 찾은 답 ----------------------------------------

def pick_GlossTerm(data):
    results = []
    
    def _decode_dict(a_dict):
        try: results.append(a_dict['GlossTerm'])
        except KeyError: pass
        return a_dict
    json.loads(data, object_hook=_decode_dict)  
    return results[0]