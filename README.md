## ITCS- 6114/8114: Algorithm and Data Structure Project 1 - Shortest path in a Network
##### By Shreya Sekhar - 801254672
Consider a data communication network that must route data packets. Such a network consists of routers connected by physical cables or links. A router can act as a source, a destination, or a forwarder of data packets. We can model a network as a graph with each router corresponding to a vertex and the link or physical connection between two routers corresponding to a pair of directed edges between the vertices.
It uses Dijkstra's shortest path algorithm to route packets across a network. The time it takes to transmit data, the link's reliability, transmission cost, and available bandwidth are all factors that can be used to determine a link's weight. Typically, each router has access to a comprehensive representation of the network graph as well as accompanying data.
Programming Language : Python
Data Structures used: Heap, priority queue,Linked list. Implementation:
The implementation code is included in a single file called Graph.py, which contains all of the project's duties. The algorithm utilized is Dijkstra's Algorithm, which is used to discover the shortest path between nodes in a graph. The reachable vertices job is added to the aforementioned task by utilizing a recursive approach to determine the vertices related to each vertex. The task of reachable takes O(n logn) time to complete, where n is the number of vertices.
What works and Fails?
1. Input file is expected to be in precise format for correct execution of the program
2. Query file should have "quit" as the last query, else the program will run indefinitely.
3. Not tested on Windows OS. Works well on Mac OS.
