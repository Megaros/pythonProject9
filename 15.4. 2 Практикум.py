import json
with open('json_example_QAP.json') as f:
     strfile = f.read()
     templates = json.loads(strfile)

# with open('json_example_QAP.json', encoding='utf8') as f:
#     templates = json.load(f)
print(type(templates)) # <class 'list'>
print(type(templates[1])) # <class 'dict'>
# print(templates[0]['timestamp'])
def ErrorLog(item, value, string):
    Error.append({item: f'{value}, {string}'})
def CheckStrValue(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False
def CheckUrl(item):
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False



listOfItems = {
    'timestamp': 'int',
    'referer': 'url',
    'location': 'url',
    'remoteHost': 'str',
    'partyId': 'str',
    'sessionId': 'str',
    'pageViewId': 'str',
    'eventType': 'val',
    'item_id': 'str',
    'item_price': 'int',
    'item_url': 'url',
    'basket_price': 'str',
    'detectedDuplicate': 'bool',
    'detectedCorruption': 'bool',
    'firstInSession': 'bool',
    'userAgentName': 'str'
}
Error = []
for items in templates:

    for item in items:
        #print(type(items[item]))
        if item in listOfItems:
            if listOfItems[item] == 'int':
                if not isinstance(items[item], int):

                    ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] =='str':
                if not isinstance(items[item], str):
                     ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'bool':
                if not isinstance(items[item], bool):
                    ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'url':
                if not CheckUrl(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'val':
                if not CheckStrValue(items[item],['itemBuyEvent', 'itemViewEvent']):
                    ErrorLog(item, items[item], f'ожидали значение  itemBuyEvent или itemViewEvent')
            else:
                ErrorLog(item, items[item], 'неожиданноее значение')
        else:
             ErrorLog(item, items[item], 'неожиданная переменная')
if Error == []:
    print('Ошибок не обнаружено')
else:
    print('False')
    print(Error)









