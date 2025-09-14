import pandas as pd
import matplotlib as plt
import numpy as np
from datetime import datetime as dt


def main():
    # Turn csv into dataframe for when I want to graph progress
    dw_df = pd.read_csv('DailyWorkout.csv')
    
    repsarr = []
    weights = []
    volume = []
    
    dateinp = input("Enter the date: ")
    date = dt.strptime(dateinp,"%m/%d/%Y")
    exerinp = input('Enter the exercise name: ')
    setsinp = int(input('Enter the number of sets: '))
    

    for i in range(setsinp):
        repsinp = int(input('Enter your reps for set {num}: '.format(num = i + 1)))
        weightinp = int(input('Enter your weight for set {num}: '.format(num = i + 1)))


        volume.append(repsinp*weightinp)
        repsarr.append(repsinp)
        weights.append(weightinp)


    #Appends the parameters to the end of the dataframe
    dw_df.loc[len(dw_df)] = [date.date(),exerinp,setsinp,repsarr,weights,sum(volume)]

    dw_df.to_csv('DailyWorkout.csv', mode='a', header=False, index=False)
    print(dw_df)


if __name__ == "__main__":
    main()