value = int(input("How much is the purchase price? "))
rate = 0.12
intRate = rate / 12
payment = (intRate * value)

while value > 0:
	
	interest = value * intRate
	principle = payment - interest
	
	if value - payment < 0:
		principle = value
		
	value = value - principle
