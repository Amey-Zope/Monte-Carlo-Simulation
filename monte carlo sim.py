import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel(
    r'C:\Users\Amey\Desktop\Monte Carlo Simulation\monte carlo.xlsx')

# print(df)
# print(df['probability'].count())

cum_prob = []
cum_sum = 0
cum_prob.append(1)

for i in range(1, df['probability'].count()):
    for j in range(df['probability'].count()-i):
        cum_sum += df.iloc[j]['probability']
    cum_prob.append(cum_sum.round(2))
    cum_sum = 0


cum_prob = cum_prob[::-1]


# for i in range(1, df['probability'].count()):
#     df['cummulative_probability']=df['cummulative_probability']+df[0:i+1]['probability']
df['cummulative_probability'] = cum_prob

rand_interval_start = []
rand_interval_end = []
rand_interval_start.append(0)
# rand_interval_end.append(0)

for i in range(len(cum_prob)-1):
    rand_interval_start.append(int(str(cum_prob[i])[2:]))

df['random_interval_start'] = rand_interval_start
# print(rand_interval_start)

for i in range(1, len(cum_prob)):
    rand_interval_end.append(rand_interval_start[i]-1)

rand_interval_end.append(99)

df['random_interval_end'] = rand_interval_end

noOfIterations = int(input("Enter no. of days you want to simulate for: "))

days = []
expected_demand = []

for i in range(1, noOfIterations+1):
    days.append(i)
    randomNo = random.randint(0, 99)
    for j in range(len(rand_interval_start)):
        if(randomNo >= rand_interval_start[j] and randomNo <= rand_interval_end[j]):
            expected_demand.append(df.iloc[j]['daily_demand'])
            break

print("No of days", len(days))
print("No of demands", len(expected_demand))


# print(expected_demand)

# df['simulated_demand'] = expected_demand
# print(df.iloc[2]['daily_demand'])


print(df)

x = np.array(days)
y = np.array(expected_demand)

print("x ", x)
print("y ", y)

avg_demand = sum(expected_demand)/len(expected_demand)

plt.plot(x, y, label="demand")

plt.xlabel('No. of days')
plt.ylabel('Simulated demand')

plt.text(65, 45, 'Average demand: %d ' % (avg_demand),
         fontsize=12, bbox=dict(facecolor='red', alpha=0.5))

plt.title('Demand Graph')


plt.legend()

mng = plt.get_current_fig_manager()
mng.window.state("zoomed")

plt.show()
