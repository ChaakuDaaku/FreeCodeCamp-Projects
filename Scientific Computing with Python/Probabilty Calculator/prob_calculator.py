import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self, **args):
		self.contents = []
		for i, j in args.items():
			for k in range(j):
				self.contents.append(i)
		self.total = len(self.contents)

	def draw(self, balls):
		if balls > self.total:
			return self.contents

		draw_list = []
		contents = self.contents
		while len(draw_list) < balls:
			index = random.randint(0,len(contents)-1)
			content = contents[index]
			contents.remove(content)
			draw_list.append(content)       
		return draw_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	count = 0 

	for _ in range(num_experiments):
		new_hat = copy.deepcopy(hat)
		draw = new_hat.draw(num_balls_drawn) 
		count_colour = 0   
		for i in expected_balls.keys():
			if draw.count(i)>= expected_balls[i]:
				count_colour +=1 
		if count_colour == len(expected_balls):
			count+=1
	probability = count/num_experiments
	return probability
