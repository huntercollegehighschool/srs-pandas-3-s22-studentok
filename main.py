# 1. Import pandas
import pandas as pd 

# 2. Read the "metacritic2.csv" file, and save the data in a dataframe variable. Print the data

videogames = pd.read_csv('metacritic2.csv')
print(videogames)


# 3. Create a new dataframe with only Mario Games. Save that in a new dataframe variable and print that data (this will involve Boolean indexing)

mariogames = videogames[videogames['Game'].str.contains('Mario')]
print(mariogames)


# 4. Sort the Mario data by release year in descending order. (a .sort_values() function exists)

mariogames = mariogames.sort_values(by=['Release Year'],ascending = False)



# 5. Last time we used a loop to find individual data on different platforms, years, etc. There is a .groupby() function that exists as well. Let's start by grouping by Release Year. Run the following code:
# <var> = <dataframe>.groupby("Release Year").count()
# What does it seems like count presents?

yeargroup = videogames.groupby('Release Year').count()



# 6. Use groupby again, but this time on Platform. Afterwards, run .count(), .mean(), and .median(). Which platform looks like it has the best games?

platformgroup = videogames.groupby('Platform')
platformcount = platformgroup.count()
platformmean = platformgroup.mean()
platformmedian = platformgroup.median()


# 7. Create a new dataframe from the HunterAMC.csv file.

AMCdata = pd.read_csv('HunterAMC.csv', sep = '\t')
print(AMCdata)

# 8. In that csv, contest 0 is the AMC 10, and contest 2 is the AMC 12. Create two separate dataframes containing data from the two different contests.
AMC10 = AMCdata[AMCdata['contest'] == 0]
print(AMC10)
AMC12 = AMCdata[AMCdata['contest']==0]
print(AMC12)


# 9. Find the average scores for each contest.

average_10 = AMC10['TotalScore'].mean()
average_12 = AMC12['TotalScore'].mean()


# 10. For each column, count how often each answer choice was selected.


