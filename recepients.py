from gevent import monkey; monkey.patch_socket()
import gevent
from gevent.pool import Pool
import json
from guidestar import get_guidestar
from pprint import pprint

def get_data(results,rec):
    name = rec['name']
    gs = get_guidestar(name)
    if gs:
        rec.update(gs)
        print len(results)
        pprint(rec)
    else:
        pass
    results.append(rec)

if __name__=="__main__":
    results = []
    try:
        recepients = json.load(file("recepients.json"))
    except:
        data = json.load(file("out.json"))
        tmichot, strings = data['tmichot'], data['strings']
        recepients = [ strings[str(x['r'])] for x in tmichot ]
        recepients = list(set(recepients))
        recepients = [ {'name' : x } for x in recepients ]
    
    pool = Pool(4)
    for rec in recepients:
        if rec.has_key('url') and False:
            results.append(rec)
        else:
            pool.spawn(get_data, results, rec)
    pool.join()
    print(len(results))
    json.dump(results,file("recepients.json","w"))

    
