import re


class Post:
    '''
    Class for text post-processing functions
    '''
    
    def __init__(self):
        pass
    
    def rep_search(self, text):
        
        '''
        Function to catch repeating phrases
        '''
         
        for x in range(len(text.split(' '))):
            
            exp = rf'((\(*[\$€«\'\"]*\s*[A-Z]*\S+\b\s*[\$€\.\,\!\?\&\s]*[»\'\"]?\)*)([\s\,\:\;]+\(*[\$€«\'\"]*\s*\b\S+\b\s*[\$€\.\,\!\?\&\s]*[»\'\"]?\)*){{{x}}}([\s\,\:\;]+\(*[\$€«\'\"]*\s*\b\S+\s*[\$€\.\,\!\?\&\s]*[»\'\" ]?\)*[\.\?\!]?))\s*(\1)+'
            search = re.search(exp, text, re.UNICODE)
            find = re.findall(exp, text, re.UNICODE)
            
            if search:
                # starting index of the phrase repetitions
                start = search.span()[0]
                # area containing single instance of phrase that is repeated
                middle = start + len(find[0][0])
                # ending index of the phrase repetitions
                end = search.span()[1]
                
                new_text = text[0:middle] + text[end:]
                return self.rep_search(new_text)
                
        if not search:
            # If there are no repetitions in the string
            return text
 


class Pre:
    '''
    Class for text pre-processing functions
    '''
    
    def __init__(self):
        pass
    
    def fr_blocked_phrase(self, text):
        
        '''
        Function to get rid of unnecessary phrases found in some of our French articles
        '''
        
        exp1 = 'Ce contenu est bloqué car vous n\'avez pas accepté les traceurs. '
        exp2 = 'En cliquant sur « J’accepte », les traceurs seront déposés et vous pourrez visualiser les contenus . '
        exp3 = 'En cliquant sur « J’accepte tous les traceurs », vous autorisez des dépôts de traceurs pour le stockage de vos données sur nos sites et applications à des fins de personnalisation et de ciblage publicitaire. '
        
        exp_list = [exp1, exp2, exp3]
        
        for exp in exp_list:
            search = re.search(exp, text)
        
            if search:
                new_text = re.sub(exp, '', text)
                return self.blocked_phrase(new_text)
                
        if not search:
            return text
  
