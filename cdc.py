from tarfile import PAX_FIELDS
import csv

import plotly.express as px   

import os
dirpath = os.path.dirname(os.path.realpath(__file__))
print(os.listdir(dirpath))
print(dirpath)

import pandas as pd
data = pd.read_csv("Annual_Greenhouse_Gas_(GHG)_Air_Emissions_Accounts.csv")
#print(data.head(10))


# Figures for line graphs of G20 and World

newList = []
newList2 = []
newList3 = []

newListWorld = []
newListWorld2 = []
newListWorld3 = []

# emissions data into newList
for x in range(5):
    for index, line in enumerate(data.iloc[x+475]):
        #if index == 1:
            #print(line)
        #if index == 8:
            #print(line)
        if index < 11:
            continue
        newList.append(line)


# years into newList2
for x in range(5):
    for index, line in enumerate(data):
        if index > 40:
            break
        if index < 11: 
            continue
        newList2.append(line)


# gas type into newList3
for x in range(5):
    for y in range(12):
        if x == 0:
            gasType = "CO2"
        if x == 1:
            gasType = "Fluorinated Gases"
        if x == 2:
            gasType = "Greenhouse"
        if x == 3:
            gasType = "Methane"
        if x == 4:
            gasType = "Nitrous Oxide"
        newList3.append(gasType)


# emissions data into newListWorld
for x in range(5):
    for index, line in enumerate(data.iloc[x+1039]):
        #if index == 1:
            #print(line)
        #if index == 8:
            #print(line)
        if index < 11:
            continue
        newListWorld.append(line)


# years into newList2
for x in range(5):
    for index, line in enumerate(data):
        if index > 40:
            break
        if index < 11: 
            continue
        newListWorld2.append(line)


# gas type into newList3
for x in range(5):
    for y in range(12):
        if x == 0:
            gasType = "CO2"
        if x == 1:
            gasType = "Fluorinated Gases"
        if x == 2:
            gasType = "Greenhouse"
        if x == 3:
            gasType = "Methane"
        if x == 4:
            gasType = "Nitrous Oxide"
        newListWorld3.append(gasType)

#print(newList)
newDataFrameYears = pd.DataFrame(newList2, columns = ['years'])
newDataFrame = pd.DataFrame(newList, columns = ['emissions'])
newDataFrameGases = pd.DataFrame(newList3, columns = ['gases'])
df = pd.concat([newDataFrameYears, newDataFrame], axis=1)
df = pd.concat([df, newDataFrameGases], axis = 1)
#print(df)

newDataFrameYears2 = pd.DataFrame(newListWorld2, columns = ['years'])
newDataFrame2 = pd.DataFrame(newListWorld, columns = ['emissions'])
newDataFrameGases2 = pd.DataFrame(newListWorld3, columns = ['gases'])
df2 = pd.concat([newDataFrameYears2, newDataFrame2], axis=1)
df2 = pd.concat([df2, newDataFrameGases2], axis = 1)
#print(df2)

fig = px.line(df, x="years", y="emissions", color="gases", title="G20 Annual Emissions by Gas")
#fig.show()

fig2 = px.line(df2, x="years", y="emissions", color="gases", title="Global Annual Emissions by Gas")
#fig2.show()

newListIndustry = []
newListYears = []
newListType = []

# Figures for histograms of industries within G20 and World
for x in range(44):
    for index, line in enumerate(data.iloc[x]):
        #if index == 1:
            #print(line)
        #if index == 8:
            #print(line)
        if index == 9:
            if line != "Greenhouse gas":
                break
        if index < 22:
            continue
        newListIndustry.append(line)

#for x in range(1):
    #for index, line in enumerate(data):
        #if index > 40:
            #break
        #if index < 11: 
            #continue
        #newListYears.append(line)

#for x in range(12):
for y in range(10):
    if y == 0:
        industryType = "Agriculture, Forestry, and Fishing"
    if y== 1:
        industryType = "Construction"
    if y == 2:
        industryType = "Electricity, Gas, Steam and Air Conditioning Supply"
    if y == 3:
        industryType = "Manufacturing"
    if y == 4:
        industryType= "Mining"
    if y == 5:
        industryType = "Other Service Industries"
    if y == 6: 
        industryType = "Total Households"
    if y == 7:
        industryType = "Total Industry and Households"
    if y == 8:
        industryType = "Transportation and Storage"
    if y == 9:
        industryType = "Water supply; sewerage, waste management and remediation activities"
    newListType.append(industryType)

#print(agriList)
yearsDF = pd.DataFrame(newListYears, columns = ['Years'])
industryDF = pd.DataFrame(newListType, columns = ['Industry'])
#print(yearsDF)
agriDF = pd.DataFrame(newListIndustry, columns = ['Emissions'])
#agriDF = pd.concat([yearsDF, agriDF], axis=1)
agriDF = pd.concat([agriDF, industryDF], axis=1)
agriDF = agriDF.drop(7, axis=0)
#print(agriDF)
fig3 = px.histogram(agriDF, x="Industry", y="Emissions", title="Emissions by Industry in Advanced Economies")
#fig3.show()


newListIndustryWorld = []
newListYearsWorld = []
newListTypeWorld = []

for x in range(44):
    for index, line in enumerate(data.iloc[x+356]):
        #if index == 1:
            #print(line)
        #if index == 8:
            #print(line)
        if index == 9:
            if line != "Greenhouse gas":
                break
        if index < 22:
            continue
        newListIndustryWorld.append(line)

for y in range(10):
    if y == 0:
        industryType = "Agriculture, Forestry, and Fishing"
    if y== 1:
        industryType = "Construction"
    if y == 2:
        industryType = "Electricity, Gas, Steam and Air Conditioning Supply"
    if y == 3:
        industryType = "Manufacturing"
    if y == 4:
        industryType= "Mining"
    if y == 5:
        industryType = "Other Service Industries"
    if y == 6: 
        industryType = "Total Households"
    if y == 7:
        industryType = "Total Industry and Households"
    if y == 8:
        industryType = "Transportation and Storage"
    if y == 9:
        industryType = "Water supply; sewerage, waste management and remediation activities"
    newListTypeWorld.append(industryType)

#print(agriList)
yearsDFWorld = pd.DataFrame(newListYearsWorld, columns = ['Years'])
industryDFWorld = pd.DataFrame(newListTypeWorld, columns = ['Industry'])
#print(yearsDF)
agriDFWorld = pd.DataFrame(newListIndustryWorld, columns = ['Emissions'])
#agriDF = pd.concat([yearsDF, agriDF], axis=1)
agriDFWorld = pd.concat([agriDFWorld, industryDFWorld], axis=1)
agriDFWorld = agriDFWorld.drop(7, axis=0)
#print(agriDFWorld)
fig4 = px.histogram(agriDFWorld, x="Industry", y="Emissions", title="Emissions by Industry in Emerging and Developing Economies")
#fig4.show()

pieEmissions = []
# locations of continents on graph: 34 (Africa), 78 (Americas), 123 (Asia), 168 (Australia), 390 (Europe)
countriesIndex = [34, 78, 123, 168, 390]
for x in countriesIndex:
    for index, line in enumerate(data.iloc[x+43]):
            #if index == 1:
                #print(line)
            #if index == 8:
                #print(line)
            #if index == 9:
                #print(line)
                #if line != "Greenhouse gas":
                    #break
            if index < 22:
                continue
            pieEmissions.append(line)

#print(pieEmissions)
pieDF = pd.DataFrame(pieEmissions, columns = ['Emissions'])
countries = pd.DataFrame(['Africa', 'Americas', 'Asia', 'Australia', 'Europe'], columns = ['Countries'])
pieDF = pd.concat([pieDF, countries], axis=1)
print(pieDF)

fig5 = px.pie(pieDF, values='Emissions', names='Countries', title='Pie Chart of Emissions Distributions by Continent')
fig5.show()