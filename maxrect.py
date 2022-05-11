import numpy as np


class maxrect:
    U = np.array([0, 1, 2], dtype=int)
    L = np.array([0, 1, 2, 3, 4], dtype=int)
    E = np.array([[1, 1, 1, 0, 0],[1, 1, 1, 1, 1], [0, 0, 1, 1, 1]], dtype=int)
    ec = np.empty(0,dtype=int)

    def __init__(self):
        pass

    def ready(self):
        F = np.copy(self.E)
        R = np.copy(self.U)
        for k in range(10):
            S = np.array([], dtype=int)
            T = np.copy(self.L)

            S_max = np.copy(S)
            T_max = np.copy(T)


            ##Rの頂点セットからRに連結しているエッジ数が多い順にソートする
            R = sorted(R, reverse=True,key=lambda x:np.sum(F, axis=1)[x])
            ##print(R)

            for u in R:
                S = np.append(S, u)
                T_copy = np.copy(T);
                T = np.array([], dtype=int)

                cnt = 0
                for tail in self.E[u]:
                    if(tail == 1 and (cnt in T_copy)):
                        T = np.append(T, cnt)
                    cnt += 1

                print(k+1)
                print(self.E[u])
                print(S)
                print(T)
                print(self.d(S, T, F)) 
                print("###")

                if(self.d(S, T, F) > self.d(S_max, T_max, F)):
                    S_max = np.copy(S)
                    T_max = np.copy(T)
            
            if(self.d(S_max, T_max, F) >= 0):
                #Fから完全二部グラフS_max × T_maxのエッジを削除
                for i in S_max:
                    for j in T_max:
                        F[i][j] = 0
                self.ec = np.append(self.ec, np.array([[S_max], [T_max]]))
                R = np.copy(self.U)
            else:
                R = np.delete(R, 0)
            
            if(R.size == 0):
                break
    
  
        self.ec = np.reshape(self.ec, (2, 2))  
        #print(ec)


    def printResult(self):
        print(self.ec)

    def d(self,S, T, F):
        res = 0
        inc = 0
        for i in S:
            for j in T:
                if(F[i][j] == 1):
                    inc += 1
        res = inc - S.size - T.size
        ##print("!!!!")
        ##print(inc)
        ##print(S.size + T.size)
        ##print("!!!!")
        return res


def main():
    m1 = maxrect()
    m1.ready()
    m1.printResult()
   

            






if __name__ == "__main__":
    main()