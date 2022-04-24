import numpy as np

def d(S, T):
    return 1

def main():
    U = np.array([0, 1, 2])
    L = np.array([0, 1, 2, 3, 4])
    E = np.array([[1, 1, 1, 1, 0],[1, 1, 1, 1, 1], [0, 0, 0, 1, 1]])
    ec = np.array([])

    F = np.copy(E)
    R = np.copy(U)

    for k in range(10):
        S = np.array([])
        T = np.copy(L)

        S_max = np.copy(S)
        T_max = np.copy(T)


        ##Rの頂点セットからRに連結しているエッジ数が多い順にソートする

        for u in R:
            S = np.append(S, u)
            T = np.append(T, u)

            if(d(S, T) > d(S_max, T_max)):
                Smax = np.copy(S)
                Tmax = np.copy(T)
            
            if(d(S_max, T_max) >= 0):
                F = 1
                ec = ec.append(1)
                R = np.copy(U)
            else:
                R = np.delete(R, 0)

            if(R.size() == 0):
                break
    
    print(ec)

            






if __name__ == "__main__":
    main()