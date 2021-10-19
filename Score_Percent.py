from sympy import exp, sqrt, pi, Integral, Symbol

m = float(input('점수를 입력하십시오: '))
mu = float(input('평균 점수를 입력하십시오: '))
sigma = float(input('표준편차를 입력하십시오: '))

x = Symbol('x')
f = exp(-(x-mu)**2/(2*sigma**2))/(sigma*sqrt(2*pi))

y = Integral(f, (x, mu, m)).doit().evalf()
y += 0.5
y *= 100
y = round(y, 2)
print('\n','백분율: ',y, '%')