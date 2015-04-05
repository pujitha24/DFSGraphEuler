#NAME        : P PUJITHA SRI LAKSHMI PALADUGU
#NET ID      : PXP142730
#DATE STARTED: 2/1/2014.
#PURPOSE     : This is the assignment for the class CS6364
#Design an intelligent agent to draw a continuous line  covering all the links from node A to node A and node A to anywhere.
#DESCRPTION   :This module mainly find the path using Depth first search. The function takes input as two graphs staring node and no of edges
#it find the path starting from node A to node A and node A to anywhere.



# This function gets the graph and inserts children nodes in the stack and removes the last element from the stack and checks if there is an
#edge between two edges. if edge exists,then path list is appended. This process is repeated until all the  links of graph are covered only once.
__author__ = 'pujitha'
import random
def neihgb(graph, start):

 odd = [ x for x in graph.keys() if len(graph[x])&1 ]
 stack=[start];
 path=[]
 nodes_exp=0
 while stack:

    v = stack[-1]
    if graph[v]:
      nodes_exp=nodes_exp+1
      u = graph[v][0]
      stack.append(u)
      # deleting edge u-v
      del graph[u][graph[u].index(v) ]
      del graph[v][0]
    else:
       path.append(stack.pop())
 path.append(nodes_exp)
 return path



#it calls def BFS and stores the values in a list and prints the list.
def main():

  graph1={  'A':['B','C','D'],
 	        'B':['A','D','C'],
 	        'C':['A','B','D','E'],
            'D':['A','B','C','E'],
            'E':['C','D']}
  print("--------------------------------------------------------------------------------------------------------------")
  print ("Solution for Graph1 in DFS")
  list1=list(neihgb(graph,'A'))
 # print list1
 # m=len(list1)-1
  nodes=list1.pop()
  print nodes
  list2=list1[::-1]
  if (list2[-1]== 'A'):
     print(list2[-1])
     print("path exist from source node 'A' to 'A' only"+" and Path is:")
     print list2
     print("Solution:")
     list3=[]
     list3.extend([list2[0],list2[1],nodes,nodes,nodes,list2[-1]])
     print(list3)
  else:
     print("Path from source node to other nodes exist"+ " and Path is:")
     print list2
     print("Solution:")
     list3=[]
     list3.extend([list2[0],list2[1],nodes,nodes,nodes,list2[-1]])
     print(list3)
     print("no path exist from source node 'A' to 'A' ")
     print("No Solution")



  print("--------------------------------------------------------------------------------------------------------------")
  print ("Solution for Graph2 in DFS")
  graph2={'A':['B','C','D','F'],
          'B':['A','C','D','F'],
          'C':['A','B','D','E'],
          'D':['A','B','C','E'],
          'E':['C','D'],
          'F':['A','B'] }
  list1 = list(neihgb(graph2,'A'))
  nodes=list1.pop()
  list2=list1[::-1]


  if (list2[-1]== 'A'):
     print("path exist from source node 'A' to 'A'"+"and Path is:")
     print list2
     print("Solution:")
     list3=[]
     list3.extend([list2[0],list2[1],nodes,nodes,nodes,list2[-1]])
     print(list3)
     print("no path exist from source node 'A' to other nodes")
     print("No solution")
  else:
     print("Path from source node to other nodes exit")
     print list2
     print("Solution:")
     list3=[]
     list3.extend([list2[0],list2[1],nodes,nodes,nodes,list2[-1]])
     print(list3)
     print("no path exist from source node 'A' to 'A'")
     print("No Solution")
  raw_input()
if __name__ == '__main__':

  graph= {  'A':['B','C','D'],
 	        'B':['A','D','C'],
 	        'C':['A','B','D','E'],
            'D':['A','B','C','E'],
            'E':['C','D']
             }

  main()