numbers = input()
a,b,c,d = numbers
i = len(numbers)-1

op = ['+','-']

for j in range(2 ** i):
  o = [op[int((j>>k)&1)] for k in range(i)]
  f=f"{a}{o[0]}{b}{o[1]}{c}{o[2]}{d}"
  if eval(f) == 7:
    print(f+'=7')
    break
      