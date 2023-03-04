from mpi4py import MPI
import numpy as np
N=1000
A,B=None,None
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
#Get matrices from node 0
if rank==0:
    A=np.ones((N,N))
B=np.ones((N,N))
#Initialize an empty array to receive data
if N%size==0:
    partial=np.empty((int(N/size),N),dtype='d')
else:
    if rank<size-1:
        partial=np.empty((int(N/size),N),dtype='d')
    else:
        partial=np.empty((int(N/size)+(N%size),N),dtype='d')
#Scatter A into different cores
comm.Scatter(A,partial,root=0)
#Prepare result matrix to gather the partial results
result=None
if rank==0:
    result=np.empty((N,N),dtype='d')
#Gather matrix multiplication result from different cores
comm.Gather(np.matmul(partial,B),result,root=0)
#Print the result
if rank==0:
    print("Matrix multiplication result = ",result)
    print("Does the result match the expectation? ",sum(sum(result==N*np.ones((N,N))))==N*N)
# mpirun -n 4 python Mat_X_MPI.ipynb