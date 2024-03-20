import numpy as np
import pandas as pd

def norm(matrix):
  f = np.sqrt(np.sum(matrix**2))
  return f


def GaussJacobi(A, b, D, tol = 10**(-5), N = 10000):
  '''Takes in required inputs A and b, and optional inputs N and tol'''
  '''solves Ax=b with initial guess x0, and max number of iterations N'''
  '''Output: solution, iterations to converge, whether it was successful, and [iteration,errors] in a dataframe if successful'''
  errors = []
  n = len(b)
  x0 = np.zeros(n)
  x = np.copy(x0)
  for k in range(0, N):
    for i in range(n):
      summ = 0.0
      for j in range(0, n):
        if j != i:
          summ += A[i,j]*x0[j]
      if abs(A[i,i]) <= 10**-16:
        return x, k, 0, 0
      x[i] = (-summ + b[i])/A[i, i]
    error = (norm(x- x0))/(norm(x))
    if error < tol:
      df = pd.DataFrame(errors)
      df.to_csv("Errors_GaussJacobi_D=" + str(D) + ".csv")
      return x, k, 1, df
    errors.append([k, error])
    x0 = np.copy(x)
  return x, "didnt converge", 0, 0

def GaussSeidel(A, b, D, tol = 10**(-5), N = 10000):
  '''Takes in required inputs A and b, and optional inputs N and tol'''
  '''solves Ax=b with initial guess x0, and max number of iterations N'''
  '''Output: solution, iterations to converge, whether it was successful, and [iteration,errors] in a dataframe if successful'''
  errors = []
  n = len(b)
  x0 = np.zeros(n)
  x = np.copy(x0)
  for k in range(0, N):
    for i in range(0, n):
      #summation1
      sum1 = 0.0
      for j in range(0, i): #range already doesnt do i, so this goes to i-1
        sum1 += A[i, j] * x[j]
      #summation2
      sum2 = 0.0
      for j in range(i + 1, n):
        sum2 += A[i, j] * x0[j]
      if abs(A[i,i]) <= 10**-16:
        return x, k, 0, 0
      x[i] = (-sum1 - sum2 + b[i])/A[i,i]
    error = (norm(x- x0))/(norm(x))
    if error < tol:
      df = pd.DataFrame(errors)
      df.to_csv("Errors_GaussSeidel_D=" + str(D) + ".csv")
      return x, k+1, 1, df
    errors.append([k, error])
    x0 = np.copy(x)
  return x, "didnt converge", 0, 0

def ConjugateGradient(A, b, tol = 10**(-5), x0 = "", maxiter = 1000):
  '''
  Without conditioning, With conditioning, only requires inputs A and b, 
    optional tolerance, choice of x_0 and max iterations
  Output: solution, iterations to converge, whether it was successful, and whether it's symmetric
  '''
  if np.array_equal(A, A.T):
    symm = 1
  else:
    symm = 0
  A = A.copy()
  b = b.copy()
  n, m = np.shape(A)
  if x0 == "":
    x0 = np.zeros(m)
  x = x0
  r = b - A@x
  p = r
  E = norm(r)**2
  count = 0
  while np.sqrt(E) > tol:
    count += 1
    y = A @ p
    alpha = E/(np.transpose(p) @ y)
    x = x + (alpha * p)
    r = r - (alpha * y)
    E_new = (norm(r))**2
    beta = E_new/E
    p = r + beta * p
    E = E_new
  works = 1 
  return x, count, works, symm

def ConjugateGradientpc(A, b, tol = 10**(-5), x0 = "", maxiter = 1000):
  '''
  With conditioning, only requires inputs A and b, 
    optional tolerance, choice of x_0 and max iterations
  Output: solution, iterations to converge, whether it was successful, and whether it's symmetric
  '''
  if np.array_equal(A, A.T):
    symm = 1
  else:
    symm = 0
  A = A.copy()
  b = b.copy()
  n, m = np.shape(A)
  if x0 == "":
    x0 = np.zeros(m)
  M_inv = get_M_inv(A)
  M_inv.copy()
  #-----
  x = x0
  r = b - A@x
  z = M_inv @ r
  p = z
  E = r.T @ z
  count = 0
  while np.sqrt(E) > tol:
    count += 1
    y = A @ p
    alpha = E/(p.T @ y)
    x = x + (alpha * p)
    r = r - (alpha * y)
    z = M_inv @ r
    E_new = r.T @ z
    beta = E_new/E
    p = z + beta * p
    E = E_new
  works = 1 
  return x, count, works, symm

def get_M_inv(A):
  '''
  Compute M^{-1} for use with preconditioning
  input: A to find corresponding M^{-1}, and returns M^{-1}
  '''
  m, n = np.shape(A)
  M_inv = np.zeros((m, m))
  diag = np.diagonal(A)
  diag_inv = []
  for a in diag:
    diag_inv.append(1/a)
  np.array(diag_inv)
  np.fill_diagonal(M_inv, diag_inv)
  return M_inv


#https://www.youtube.com/watch?v=z9glsQDkkWU&t=782s
#psuedocode: https://www3.nd.edu/~zxu2/acms40390F12/Lec-7.3.pdf