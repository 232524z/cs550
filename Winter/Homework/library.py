

#EXTRACT KEYWORDS

#finds any keywords in a string, including different names
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
#keyword_processor = KeywordProcessor(case_sensitive=True) makes it case sensative

#big apple is what is found, new york is what is returned
keyword_processor.add_keyword('Big Apple', 'New York')
#bay area is found
keyword_processor.add_keyword('Bay area')
#anything included that is not found is not returned
keyword_processor.add_keyword('connecticut')
#finds the keywords from a string
keywords_found = keyword_processor.extract_keywords('I love Big Apple and Bay Area.')
print(keywords_found)





#REPLACE KEYWORDS
#first term to be replaced, then new term
keyword_processor.add_keyword('New Delhi', 'NCR region')
new_sentence = keyword_processor.replace_keywords('I love Big Apple and new delhi.')
print(new_sentence)







#add multiple keywords at the same time
keyword_processor = KeywordProcessor()
keyword_dict = {
	"java": ["java_2e", "java programing"],
	"product management": ["PM", "product manager"]
}
# {'clean_name': ['list of unclean names']}
keyword_processor.add_keywords_from_dict(keyword_dict)
keyword_processor.add_keywords_from_list(["java", "python"])
keyword_processor.extract_keywords('I am a product manager for a java_2e platform')
# output ['product management', 'java']






#chekc number of terms
keyword_dict = {
	"java": ["java_2e", "java programing"],
	"product management": ["PM", "product manager"]
}
keyword_processor.add_keywords_from_dict(keyword_dict)
print(len(keyword_processor))
# output 4






keyword_processor.add_keyword('j2ee', 'Java')
'j2ee' in keyword_processor
# output: True
keyword_processor.get_keyword('j2ee')
# output: Java
keyword_processor['colour'] = 'color'
keyword_processor['colour']
# output: color






keyword_processor.add_keyword('j2ee', 'Java')
keyword_processor.add_keyword('colour', 'color')
keyword_processor.get_all_keywords()
# output: {'colour': 'color', 'j2ee': 'Java'}






 keyword_dict = {
"java": ["java_2e", "java programing"],
	"product management": ["PM", "product manager"]
}
keyword_processor.add_keywords_from_dict(keyword_dict)
print(keyword_processor.extract_keywords('I am a product manager for a java_2e platform'))
# output ['product management', 'java']
keyword_processor.remove_keyword('java_2e')
# you can also remove keywords from a list/ dictionary
keyword_processor.remove_keywords_from_dict({"product management": ["PM"]})
keyword_processor.remove_keywords_from_list(["java programing"])
keyword_processor.extract_keywords('I am a product manager for a java_2e platform')
# output ['product management']






