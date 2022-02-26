import queue
q=queue.Queue()
graph = {
"Arad": {"Timisoara": 118, "Sibiu": 140,"Zerind": 75},
"Zerind": {"Arad": 75, "Oradea": 71},
"Oradea": {"Zerind": 71, "Sibiu": 151},
"Timisoara": {"Arad": 118, "Lugoj": 111},
"Lugoj": {"Timisoara": 111, "Mehadia":70},
"Mehadia": {"Lugoj": 70, "Dobreta": 75},
"Dobreta": {"Mehadia":75, "Craiova":120},
"Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
"RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu":80},
"Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99},
"Fagaras": {"Sibiu": 99, "Bucharest":211},
"Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
"Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
"Giurgiu": {"Bucharest": 90},
"Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
"Hirsova": {"Urziceni": 98, "Eforie": 86},
"Eforie": {"Hirsova": 86},
"Vaslui": {"Urziceni": 142, "Iasi": 92},
"Iasi": {"Vaslui": 92, "Neamt": 87},
"Neamt": {"Iasi": 87}
}
goal="Bucharest"
flag=0
visited= {"Arad": 1,"Zerind": 1,"Oradea": 0,"Timisoara": 1,"Lugoj": 0,
"Mehadia": 0, "Dobreta": 0, "Craiova":0,"RimnicuVilcea": 0,"Sibiu": 1,
"Fagaras": 0,"Pitesi":0, "Bucharest":0,"Giurgiu":0,"Urziceni":0,"Hirsova": 0,
"Eforie": 0, "Vaslui": 0,"Iasi": 0,"Neamt": 0}
0-unvisited 1-visited/in frontier; 2:expanded/in explored set

parent= {"Arad": None,"Zerind": "Arad","Oradea": None,"Timisoara": "Arad",
"Lugoj":None,"Mehadia":None, "Dobreta":None, "Craiova":None,
"RimnicuVilcea": None,"Sibiu":"Arad","Fagaras":None,"Pitesi":None,
"Bucharest":None,"Giurgiu":None,"Urziceni":None,"Hirsova":None,
"Eforie":None,"Vaslui":None,"Iasi":None,"Neamt":None}
Queue: Arad, Timisoara, Sibiu,Zerind
q.put("Arad");
while( queue not empty)
x=dequeue
visited[x]=2 //making it expanded
list=Graph[x]
for loop on list
if visited[child] !=1 && visited[child] !=2 //Child state not in frontier and explored set
parent[child]=x
if child==goal //
else
put child state in queue
visited[child]=1
