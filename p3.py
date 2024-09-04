import pandas as p
from matplotlib import pyplot as m
d={
"First_name":["Aryan","Rohan","Riya","Yash","Siddhant"],
"Last_name":["Singh","Agarwal","Shah","Bhatia","Khanna"],
"Type":["Full-Time","Itern","Full-Time","Part-Time","Full-Time"],
"Dept":["Administration","Technical","Administration","Technical","Management"],
'YoE':[12,25,16,20,28],"Salary":[10,20,30,50,40]
}
df=p.DataFrame(d)
print(df)
av=df.pivot_table(index=['Dept', 'Type'], values='Salary',aggfunc='mean') 
print("Average Salary from ecah dept:\n",av)
sm=df.pivot_table(index=['Type'], values='Salary', aggfunc=['sum', 'mean','count'])
sm.columns=['Total Salary', 'Mean Salary', 'Number of Employees']
print("\nSum and Mean of:\n",sm)
st=df.pivot_table(values='Salary', index='Type',aggfunc='std')
print("\nStandard Deviation:\n",st)
m.plot(df["YoE"],'^-',color='red')
m.plot(df["Salary"],'o-.b')
m.xlabel("YoE"),m.ylabel("salary")
m.title("Salary of a person")
m.grid(True)
m.show()