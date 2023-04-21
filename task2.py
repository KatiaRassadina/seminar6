lambda_ = 0.95
t_lambda_ = 1.96
import numpy as np
import math
X = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
S = np.std(X)
M = np.mean(X)
n = len(X)

delta_ = t_lambda_ * S / math.sqrt(n)

a, b = M - delta_, M + delta_

print(f'Доверительный интервал: [{a}, {b}]')