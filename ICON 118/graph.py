class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    def printGraph(self):
        nodesNameList = list(self.adjac_lis.keys())
        nodesNameList.sort()
        nodeSeparatorString = '+--------------------------------------------------+'
        for nodeName in nodesNameList:
            print('Node: ', nodeName, end=' ')
            count = 1
            print("->", end=" ")
            for adj in self.adjac_lis[nodeName]:
                if (count > 1):
                    print(adj, ' ', end=" ")
                else:
                    print(adj, ' ', end=" ")
                count += 1
            print()

    def h_osp1(self, n):
        H = {
            'A': abs(5 - 15) + abs(15 - 22),
            'B': abs(5 - 20) + abs(15 - 22),
            'C': abs(5 - 20) + abs(15 - 16),
            'D': abs(5 - 15) + abs(15 - 15),
            'E': abs(5 - 20) + abs(15 - 12),
            'F': abs(5 - 15) + abs(15 - 9),
            'G': abs(5 - 16) + abs(15 - 4),
            'H': abs(5 - 20) + abs(15 - 5),
            'I': abs(5 - 26) + abs(15 - 16),
            'J': abs(5 - 27) + abs(15 - 8),
            'K': abs(5 - 26) + abs(15 - 25),
            'L': abs(5 - 29) + abs(15 - 23),
            'M': abs(5 - 35) + abs(15 - 26),
            'N': abs(5 - 33) + abs(15 - 23),
            'O': abs(5 - 29) + abs(15 - 12),
            'P': abs(5 - 36) + abs(15 - 15),
            'Q': abs(5 - 40) + abs(15 - 14),
            'R': abs(5 - 35) + abs(15 - 10),
            'S': abs(5 - 36) + abs(15 - 5),
            'T': abs(5 - 42) + abs(15 - 8),
            'U': abs(5 - 40) + abs(15 - 3),
            'V': abs(5 - 3) + abs(15 - 10),
            'W': abs(5 - 2) + abs(15 - 16),
            'X': abs(5 - 6) + abs(15 - 19),
            'Y': abs(5 - 7) + abs(15 - 13),
            'Z': abs(5 - 6) + abs(15 - 6),
            'O1': 0,
            'O2': abs(5 - 17) + abs(15 - 17),
            'O3': abs(5 - 18) + abs(15 - 6),
            'O4': abs(5 - 32) + abs(15 - 24),
            'O5': abs(5 - 39) + abs(15 - 9),
        }

        return H[n]

    def h_osp2(self, n):
        H = {
            'A': abs(17 - 15) + abs(17 - 22),
            'B': abs(17 - 20) + abs(17 - 22),
            'C': abs(17 - 20) + abs(17 - 16),
            'D': abs(17 - 15) + abs(17 - 15),
            'E': abs(17 - 20) + abs(17 - 12),
            'F': abs(17 - 15) + abs(17 - 9),
            'G': abs(17 - 16) + abs(17 - 4),
            'H': abs(17 - 20) + abs(17 - 5),
            'I': abs(17 - 26) + abs(17 - 16),
            'J': abs(17 - 27) + abs(17 - 8),
            'K': abs(17 - 26) + abs(17 - 25),
            'L': abs(17 - 29) + abs(17 - 23),
            'M': abs(17 - 35) + abs(17 - 26),
            'N': abs(17 - 33) + abs(17 - 23),
            'O': abs(17 - 29) + abs(17 - 12),
            'P': abs(17 - 36) + abs(17 - 15),
            'Q': abs(17 - 40) + abs(17 - 14),
            'R': abs(17 - 35) + abs(17 - 10),
            'S': abs(17 - 36) + abs(17 - 5),
            'T': abs(17 - 42) + abs(17 - 8),
            'U': abs(17 - 40) + abs(17 - 3),
            'V': abs(17 - 3) + abs(17 - 10),
            'W': abs(17 - 2) + abs(17 - 16),
            'X': abs(17 - 6) + abs(17 - 19),
            'Y': abs(17 - 7) + abs(17 - 13),
            'Z': abs(17 - 6) + abs(17 - 6),
            'O1': abs(17 - 5) + abs(17 - 15),
            'O2': 0,
            'O3': abs(17 - 18) + abs(17 - 6),
            'O4': abs(17 - 32) + abs(17 - 24),
            'O5': abs(17 - 39) + abs(17 - 9),
        }

        return H[n]

    def h_osp3(self, n):
        H = {
            'A': abs(18 - 15) + abs(6 - 22),
            'B': abs(18 - 20) + abs(6 - 22),
            'C': abs(18 - 20) + abs(6 - 16),
            'D': abs(18 - 15) + abs(6 - 15),
            'E': abs(18 - 20) + abs(6 - 12),
            'F': abs(18 - 15) + abs(6 - 9),
            'G': abs(18 - 16) + abs(6 - 4),
            'H': abs(18 - 20) + abs(6 - 5),
            'I': abs(18 - 26) + abs(6 - 16),
            'J': abs(18 - 27) + abs(6 - 8),
            'K': abs(18 - 26) + abs(6 - 25),
            'L': abs(18 - 29) + abs(6 - 23),
            'M': abs(18 - 35) + abs(6 - 26),
            'N': abs(18 - 33) + abs(6 - 23),
            'O': abs(18 - 29) + abs(6 - 12),
            'P': abs(18 - 36) + abs(6 - 15),
            'Q': abs(18 - 40) + abs(6 - 14),
            'R': abs(18 - 35) + abs(6 - 10),
            'S': abs(18 - 36) + abs(6 - 5),
            'T': abs(18 - 42) + abs(6 - 8),
            'U': abs(18 - 40) + abs(6 - 3),
            'V': abs(18 - 3) + abs(6 - 10),
            'W': abs(18 - 2) + abs(6 - 16),
            'X': abs(18 - 6) + abs(6 - 19),
            'Y': abs(18 - 7) + abs(6 - 13),
            'Z': abs(18 - 6) + abs(6 - 6),
            'O1': abs(18 - 5) + abs(6 - 15),
            'O2': abs(18 - 17) + abs(6 - 17),
            'O3': 0,
            'O4': abs(18 - 32) + abs(6 - 24),
            'O5': abs(18 - 39) + abs(6 - 9),
        }

        return H[n]
    
    def h_osp4(self, n):
        H = {
            'A': abs(32 - 15) + abs(24 - 22),
            'B': abs(32 - 20) + abs(24 - 22),
            'C': abs(32 - 20) + abs(24 - 16),
            'D': abs(32 - 15) + abs(24 - 15),
            'E': abs(32 - 20) + abs(24 - 12),
            'F': abs(32 - 15) + abs(24 - 9),
            'G': abs(32 - 16) + abs(24 - 4),
            'H': abs(32 - 20) + abs(24 - 5),
            'I': abs(32 - 26) + abs(24 - 16),
            'J': abs(32 - 27) + abs(24 - 8),
            'K': abs(32 - 26) + abs(24 - 25),
            'L': abs(32 - 29) + abs(24 - 23),
            'M': abs(32 - 35) + abs(24 - 26),
            'N': abs(32 - 33) + abs(24 - 23),
            'O': abs(32 - 29) + abs(24 - 12),
            'P': abs(32 - 36) + abs(24 - 15),
            'Q': abs(32 - 40) + abs(24 - 14),
            'R': abs(32 - 35) + abs(24 - 10),
            'S': abs(32 - 36) + abs(24 - 5),
            'T': abs(32 - 42) + abs(24 - 8),
            'U': abs(32 - 40) + abs(24 - 3),
            'V': abs(32 - 3) + abs(24 - 10),
            'W': abs(32 - 2) + abs(24 - 16),
            'X': abs(32 - 6) + abs(24 - 19),
            'Y': abs(32 - 7) + abs(24 - 13),
            'Z': abs(32 - 6) + abs(24 - 6),
            'O1': abs(32 - 5) + abs(24 - 15),
            'O2': abs(32 - 17) + abs(24 - 17),
            'O3': abs(32 - 18) + abs(24 - 6),
            'O4': 0,
            'O5': abs(32 - 39) + abs(24 - 9),
        }

        return H[n]
    
    def h_osp5(self, n):
        H = {
            'A': abs(39 - 15) + abs(9 - 22),
            'B': abs(39 - 20) + abs(9 - 22),
            'C': abs(39 - 20) + abs(9 - 16),
            'D': abs(39 - 15) + abs(9 - 15),
            'E': abs(39 - 20) + abs(9 - 12),
            'F': abs(39 - 15) + abs(9 - 9),
            'G': abs(39 - 16) + abs(9 - 4),
            'H': abs(39 - 20) + abs(9 - 5),
            'I': abs(39 - 26) + abs(9 - 16),
            'J': abs(39 - 27) + abs(9 - 8),
            'K': abs(39 - 26) + abs(9 - 25),
            'L': abs(39 - 29) + abs(9 - 23),
            'M': abs(39 - 35) + abs(9 - 26),
            'N': abs(39 - 33) + abs(9 - 23),
            'O': abs(39 - 29) + abs(9 - 12),
            'P': abs(39 - 36) + abs(9 - 15),
            'Q': abs(39 - 40) + abs(9 - 14),
            'R': abs(39 - 35) + abs(9 - 10),
            'S': abs(39 - 36) + abs(9 - 5),
            'T': abs(39 - 42) + abs(9 - 8),
            'U': abs(39 - 40) + abs(9 - 3),
            'V': abs(39 - 3) + abs(9 - 10),
            'W': abs(39 - 2) + abs(9 - 16),
            'X': abs(39 - 6) + abs(9 - 19),
            'Y': abs(39 - 7) + abs(9 - 13),
            'Z': abs(39 - 6) + abs(9 - 6),
            'O1': abs(39 - 5) + abs(9 - 15),
            'O2': abs(39 - 17) + abs(9 - 17),
            'O3': abs(39 - 18) + abs(9 - 6),
            'O4': abs(39 - 32) + abs(9 - 24),
            'O5': 0,
        }

        return H[n]
    
    def a_star_algorithm(self, start, stop):

        open_lst = set([start])
        closed_lst = set([])

        poo = {}
        poo[start] = 0

        par = {}
        par[start] = start

        while len(open_lst) > 0:
            n = None

            for v in open_lst:
                if(stop == 'O1'):
                    if n == None or poo[v] + self.h_osp1(v) < poo[n] + self.h_osp1(n):
                        n = v;
                elif(stop == 'O2'):
                    if n == None or poo[v] + self.h_osp2(v) < poo[n] + self.h_osp2(n):
                        n = v;
                elif(stop == 'O3'):
                    if n == None or poo[v] + self.h_osp3(v) < poo[n] + self.h_osp3(n):
                        n = v;
                elif(stop == 'O4'):
                    if n == None or poo[v] + self.h_osp4(v) < poo[n] + self.h_osp4(n):
                        n = v;
                elif(stop == 'O5'):
                    if n == None or poo[v] + self.h_osp2(v) < poo[n] + self.h_osp2(n):
                        n = v;
                else:
                    break
                    return reconst_path.clear()
            if n == None:
                #print('Path does not exist!')
                return None


            if n == stop:
                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(start)

                reconst_path.reverse()

                #print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):

                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight


                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)


            open_lst.remove(n)
            closed_lst.add(n)

        #print('Path does not exist!')
        return reconst_path

    def timeForPath(self, nodesPath: list):
        time = 0
        count = 0

        while (count < len(nodesPath)):
            if (count + 1 < len(nodesPath)):
                startNodeName = nodesPath[count]
                endNodeName = nodesPath[count + 1]

                for adjac_node in self.get_neighbors(startNodeName):
                    if (adjac_node[0] == endNodeName):
                        time += adjac_node[1]

            count += 1

        return time