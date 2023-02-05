import pandas as pd
df = pd.read_excel('TokyoCafe.xlsx')
length = len(df)
cafeArray = [length]
cafeInfo = [length]      
cafeArray = df["Name"]
cafeInfo = df["Address"] 
print(cafeArray)
print(cafeInfo)

userInput = input("enter a Cafe Name:    ")
for i in range(0,length):
    if userInput == cafeArray[i]:
        index=i
        print(cafeInfo[i])




