print("please calculate what you want")
print("1) a voltage")
print("2) a resistance")
choice=input()

if choice=="1":

	resistantance= float(input("please enter the resistance: "))
	current =float(input("please enter the resistance: "))
	voltage=resistance*current
	print("voltage is")
	print(voltage)

else:
	voltage=float (input("please enter the voltage: "))
	current= float(input("please enter the current" ))

	resistance= voltage/current

	print("the resistance is:")
	print(resistance)