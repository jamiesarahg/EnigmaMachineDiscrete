import random
options1= ['123','124','125','132','134','135','142','143','145','152','153','154','213','214','215','231','234','235','241','243','245','251','253','254','312','314','315','321','324','325','341','342','345', '351', '352', '354', '412','413','415','421','423','425','431','432','435','451','452','453','512','513','514','521','523','524','531','532','534','541','542','543']

def countWaysOfLastDayRandom(j):
	options = ['123','124','125','132','134','135','142','143','145','152','153','154','213','214','215','231','234','235','241','243','245','251','253','254','312','314','315','321','324','325','341','342','345','412','413','415','421','423','425','431','432','435','451','452','453','512','513','514','521','523','524','531','532','534','541','542','543']

	chosen = []
	yesterday = random.choice(options)

	for i in range(j):

		correct = False
		loopCount = 0
		while correct == False:
			loopCount +=1
			pick = random.choice(options)
			if pick not in chosen:
				if pick[0] != yesterday[0]:
					if pick[1] != yesterday[1]:
						if pick[2] != yesterday [2]:
							chosen.append(pick)
							correct = True
							options.remove(pick)
							yesterday = pick
			if loopCount > 1000:
				#return chosen
				return False
	count = 0
	count1 = 0
	for item in options1:
		count1+=1
		if item not in chosen:
			if item[0] != yesterday[0]:
				if item[1] != yesterday[1]:
					if item[2] != yesterday[2]:
							count +=1





	return count#, yesterday

for k in range(30):
	result = {}
	for i in range(1000):
		j =  countWaysOfLastDayRandom(k)
		if j in result.keys():
			result[j]+=1
		else:
			result[j]=1
	print str(k) + ' '+str(result.keys())
