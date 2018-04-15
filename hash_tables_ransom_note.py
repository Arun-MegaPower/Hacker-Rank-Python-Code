from collections import Counter
    
def ransom_note(magazine, ransom):
    #Create Two Counters for magazine and ransom
    c_mag = Counter(magazine)
    c_ran = Counter(ransom)
    #Intersection of magazine and ransom should be equal to ransom
    if (c_mag & c_ran == c_ran):
        return True
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
