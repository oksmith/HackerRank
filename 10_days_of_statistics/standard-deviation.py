N = int(input())
X = list(map(int,input().split(" ")))

mu = float(sum(X)/N)
diff = [x-mu for x in X]
sumsq = sum([d*d for d,d in zip(diff,diff)])
variance = sumsq/N
sd = variance ** 0.5
print(sd)
