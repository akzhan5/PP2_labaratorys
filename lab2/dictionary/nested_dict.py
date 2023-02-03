#dict contain dict - nested dict
myfamily = {
    'child1': {
        'name': 'Akzhan', 
        'age': 17
    },
    'child2': {
        'name': 'Aishu',
        'age': 12
    }
}

# 3 dict, then into one dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfam = {
    'ch1': child1,
    'ch2': child2, 
    'ch3': child3
}