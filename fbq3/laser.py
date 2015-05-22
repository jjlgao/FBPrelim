import fileinput, logging, sys, time



def single(size,grid):
	for g in range(len(grid)):
		grid[g] = list(grid[g])


	#Find the location of start, goal, as well as all lasers.
	x = 0
	y = 0
	gx = 0
	gy = 0
	turrets = []
	walls = []
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == 'S':
				x = i
				y = j
			elif grid[i][j] == 'G':
				gx = i
				gx = j
			elif grid[i][j] == '<':
				turrets.append( (i,j,0) )
			elif grid[i][j] == '^':
				turrets.append( (i,j,1) )
			elif grid[i][j] == '>':
				turrets.append( (i,j,2) )
			elif grid[i][j] == 'v':
				turrets.append( (i,j,3) )
			elif grid[i][j] == "#":
				walls.append( (i,j) )

	#Solve.
	queue = [ (x,y,0) ]
	while queue[0] != (gx,gy):
		if len(queue) == 0:
			return 'impossible'
			break

		location = queue[0]
		queue = queue[1:]

		if tuple(location[0:2]) == (gx,gy):
			return str(queue[0][2])

		#return str(turrets) + str(walls)

		possible_locations = []
		#Write out possible new locations.
		j = location[1]
		for i in (location[0]-1,location[0]+1):
			possible_locations.append( (i,j) )
			#return size[0]
			if i >= 0 and i < int(size[0]) and (i,j,0) not in turrets and (i,j,1) not in turrets and (i,j,2) not in turrets and (i,j,3) not in turrets \
				and (i,j) not in walls:
				#Find out if we're in the way of a turret.
				for turret in turrets:
					if turret[2] == 0: #Turns left
						if j not in range(turret[1]):
							queue.append( (i,j,location[2] + 1) )
					elif turret[2] == 1: #Turns up
						if i not in range(turret[0]):
							queue.append( (i,j,location[2] + 1) )
					elif turret[2] == 2: #Turns right
						if j not in range(turret[1],int(size[1])):
							queue.append( (i,j,location[2] + 1) )
					elif turret[2] == 3: #Turns down
						if i not in range(turret[0],int(size[0])):
							queue.append( (i,j,location[2] + 1) )

		i = location[0]
		#return str(i)
		for j in (location[1]-1,location[1]+1):
			possible_locations.append( (i,j) )
			if j >= 0 and j < size[1]:
				if (i,j) not in turrets and (i,j) not in walls:
					#Find out if we're in the way of a turret.
					for turret in turrets:
						if turret[2] == 0: #Turns left
							if j not in range(turret[1]):
								queue.append( (i,j,location[2] + 1) )
						elif turret[2] == 1: #Turns up
							if i not in range(turret[0]):
								queue.append( (i,j,location[2] + 1) )
						elif turret[2] == 2: #Turns right
							if j not in range(turret[1],int(size[1])):
								queue.append( (i,j,location[2] + 1) )
						elif turret[2] == 3: #Turns down
							if i not in range(turret[0],int(size[0])):
								queue.append( (i,j,location[2] + 1) )

		try:
			if queue[0][2] == 7:
				return str(queue)
				return str(possible_locations)
		except IndexError:
			return str(queue)
	return queue[0][2]

def helper(size,location,goal,turrets,walls):
	return





	#return str(size) + " " + str(grid) + " " + str(turrets)





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
			coordinates = alg_input[0].split()
			ind_input = alg_input[1:1 + int(coordinates[0])]
			alg_input = alg_input[1 + int(coordinates[0]):]
			if i == int(num_inputs) - 1:
				line = "Case #" + str(i+1) + ": " + single(coordinates,ind_input)
				print line,
			else:

				line = "Case #" + str(i+1) + ": " + single(coordinates,ind_input) + '\n'
				print line,


	except RuntimeError:
		print("Whoops.")

	sys.stdout = Logger()
	print('Solution found in %.1f seconds.' % (time.time() - starttime))

if __name__ == "__main__":
    main()