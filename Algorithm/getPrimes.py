import math

pp=2
ps=[pp]
pp+=1
ps.append(pp)
lim=raw_input("\n Generate prime numbers up to what number? : ")
while pp<int(lim)-1:
	pp+=2
	test=True
	sqrtpp=math.sqrt(pp)
	for a in ps:
		if a>sqrtpp: break
		if pp%a==0:
                     test=False
                     break
	if test: ps.append(pp)
	
print ps