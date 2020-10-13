import this

print("hello world")

def gcd(a, b):
  if b > 0: return gcd(b, a % b)
  else: return a

print("test")

N = 1000
A = []
for i in range(0, N):
  A.append(i)

ans = 0
for i in A:
  for j in A:
    ans += gcd(i, j)
print(ans)
