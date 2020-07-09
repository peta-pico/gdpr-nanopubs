import json
import re

with open("data/GDPRfines.json") as json_file:
    data = json.load(json_file)
    data['@id'] = 'fine:data'
    for f in data['fines']:
        # print("Article violated: " + f['articleViolated'])
        f['@id'] = 'fine:'+str(f['id'])
        del f['id']
        del f['picture']
        articles = re.finditer('Art. (.+?) GDPR', f['articleViolated'])
        if articles:
            f['articleViolated'] = []
            for a in articles:
                replacement = re.sub('(.)([a-z])', ' (\\2', a.group(1))
                replacement = re.sub(' ','', replacement)
                if replacement:
                    f['articleViolated'].append("gdpr:"+replacement)
                else:
                    f['articleViolated'].append("gdpr:"+a.group(1))
            # print(f['articleViolated'])

    context = {}
    context['id'] = "http://example.com/id/"
    context['fine'] = "http://example.com/fines"
    context['authority'] = "http://example.com/authority"
    context['controller'] = "http://example.com/controller"
    context['date'] = "http://example.com/date"
    context['name'] = "http://example.com/name"
    context['picture'] = "http://example.com/picture"
    context['price'] = "http://example.com/price"
    context['source'] = "dct:source"
    context['summary'] = "dct:description"
    context['gdpr'] = "http://purl.org/adaptcentre/resources/GDPRtEXT#article"
    context['dct'] = "http://purl.org/dc/terms/"
    fines = {}
    fines['@id'] = "dct:hasPart"
    fines['@type'] = "@id"
    context['fines'] = fines
    articlesViolated = {}
    articlesViolated['@id'] = "http://example.com/articleViolated"
    articlesViolated['@type'] = "@id"
    context['articleViolated'] = articlesViolated
    data['@context'] = context

    with open("data/GDPRfines_clean.jsonld", 'w') as outfile:
        outfile.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
