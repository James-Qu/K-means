import json as simplejson
import re

# clean string
#def clean(str):
 #   result=re.sub(r'[^\w]', ' ', str)
 #   return result


# parser json file
#def parser_Json(filename):
file = open(filename)
data = []
for line in file.readlines():
    dec_json = simplejson.loads(line)
	data.append([dec_json['id'], clean(dec_json['text'])])
		#print dec_json['id'], dec_json['text']
#	return data