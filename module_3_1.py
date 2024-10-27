calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    string_1 = str(string)
    result = (len(string_1), string_1.upper(), string_1.lower())
    count_calls()
    return result

def  is_contains(string,  list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    list_to_search1 = str(list_to_search).lower()

    count_calls()
    for i in range(len(list_to_search)):
        if list_to_search1[i] == string:
            result = True
            break
        else:
            result = False
            continue
    return result
print(string_info('Konfetka'))
print(string_info('ZeFirka'))
print(is_contains('Morozhenka', ['pechenka', 'marmeladka', 'tort']))
print(is_contains('yogurt', ['vishneviy', 'ananasoviy', 'vkusniy']))
print(calls)
