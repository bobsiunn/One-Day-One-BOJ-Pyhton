import sys
input = sys.stdin.readline


t= int(input())

def checkGood():
    global n, phonebook

    phonebook.sort()
    print(phonebook)


    for index in range(n-1):
        phoneLen = len(phonebook[index])

        if(phonebook[index+1][:phoneLen] == phonebook[index]):
            return False
    
    return True

class TrieNode():
    def __init__(self):
        self.child = dict()
        self.end = False
    

def checkTrie():
    global n, phonebook

    root = TrieNode()

    for number in phonebook:
        node = root        

        for digit in number:
            if(node.end): #현재 number에 대한 접두어가 있다면
                return False

            if(digit in node.child): #이미 추가된 prefix 경로
                node = node.child[digit] #해당 prefix 경로로 이동    
            
            else: #새로운 prefix 경로
                node.child[digit] = TrieNode() #새로운 prefix 추가
                node = node.child[digit] #해당 prefix 경로로 이동
    
        if(node.child): #자신이 누군가의 접두어라면
            return False

        #prefix 추가가 완료된 경우 마지막 노드에 True 표기    
        node.end = True

    
    return True #모든 prefix가 성공적으로 추가되면 return
        


for _ in range(t):
    n = int(input())
    phonebook = [input().rstrip() for _ in range(n)]
    
    # print(phonebook)

    if(checkTrie()):
        print("YES")
    else:
        print("NO")



#prefix 문제
#문자열 정렬을 하면 사전순으로 정렬되므로 접두어는 바로 뒤에 위치할 수 밖에 없다
#113 -> 123 -> 1132가 있으면, 113 -> 1132 -> 123으로 정렬된다
#이를 활용해서 n과 n+1만 비교하면 된다

#트라이 알고리즘
#문자열을 효율적으로 저장할 수 있는 자료구조
#트리 구조로 위쪽 노드부터 아래쪽 노드로 갈수록 문자열이 쌓이는 형태 a -> ab,ac,ad -> abd, acd, adr 등등
#노드는 자신에 대한 child(다음 digit)들을 저장하고, end인지 아닌지 저장함(기본 False), 문자열 모두 삽입시 마지막에는 True
#매칭 시 내가 접두어거나, 나에 대한 접두어를 찾는 2가지 경우를 찾았어야 함