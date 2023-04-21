lambda_ = 0.95
t_lambda_ = 1.96
import math
S = 16
M = 80
n = 256

delta_ = t_lambda_ * S / math.sqrt(n)

a, b = M - delta_, M + delta_

print(f'Доверительный интервал: [{a}, {b}]')