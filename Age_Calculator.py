age=int(input('Enter your age'))
target_age = int(input('Enter the age you want to calculate up to: '))
years_left=target_age-age
days_left=years_left*365
weeks_left=years_left*52
months_left=years_left*12
print(f'You have {days_left} days ,{months_left} months,{weeks_left} weeks left')
