def solution(new_id):
    #1
    new_id = new_id.lower()    
    #2 
    new_id = ''.join([i for i in new_id if i in "0123456789-_.abcdefghijklmnopqrstuvwxyz"])
    #3 
    nxt = new_id
    new_id = new_id.replace('..','.')
    while new_id != nxt:
        new_id = nxt 
        nxt = new_id.replace('..','.')
    #4
    if new_id and new_id[0]=='.':
        new_id = new_id[1:]
    if new_id and new_id[-1]=='.':
        new_id = new_id[:-1]
    
    #5 
    if len(new_id)==0:
        new_id = 'a'
    #6 
    if len(new_id)>=16:
        new_id = new_id[:15]
    if new_id and new_id[-1]=='.':
        new_id = new_id[:-1]
    
    #7
    if len(new_id)<=2:
        while len(new_id)<3:
            new_id += new_id[-1]

    return new_id