from django_rq import job
import requests


@job
def my_background_task(search_id, **word):        
    # try:
    #     word = kwargs['word']
    #     sources = kwargs['sources']    
    # except KeyError:
    #     kwargs_ = kwargs['kwargs']
    #     word = kwargs_['word']
    #     sources = kwargs_['sources']       
    
    # try:
    #     search_word =  kwargs['word']
    # except KeyError:
    #     search_word = kwargs_['word']

    
    # andstring = ' '.join(str(e) for e in search_word['and'])   
    # orstring = ' '.join(str(e) for e in search_word['or']) 
    all_keywords = []
    # all_keywords.append(str(andstring))
    # all_keywords.extend(search_word['or'])
    # and_not = search_word['not']
    
    while ("" in all_keywords):
        all_keywords.remove("")            
    
    for i in all_keywords:        
        r = requests.post('http://localhost:5000/api/getdata/trustpilot', 
        json = {'search_id':search_id, 'word': i}, 
        headers={"Content-Type": "application/json"})                
        print(r.status_code)