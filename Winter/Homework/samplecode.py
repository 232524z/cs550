from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('New Delhi', 'NCR region')
keyword_processor.add_keyword('Big Apple', 'New York')
new_sentence = keyword_processor.replace_keywords('I love Big Apple and new delhi.')
#returns 'I love New York and NCR region.'
print(new_sentence)