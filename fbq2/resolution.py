import fileinput, logging, sys, time



def yesorno(goal,input_str):
	g_p = int(goal[0])
	g_c = int(goal[1])
	g_f = int(goal[2])
	if len(input_str) == 0:
		if (g_p != 0 and g_c != 0 and g_f != 0):
			return 'no'
		else:
			return 'yes'
	elif len(input_str) == 1:
		temp = input_str[0].split()
		i_p = int(temp[0])
		i_c = int(temp[1])
		i_f = int(temp[2])
		if (g_p == i_p and g_c == i_c and g_f == i_f) or (g_p == 0 and g_c == 0 and g_f == 0):
			return 'yes'
		else:
			return 'no'
	else:
		temp = input_str[0].split()
		i_p = int(temp[0])
		i_c = int(temp[1])
		i_f = int(temp[2])
		g_pnew = g_p - i_p
		g_cnew = g_c - i_c
		g_fnew = g_f - i_f
		if yesorno([g_p,g_c,g_f],input_str[1:]) == 'yes' or yesorno([g_pnew,g_cnew,g_fnew],input_str[1:]) == 'yes':
			return 'yes'
		else:
			return 'no'





"""
--------------------------------------------------------------------------------------------
********************************************MAIN********************************************
--------------------------------------------------------------------------------------------
"""

def main():
	#A class to let me print time to the terminal.
	class Logger(object):
	    def __init__(self):
	        self.log = open("logfile.txt", "w")

	    def write(self, message):
	        self.log.write(message)  

	starttime = time.time()

	#Create a list of all lines in the input file, which will be fed into the algorithm.
	alg_input = []
	for line in fileinput.input():
	    line = line.strip() # Remove the trailing newline
	    alg_input.append(line)

	#print(alg_input)

	try:
		num_inputs = alg_input[0]
		alg_input = alg_input[1:]
		for i in range(int(num_inputs)):
			num_food = int(alg_input[1])
			i_want_this_much = alg_input[0]
			ind_input = alg_input[2:num_food + 2]
			alg_input = alg_input[num_food+2:]
			if i == int(num_inputs) - 1:
				line = "Case #" + str(i+1) + ": " + yesorno(i_want_this_much.split(),ind_input)
				print line,
			else:

				line = "Case #" + str(i+1) + ": " + yesorno(i_want_this_much.split(),ind_input) + '\n'
				print line,


	except RuntimeError:
		print("Whoops.")

	sys.stdout = Logger()
	print('Solution found in %.1f seconds.' % (time.time() - starttime))

if __name__ == "__main__":
    main()