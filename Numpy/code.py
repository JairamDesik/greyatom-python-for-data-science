# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)
census = np.concatenate((data, new_record))
print(census)
print(census.shape)

# Step 2
age = np.array(census[ : , 0])
print(age)
max_age = age.max()
print(max_age)
min_age = age.min()
print(min_age)
age_mean = np.mean(age)
print(age_mean)
age_std = np.std(age)
print(age_std)

# Step 3
race = np.array(census[:, 2])
print(race)
a = 0
race_0, race_1, race_2, race_3, race_4 = np.array([]), np.array([]), np.array([]), np.array([]), np.array([])

for i in race:
    if i == 0:
        race_0 = np.concatenate((race_0, census[a]))
    elif i == 1:
        race_1 = np.concatenate((race_1, census[a]))
    elif i == 2:
        race_2 = np.concatenate((race_2, census[a]))
    elif i == 3:
        race_3 = np.concatenate((race_3, census[a]))
    else:
        race_4 = np.concatenate((race_4, census[a]))
    a = a+1

len_0 = len(race_0)
print(len_0)
len_1 = len(race_1)
print(len_1)
len_2 = len(race_2)
print(len_2)
len_3 = len(race_3)
print(len_3)
len_4 = len(race_4)
print(len_4)
length = np.array([len_0, len_1, len_2, len_3, len_4])
minority = length.min()

if minority == len_0:
    minority_race = 0
elif minority == len_1:
    minority_race = 1
elif minority == len_2:
    minority_race = 2
elif minority == len_3:
    minority_race = 3
else:
    minority_race = 4

print('minority_race : ' , minority_race)

# Step 4
senior_citizens = np.empty((0,8))
working_hours_sum = 0
for i in census:
    if i[0] > 60:
        senior_citizens = np.concatenate((senior_citizens, np.array([i])))
        working_hours_sum += i[6]
#print(senior_citizens)
senior_citizens_len = len(senior_citizens)
print(working_hours_sum)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

# Step 5
high, low = np.empty((0,8)), np.empty((0,8))
for i in census:
    if i[1] > 10:
        high = np.concatenate((high, np.array([i])))
    else:
        low = np.concatenate((low, np.array([i])))

avg_pay_high = np.mean(high[ : , 7])
print(avg_pay_high)
avg_pay_low = np.mean(low[ : , 7])
print(avg_pay_low)

#Code starts here




