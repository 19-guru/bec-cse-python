d1={'key1': 1, 'key2': 3, 'key3': 2} 
d2={'key1': 1, 'key2': 2} 
for(key,value) in set(d1.items()) & set(d2.items()): 
	print("%s: %s in present in both d1 and d2 "%(key,value))