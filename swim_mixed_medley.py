import datetime, os, time
import pandas as pd

os.system('cls')

def str2sec(time_str):
    if ':' not in str(time_str):
        return float(time_str)
    else:
        m, s = time_str.split(':')
        return float(m) * 60 + float(s)

f = pd.ExcelFile('swimmer_times.xlsx')

time = float('inf')

for i, row in f.parse(sheet_name = 'Back').iterrows(): # i is for name accessing
    N1 = row['Name']
    G1 = row['Gender (M/F)']
    T1 = str2sec(row['Time'])

    for i, row in f.parse(sheet_name = 'Breast').iterrows():
        N2 = row['Name']
        G2 = row['Gender (M/F)']
        T2 = str2sec(row['Time'])
                
        for i, row in f.parse(sheet_name = 'Fly').iterrows():
            N3 = row['Name']
            G3 = row['Gender (M/F)']
            T3 = str2sec(row['Time'])
                        
            for i, row in f.parse(sheet_name = 'Free').iterrows():
                N4 = row['Name']
                G4 = row['Gender (M/F)']
                T4 = str2sec(row['Time'])
                
                # Check for duplicates in relay
                if any([N1, N2, N3, N4].count(x) > 1 for x in [N1, N2, N3, N4]):
                    continue

                # Check if there's more than 2 per gender
                elif [G1, G2, G3, G4].count('M') > 2 or [G1, G2, G3, G4].count('F') > 2:
                    continue

                total = sum([T1, T2, T3, T4])

                if total < time:
                    names = [N1, N2, N3, N4]
                    genders = [G1, G2, G3, G4]
                    ind_time = [T1, T2, T3, T4]
                    time = total


for i, t in enumerate(ind_time):
    ind_time[i] = str(datetime.timedelta(seconds = t))

df = pd.DataFrame({'Name': names, 'Gender': genders, 'Time': ind_time})

print(df)

print('\nTotal: ' + str(datetime.timedelta(seconds = time)))