#트리 구현
#각 노드는 1개의 부모를 가짐
#노드가 제거되면, 해당 노드를 부모로 가지는 자식 노드들도 같이 제거함
#노드 = {부모, [자식 리스트]}
#딕셔너리로 구현
#key: ID
#value:
#parent ID
#child ID



import sys
input = sys.stdin.readline

N = int(input())

parentdata = list(map(int, input().split()))

erasenode = int(input())



def dfs_delete(node):
    
    parentdata[node] = -2 #제거 대상인 노드를 제거함
    
    for i in range(N):
        
        if node == parentdata[i]: #제거 대상인 노드를 부모로 가지는 노드들을 제거함
            dfs_delete(i)



dfs_delete(erasenode)

counter = 0

for i in range(N):
    
    if parentdata[i] != -2 and i not in parentdata: # 제거되지 않고 남아있는 노드 i의 자식이 없다면

        counter  += 1
 
print(counter)

#느낀점
#문제 이름에 낚이지 말기
#복잡한 자료구조를 구현하지 않고 풀 수 있는 방법을 찾기
#전파되는 구조라면 dfs를 쓰는 것이 좋음
#문제의 요구사항(리프 노드)를 주어진 자료구조에서 파악할 수 있는 방법 손으로 찾아보기





# N = int(input())


# node = list(map(int, input().split()))

# Tree = {}

# for nodeID in range(N):
#     Tree[nodeID] = [node[nodeID], []]

# for nodeID in range(N):
#     if(node[nodeID] != -1):
#         parentID = node[nodeID]
#         Tree[parentID][1].append(nodeID)


# targetID = int(input())

# parentID = Tree[targetID][0]

# if(parentID != -1):
#     Tree[parentID][1].remove(targetID) #해당 노드의 부모에서 자식 노드 제거

# removeIDs = [targetID] 

# while(removeIDs):
#     removeID = removeIDs.pop()

#     childID = Tree[removeID][1]
    
#     removeIDs += Tree[removeID][1] #제거 대상에 자식 노드 추가
    
#     Tree[removeID] = [999, []] #해당 노드 제거


# cnt = 0

# for nodeID in Tree.keys():
#     if(Tree[nodeID][0] != 999 and not Tree[nodeID][1]):
#         cnt += 1

# print(cnt)