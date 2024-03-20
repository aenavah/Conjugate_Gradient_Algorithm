import numpy as np
import matplotlib.pyplot as plt

import ConjugateGradient_functions
#-----------------------------------
'''bullet 1 b1'''
GaussJacobi = ConjugateGradient_functions.GaussJacobi
#-----------------------------------
'''bullet 2 b1'''
GaussSeidel = ConjugateGradient_functions.GaussSeidel
ConjugateGradient = ConjugateGradient_functions.ConjugateGradient
ConjugateGradientpc = ConjugateGradient_functions.ConjugateGradientpc
norm = ConjugateGradient_functions.norm

if __name__ == "__main__":
  #-----------------------------------
  '''bullet 3 b1'''
  m = int(input("Input m for matrix size mxm: "))
  D = int(input("Input value of d_{ii}: "))
  A = np.ones((m, m))
  np.fill_diagonal(A, D)
  A = np.copy(A)
  '''bullet 4 b1'''
  b = []
  for i in range(0, m):
    b.append(i+1)
  A = A.copy()
  b = b.copy()

  #-----------------------------------
  '''bullet 5 b1'''
  which = int(input("To solve Ax = b enter (0) Gauss-Jacobi or (1) Gauss-Seidel or (2) for Conjugate-Gradient: "))

  #-----------------------------------
  '''bullet 6 b1'''
  '''Computes both gauss algorithm to produce plot for given D'''
  sol0, iterations0, works0, errors_df0 = GaussJacobi(A, b, D)
  sol1, iterations1, works1, errors_df1 = GaussSeidel(A, b, D)
  '''b2 conjugate gradient algorithm'''
  sol2, iterations2, works2, symm = ConjugateGradient(A, b)
  
  #-----------------------------------
  '''bullet 8 b2'''
  print("Number of Iterations for D = " + str(D) + ":")
  print("For Gauss-Jacobi: " + str(iterations0))
  print("For Gauss-Seidel: " + str(iterations1))
  print("For Conjugate Gradient: " + str(iterations2))

  #-----------------------------------
  '''Prints solution corresponding to user choice of algorithm'''
  if which == 0:
    print("Using Gauss-Jacobi Method...")
    if works0 == 1:
      print("Yippee!")
      print(sol0)
    else:
      print("Booooo!")
  if which == 1:
    print("Using Gauss-Seidel Method...")
    if works1 == 1:
      print("Yippee!")
      print(sol1)
    else:
      print("Booooo!")
  if which == 2:
    print("Using Conjugate-Gradient Method...")
    if works2 == 1:
      print("Yippee!")
      print(sol2.reshape(1, -1))
    else:
      print("Booooo!")

  #-----------------------------------
  '''bullet 8 b1'''
  '''if either iterations work for a given D, plot either or both'''
  if works0 == 1 or works1 == 1:
      ax = None
      if works0 == 1:
        ax = errors_df0.plot(x=0, y=1, kind="line", marker='o', color="pink", label="Gauss-Jacobi")
      if works1 == 1:
        ax = errors_df1.plot(x=0, y=1, kind="line", marker='o', color="lightblue", label="Gauss-Seidel", ax=ax)
      ax.set_xlabel("Iteration number")
      ax.set_ylabel("Error")
      ax.set_title("Error vs Iteration Number for D = " + str(D))
      plt.savefig("errors_D=" + str(D) + ".jpg")

  #-----------------------------------
  '''bullet 9 b1'''
  # A20 = np.ones((10, 10))
  # D20 = [1,2,3,4,5,6,7,8,9,10]
  # b20 = D20.copy()
  # np.fill_diagonal(A20, D20)
  # print(A20)
  # sol20, tmp, tmp, tmp = GaussJacobi(A20, b20, "finalpart")
  # A21 = np.ones((10, 10))
  # D21 = [1,2,3,4,5,6,7,8,9,10]
  # b21 = D21.copy()
  # np.fill_diagonal(A21, D21)
  # print(A21)
  # sol21, tmp, tmp, tmp = GaussSeidel(A21, b21, "finalpart")
  # print(sol20)
  # print(sol21)
  
  #-----------------------------------
  '''bullet 11 b2 without preconditioning'''  
  # A10 = np.ones((10, 10))
  # D10 = list(range(1,11))
  # b10 = np.copy(D10)
  # np.fill_diagonal(A10, D10)
  # sol10, count10, works10, symm10 = ConjugateGradientpc(A10, b10)
  # print("Count for 10x10: " + str(count10))

  #-----------------------------------
  '''bullet 11 b2 with preconditioning'''  
  # A100 = np.ones((100, 100))
  # D100 = list(range(1,101))
  # b100 = np.copy(D100)
  # np.fill_diagonal(A100, D100)
  # sol100, count100, works100, symm100 = ConjugateGradientpc(A100, b100)
  # print("Count for 100x100: " + str(count100))
  
  