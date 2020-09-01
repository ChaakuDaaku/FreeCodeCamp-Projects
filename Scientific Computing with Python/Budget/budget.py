class Category:

	def __init__(self, cat):
		self.name = cat
		self.ledger = []
		self.balance = 0
		self.spent = 0

	def __str__(self):
		name = self.name 
		s = name.center(30,"*") 
		for items in self.ledger:
			left = items['description'][0:23]
			right = str("{:.2f}".format(items['amount']))
			s+= f"\n{left:<23}{right:>7}"
		s += "\nTotal: "+ str(self.get_balance())
		return s 

	def check_funds(self, amt):
		return True if amt <= self.balance else False

	def deposit(self, amt, desc=""):
		self.ledger.append({
			"amount": amt,
			"description": desc
		})
		self.balance += amt

	def withdraw(self, amt, desc=""):
		if self.check_funds(amt):
			self.deposit(-amt, desc)
			self.spent += amt
			return True
		return False

	def get_balance(self):
		return self.balance
	
	def transfer(self, amt, obj):
		if self.check_funds(amt):
			obj.deposit(amt, "Transfer from " + self.name)
			self.withdraw(amt,"Transfer to " + obj.name)
			return True
		return False

	

def create_spend_chart(categories):
	total = 0
	for i in categories:
		total += i.spent
	percent_dict = {}
	for k in categories:
		percent_dict[k.name] = int(round(k.spent/total,2)*100)
	output = 'Percentage spent by category\n'
	for i in range(100,-10,-10):
		output += f'{i}'.rjust(3) + '| '
		for percent in percent_dict.values():
			if percent >= i:
				output+= 'o  '
			else:
				output+= '   '
		output += '\n' 
	output += ' '*4+'-'*(len(percent_dict.values())*3+1)
	output += '\n     '
	dict_key_list = list(percent_dict.keys())
	max_len_category = max([len(i) for i in dict_key_list])
	
	for i in range(max_len_category):
		
		for name in dict_key_list:
			if len(name)>i:
				output+= name[i] +'  '
			else:
				output+= '   '
		if i < max_len_category-1:
			output+='\n     '
		
	return output