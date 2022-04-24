import numpy as np

def d(S, T, F):
    res = 0
    for i in S:
        for j in T:
            print("####")
            print(i)
            print(j)
            print("$$$$")
            if(F[i][j] == 1):
                res += 1
    res -= S.size + T.size

    return res


def main():
    U = np.array([0, 1, 2], dtype=int)
    L = np.array([0, 1, 2, 3, 4], dtype=int)
    E = np.array([[1, 1, 1, 1, 0],[1, 1, 1, 1, 1], [0, 0, 0, 1, 1]], dtype=int)
    ec = np.array([],dtype=int)

    F = np.copy(E)
    R = np.copy(U)

 

    for k in range(10):
        S = np.array([], dtype=int)
        T = np.copy(L)

        S_max = np.copy(S)
        T_max = np.copy(T)


        ##Rの頂点セットからRに連結しているエッジ数が多い順にソートする
        R = sorted(R, reverse=True,key=lambda x:np.sum(F, axis=1)[x])


        for u in R:
            S = np.append(S, u)
            T = np.array([], dtype=int)
            cnt = 0
            for tail in E[u]:
                if(tail == 1):
                    T = np.append(T, L[cnt])
                    cnt += 1

            if(d(S, T, F) > d(S_max, T_max, F)):
                S_max = np.copy(S)
                T_max = np.copy(T)
            
            if(d(S_max, T_max, F) >= 0):

                #Fから完全二部グラフS_max × T_maxのエッジを削除
                for i in S_max:
                    for j in T_max:
                        F[i][j] = 0

                ec = np.append(ec, [S_max, T_max])
                R = np.copy(U)
            else:
                R = np.delete(R, 0)

            if(R.size == 0):
                break
    
    print(ec)

            






if __name__ == "__main__":
    main()