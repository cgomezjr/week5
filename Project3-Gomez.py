import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
userFeedback = ""
while userFeedback != "c":
	count += 1
	computerNumber = random.randint(smaller, larger)
	userFeedback = input(f"{computerNumber}, Is my guess too high (H), too low (L), or correct (C)?").lower()
	if userFeedback == "h":
		larger = computerNumber - 1
	elif userFeedback == "l":
		smaller = computerNumber + 1
print("Congradulations! You've got it in", count,
			"tries!")
