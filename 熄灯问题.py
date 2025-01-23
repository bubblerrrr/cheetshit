#当第一行按钮状态确定后，其余行数的按钮状态也将确定。
#因此，需要列举出第一行所有的按钮状态的可能性并推导出其他行的按钮状态可能性。
import copy
X=[[0,0,0,0,0,0,0,0,]]#在灯的矩阵周围加上0，用来避免越界
Y=[[0,0,0,0,0,0,0,0,]]#用于储存按钮按下的状态，0表示不按，1表示按了
#可以用abs（i-1）来操作0和1之间的反转
for _ in range(5):
    current=list(map(int,input().split()))
    X.append([0]+current+[0])
    Y.append([0 for _ in range(8)])
X.append([0,0,0,0,0,0,0,0])
#给最后一行加上保护层
#穷举第一行的每一种状态
for a in range(2):
    Y[1][1]=a
    for b in range(2):
        Y[1][2]=b
        for c in range(2):
            Y[1][3]=c
            for d in range(2):
                Y[1][4]=d
                for e in range(2):
                    Y[1][5]=e
                    for f in range(2):
                        Y[1][6]=f
                        #复制灯和按钮的状态，防止影响其他情况的修改
                        A=copy.deepcopy(X)
                        B=copy.deepcopy(Y)
                        #模拟第一行的操作
                        for i in range(1,7):
                            if B[1][i]==1:
                                A[1][i]=abs(A[1][i]-1)
                                A[1][i-1]=abs(A[1][i-1]-1)
                                A[1][i+1]=abs(A[1][i+1]-1)
                                A[2][i]=abs(A[2][i]-1)
                        #模拟第二到五行的操作
                        for i in range(2,6):
                            for j in range(1,7):
                                if A[i-1][j]==1:
                                    B[i][j]=abs(B[i][j]-1)#如果上方灯是亮着的，为了让它熄灭，则改变下方按钮状态。
                                    A[i][j]=abs(A[i][j]-1)
                                    A[i-1][j]=abs(A[i-1][j]-1)
                                    A[i][j-1]=abs(A[i][j-1]-1)
                                    A[i][j+1]=abs(A[i][j+1]-1)
                                    A[i+1][j]=abs(A[i+1][j]-1)
                        if A[5][1]==A[5][2]==A[5][3]==A[5][4]==A[5][5]==A[5][6]==0:
                            for i in range(1,6):
                                print(" ".join(str(B[i][j])for j in range(1,7)))