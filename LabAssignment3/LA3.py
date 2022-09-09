#13
def rem_parent(LIST = ["example(.com)", "w3resource", "github(.com)", "stackoverflow(.com)"]):
    for i in range(len(LIST)):
        strt = LIST[i].find('(')
        stop = LIST[i].find(')')
        LIST[i] = LIST[i][:strt] + LIST[i][stop+1:]
    return LIST

#12
def non_repeating(word = "9920103079"):
    for ch in word:
        if(word.count(ch) == 1):
            return ch

#11
def find_unique(LIST = "9920103079"):
    ans = []
    for ele in LIST:
        if(LIST.count(ele) == 1):
            ans.append(ele)
    return ans

#10
def counter(filepath='./temp.txt'):
    words = {}
    with open(filepath, 'r') as f:
        for line in f:
            for word in line.split():
                if(word in words):
                    words[word] += 1
                else:
                    words[word] = 1
    return(max(words, key=words.get), words[max(words, key=words.get)])

#9
def bin_r(vector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], start = 0, end = 10, target = 5):
    if end >= start:
        mid = (start+end)//2
        if(vector[mid]==target):
            return mid
        elif(target > arr[mid]):
            bin_r(vector, mid, end, target)
        else:
            bin_r(vector, start, mid, target)
    else:
        return -1

def bin_i(vector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], start = 0, end = 10, target = 5):
    while(end >= start):
        mid = (start + end)//2
        if(vector[mid]==target):
            return mid
        elif(target>vector[mid]):
            start = mid
        else:
            end = mid
    return -1

#8
def handlePurchase(machine):
    item = input("ITEM: ")
    price = 0
    try:
        price = machine[item]
    except KeyError:
        print("Try Again!! 404 Not Found")
        handlePurchase(machine)
    amt = int(input("AMT : "))
    try:
        price = machine[item]
        assert amt == price
    except AssertionError:
        print("Invalid Input!! \n Amount Must be Equivalent integer")
        handlePurchase(machine)
    print("Transaction Successfully Completed!! \n Have a Great Day")
    print(item + " : " + str(price))

def VendingMachine(filepath = 'VendingMachine.txt'):
    machine = {}
    with open(filepath, 'r') as a_file:
        for line in a_file:
            key, value = line.split('|')
            machine[key] = int(value)
    handlePurchase(machine)

#7
def read_multi(_file_ = 'temp.txt', *args):
    LIST = []
    _args = list(args)
    _args.append(_file_)
    for file in _args:
        with open(file, 'r') as File:
            while(True):
                ch = File.read(1)
                if not ch:
                    break
                LIST.append(ch)
    return LIST

#6
def csString():
    LIST = [x for x in input("INPUT : ").split(', ')]
    LIST = [ele*2 for ele in LIST]
    return LIST

#5
def f(x,y,z):
    if 0<=y<10 and 0<=z<10 and x[z][y]=='1':
        x[z][y]='0'
        for dy,dz in [[-1,0],[1,0],[0,-1],[0,1]]:f(x,y+dy,z+dz)

def Q5(x = [[1,1,0,0,0,0,0,1,1,1],
            [1,0,0,0,0,0,0,1,1,1],
            [0,0,0,0,0,0,0,1,1,1],
            [0,0,1,0,0,0,1,0,0,0],
            [0,0,0,0,0,1,1,1,0,0],
            [0,0,0,0,1,1,1,1,1,0],
            [0,0,0,1,1,1,1,1,1,1],
            [1,0,0,0,1,1,1,1,1,0],
            [1,1,0,0,0,1,1,1,0,0],
            [1,1,1,0,0,0,1,0,0,0]]):

    islands = 0

    for i in range(10):
        for j in range(10):
            if x[j][i]=='1':
                islands+=1;f(x,i,j)
    print("Number of islands: ")
    return 5

#4
def permute(digits = "99"):
    if digits == "":
        return []
    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    result = [""]
    for num in digits:
        temp = []
        for an in result:
            for char in string_maps[num]:
                temp.append(an + char)
        result = temp
    return result

#3
def NLargest(LIST = [10, 20, 30, 40, 50], N = 3):
    ans = []
    for _ in range(N):
        ans.append(LIST.pop(LIST.index(max(LIST))))
    return ans

#2
def valuesort(DICT = {1: 1, 2: 9, 3: 4}):
    ans = {}
    sorted_keys = sorted(DICT, key=DICT.get)
    for w in sorted_keys:
        ans[w] = DICT[w]
    return ans

#1
def invertdict(DICT = {"a": 1, "b": 2, "c": 3, "d": 2}):
    return (dict([(v, [k for k, v1 in DICT.items() if v1 == v]) for v in set(DICT.values())]))

