graph = {"Arad": {"Timisoara", "Sibiu", "Zerind"},
         "Zerind": {"Arad", "Oradea"},
         "Oradea": {"Zerind", "Sibiu"},
         "Timisoara": {"Arad", "Lugoj"},
         "Lugoj": {"Timisoara", "Mehadia"},
         "Mehadia": {"Lugoj", "Dobreta"},
         "Dobreta": {"Mehadia", "Craiova"},
         "Craiova": {"Dobreta", "RimnicuVilcea", "Pitesi"},
         "RimnicuVilcea": {"Craiova", "Pitesi", "Sibiu"},
         "Sibiu": {"Arad", "Oradea", "RimnicuVilcea", "Fagaras"},
         "Fagaras": {"Sibiu", "Bucharest"},
         "Pitesi": {"Bucharest", "RimnicuVilcea", "Craiova"},
         "Bucharest": {"Pitesi", "Fagaras", "Giurgiu", "Urziceni"},
         "Giurgiu": {"Bucharest"},
         "Urziceni": {"Bucharest", "Hirsova", "Vaslui"},
         "Hirsova": {"Urziceni", "Eforie"},
         "Eforie": {"Hirsova"},
         "Vaslui": {"Urziceni", "Iasi"},
         "Iasi": {"Vaslui", "Neamt"},
         "Neamt": {"Iasi"}}


print(graph)


