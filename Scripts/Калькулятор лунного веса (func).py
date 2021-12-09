import sys


def lves(ves, plves, let):

	#tves=0
	
	proc = 0.165


	for week in range(0, let):
		sves=ves*proc
		print(week, sves)
		ves += plves #ves = ves + plves
		print('В', week, 'году, твой вес составит ==', sves, 'килограмм')

lves(90, 2, 20)


#earth_weight = 70
#moon_index = 0.165
#moon_weight_2018 = earth_weight * moon_index
#print('Ваш вес в 2018 году: ' + str(moon_weight_2018))

#for i in range(1, 16):
 #   print(i, round(earth_weight * moon_index, 2))
  #  earth_weight += 1