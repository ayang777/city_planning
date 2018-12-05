import sys
import numpy as np
import pandas as pd
import itertools
import matplotlib
import collections
import random
import operator
import timeit


def calculateT(s, a, sp, N, T):
	pass
	n = N[(s, a, sp)]
	d = N[(s, a)]
	T[(s, a, sp)] = float(n/d)


def mle_rl(data, N, R, T):
	pass
	for t in range(len(data)):
		row = data.ix[t]

		s = row['s']
		a = row['a']
		r = row['r']
		sp = row['sp']

		N[(s, a, sp)] += 1
		N[(s, a)] += 1

		calculateT(s, a, sp, N, T)

		R[(s, a)] += r 


		#update Q based on revised estimate of T and R --> dyna?


def value_iteration(R, T, actions, maxState):
	pass
	k = 0
	U = collections.defaultdict(float)

	while True:
		for s in range(1, maxState + 1):
			maxA = None
			maxU = ('-inf')
			#U[(k, s)] = max(R[(s, a)] + sum())




def qlearning(data, Q, discount):
	#loop through every linecalculate q score

	start = timeit.default_timer()

	for t in range(len(data)):
		row = data.ix[t]

		s = row['s']
		a = row['a']
		r = row['r']
		sp = row['sp']

		maxA = 0.0
		
		if sp in Q:
			temp = [Q[sp][x] for x in Q[sp].keys()]
			maxA = max(temp)

		
		if s not in Q:
			Q[s] = {}
			Q[s][a] = r + (discount * maxA)
		else:
			if a in Q[s]:
				Q[s][a] += r + discount * (maxA - Q[s][a])
			else:
				Q[s][a] = r + discount * maxA

	stop = timeit.default_timer()
	print('Time: ', stop - start)

	#print Q

def createPolicy(Q, states):
	policy = []
	for s in states:

		if s in Q:
			curPol = max(Q[s].iteritems(), key=operator.itemgetter(1))[0]
			policy.append(s + " to " + curPol)
		# else:
		# 	policy.append(random.randint(1,4))

	return policy


# # def createPolicySmall(Q):
# # 	policy = []
# # 	for s in range(1, 101):

# # 		if s in Q:
# # 			curPol = max(Q[s].iteritems(), key=operator.itemgetter(1))[0]
# # 			policy.append(curPol)
# # 		else:
# # 			policy.append(random.randint(1,4))

# # 	return policy

# # def createPolicyMed(Q):
# # 	policy = []
# # 	for s in range(1, 50001):

# # 		if s in Q:
# # 			curPol = max(Q[s].iteritems(), key=operator.itemgetter(1))[0]
# # 			policy.append(curPol)

# # 		elif s+1 in Q:
# # 			curPol = max(Q[s+1].iteritems(), key=operator.itemgetter(1))[0]
# # 			policy.append(curPol)

# # 		elif s-1 in Q:
# # 			curPol = max(Q[s-1].iteritems(), key=operator.itemgetter(1))[0]
# # 			policy.append(curPol)

# # 		else: 
# # 			curPol = random.randint(5,7)
# # 			policy.append(curPol)

# # 	return policy


# # def createPolicyLarge(Q):
# # 	policy = []

# # 	for s in range(1, 312021):

# # 		if s in Q:
# # 			curPol = max(Q[s].iteritems(), key=operator.itemgetter(1))[0]
# # 			policy.append(curPol)

# # 		else: 
# # 			curPol = random.randint(1,4)
# # 			policy.append(curPol)

# # 	return policy


def main():

	#discount = 0.95
	discount = 0.95

	#UNCOMMENT FOR SMALL
	# inputfilename = 'small.csv'
	# outputfilename = 'small.policy'




	#UNCOMMENT FOR MEDIUM
	# inputfilename = 'medium.csv'
	# outputfilename = 'medium.policy'
	# discount = 0.805 #medium



	# #UNCOMMENT FOR LARGE
	inputfilename = 'sarsp.csv'
	outputfilename = 'policy'

	data = pd.read_csv(inputfilename)
	grouped = data.groupby(by="s")
	#states = grouped.groups.keys()
	states = []
	for state in data['s']:
		if state not in states: states.append(state)

	print states



	Q = {}
	qlearning(data, Q, discount)
	policy = createPolicy(Q, states)

	#policy = createPolicySmall(Q)

	#policy = createPolicyMed(Q)

	#policy = createPolicyLarge(Q)

	print len(policy)

	with open (outputfilename, 'w') as f:
		for item in policy:
			f.write("%s\n" % item)





if __name__ == '__main__':
    main()

