import pandas as pd

df = pd.DataFrame([('Foreign Cinema', 50, 289.0),
                   ('Liho Liho', 45, 224.0),
                   ('500 Club', 102, 80.5),
                   ('The Square', 65, 25.30)],
           columns=('name', 'num_customers', 'AvgBill')
                 )

print(df)
df.to_csv('test_blank.csv')