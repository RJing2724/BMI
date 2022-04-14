# BMI

# w = weight(kg); h = height(m)

w = input('Please enter your weight:')
w = float(w)
h = input('Please enter your height')
h = float(h)

BMI = w / (h**2) #h^2在python里写作h**2

if BMI < 18.5:
	print(BMI, 'You are underweight.') 

elif 18.5 <= BMI < 24:
	print(BMI, 'You have normal body weight.')

elif 24 <= BMI < 27:
	print(BMI, 'You are overweight.')

elif 27 <= BMI < 30:
	print(BMI, 'You are mildly obese.')

elif 30 <= BMI < 35:
	print(BMI, 'You are moderately obese.')

else:
	print(BMI, 'You are severe obese')