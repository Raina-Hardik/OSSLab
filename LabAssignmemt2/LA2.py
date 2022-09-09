import os
import csv


#---------------------------------------------------#
#               Function Definitions                #
#---------------------------------------------------#

def duplicate(LIST):
    ans = []
    for i in range(len(LIST)):
        k = i + 1
        for j in range(k, len(LIST)):
            if(LIST[i]==LIST[j]) and LIST[i] not in ans:
                ans.append(LIST[i])
    return ans
print(duplicate(list((10, 20, 30, 20, 20, 30, 40, 50, -20, 60))))

def group(LIST, SIZE):
    result = []
    while(len(LIST)!=0):
        result.append(list(LIST[:SIZE]))
        LIST = LIST[SIZE:]
    return result
print(group(list((10, 20, 30, 20, 20, 30, 40, 50, -20, 60)), 3))

def lensort(LIST):
    return sorted(LIST, key = lambda x:len(x))
print(lensort(list(('apple', 'banana', 'cat', 'dog', 'elephant'))))

filepath = str(input("FILE PATH: "))
fileExtn = (os.path.splitext(filepath)[1])
print(fileExtn)

def extsort(LIST):
    return sorted(LIST, key = lambda x:(os.path.splitext(x)[1]))

def counter(filepath='./temp.txt'):
    num_word = 0
    num_line = 0
    num_char = 0

    with open(filepath, 'r') as f:
        for line in f:
            num_line += 1
            word = '\0'
            for letter in line:
                if (letter != ' ' and word == '\0'):
                    num_word += 1
                    word = '*'
                elif (letter == ' '):
                    word = '\0'
                num_char += len(letter)

    print("Num Word: ", num_word)
    print("Num Line: ", num_line)
    print("Num Char: ", num_char)
counter('temp.txt')

def reverse(filepath='./temp.txt'):
    with open(filepath, 'r') as f:
        for line in f:
            print(line[::-1])
reverse()

def wrap(filepath='./temp.txt', size=20):
    cur = 0
    with open(filepath, 'r') as f1:
        with open('temp.txt', 'a') as f2:
            while True:
                c = f1.read(1)
                if not c:
                    break
                if cur == size or c == "\n":
                    f2.write("\n")
                    cur = 0
                if c != "\n":
                    f2.write(c)
                cur = cur + 1
wrap()

def _map(func, *args):
    for i in zip(*args):
        yield func(*i)
_map(operator.mul, [1,2,3], [4,5,6])

def triplets(num):
    return [(a,c-a,c) for c in range(2,num) for a in range(1,c//2+1)]

def filterOdd(LIST=[1,2,3]):
    return list(x for x in LIST if (x%2 == 1))


def parse_csv(filepath='./CSVFILE.csv'):
    teams = []
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["rating"] = int(row["rating"])
            teams.append(row)
    return teams
print(parse_csv())

def mutate(word='cat'):
    ans=[word]
    i=0
    _len=len(word)
    alphabets=map(chr,range(97,123))

    while i<_len:
        original=word
        ans.append(original[:i]+original[i+1:])
        if i<_len-2:
            ans.append(original[:i]+original[i+1]+original[i]+original[i+2:])
        elif i<_len-1:
            ans.append(original[:i]+original[i+1]+original[i])
        for x in alphabets:
            ans.append(original[:i]+x+original[i+1:])
            for x in alphabets:
                ans.append(word+x)
                ans.append(x+word)
                ans.append(original[:i]+x+original[i:])
        i=i+1
    return ans
print(mutate())

def nearly_equal(word1, word2):
    if word1 != word2 and (word1 in mutate(word2)):
        return True
    else:
        return False

def makeKey(string):
	key = ''
	for ch in sorted(string):
		key += ch
	return str(key)

def findAnagram(LIST):
	group = dict()
	for ele in LIST:
		if group.get(makeKey(ele)) == None:
			group[makeKey(ele)] = [ele]
		else:
			group[makeKey(ele)].append(ele)
	return group
print(findAnagram(list(('ate','eat','bat','tab','cat','tea'))))
