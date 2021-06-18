import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import random
import csv
import statistics

df = pd.read_csv('savings_data.csv')

fig1 = px.scatter(df, y = 'quant_saved', color = 'female')

fig1.show()

with open('savings_data.csv', newline = '') as f:
    reader = csv.reader(f)
    savings_data = list(reader)

savings_data.pop(0)

total_entries = len(savings_data)

total_female = 0

for data in savings_data:
    if int(data[1]) == 1:
        total_female += 1

fig2 = go.Figure(go.Bar(x = ['Female', 'Male'], y = [total_female, [total_entries - total_female]]))

fig2.show()

all_savings = []

for data in savings_data:
    all_savings.append(float(data[0]))

print(f"Mean of Savings - {statistics.mean(all_savings)}")

print(f"Mode of Savings - {statistics.mode(all_savings)}")

print(f"Median of Savings - {statistics.median(all_savings)}")

female_savings = []

male_savings = []

for data in savings_data:
  if int(data[1]) == 1:
    female_savings.append(float(data[0]))
  else:
    male_savings.append(float(data[0]))

print(f"Mean of Female Savings - {statistics.mean(female_savings)}")

print(f"Mode of Female Savings - {statistics.mode(female_savings)}")

print(f"Median of Female Savings - {statistics.median(female_savings)}")

print(f"Mean of Male Savings - {statistics.mean(male_savings)}")

print(f"Mode of Male Savings - {statistics.mode(male_savings)}")

print(f"Median of Male Savings - {statistics.median(male_savings)}")

print(f"Standard Deviation of Female Savings - {statistics.stdev(female_savings)}")

print(f"Standard Deviations of Male Savings - {statistics.stdev(male_savings)}")

print(f"Standard Deviations of All Savings - {statistics.stdev(all_savings)}")

wealthy = []

savings = []

for data in savings_data:
    if float(data[3]) != '0':
        wealthy.append(float(data[3]))
        savings.append(float(data[0]))

correlation = np.corrcoef(wealthy, savings)

print(f"Correlation between the wealth of the person and the savings - {correlation[0, 1]}")

fig3 = ff.create_distplot([df['quant_saved'].tolist()], ['Savings'], show_hist = False)

fig3.show()