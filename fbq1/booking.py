import fileinput, logging, sys, time



def find_min_number(number):
	array = list(number)

	min_d = int(number)
	for i in range(len(array)):
		for j in range(i,len(array)):
			temp = array[:]
			temp_i = array[i]
			temp_j = array[j]
			if not (i == 0 and int(temp_j) == 0):
				temp[i] = temp_j
				temp[j] = temp_i
				if (int(''.join(temp)) < min_d):
					min_d = int(''.join(temp))

	return str(min_d)

def find_max_number(number):
	array = list(number)

	min_d = int(number)
	for i in range(len(array)):
		for j in range(i,len(array)):
			temp = array[:]
			temp_i = array[i]
			temp_j = array[j]
			if not (i == 0 and int(temp_j) == 0):
				temp[i] = temp_j
				temp[j] = temp_i
				if (int(''.join(temp)) > min_d):
					min_d = int(''.join(temp))

	return str(min_d)




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
			if i == int(num_inputs) - 1:
				line = "Case #" + str(i+1) + ": " + find_min_number(alg_input[i]) + " " + find_max_number(alg_input[i])
				print line,
			else:

				line = "Case #" + str(i+1) + ": " + find_min_number(alg_input[i]) + " " + find_max_number(alg_input[i]) + '\n'
				print line,


	except RuntimeError:
		print("Whoops.")

	sys.stdout = Logger()
	print('Solution found in %.1f seconds.' % (time.time() - starttime))

if __name__ == "__main__":
    main()