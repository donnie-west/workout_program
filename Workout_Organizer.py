import pandas as pd
import matplotlib as plt
import numpy as np
from datetime import datetime as dt

def addExercise(laterFlag,exercise = '',datearg = ''):
    temp_df = pd.DataFrame()

    repsarr = []
    weights = []
    volume = []
    
    if datearg == '':
        dateinp = input("Enter the date: ")
        date = dt.strptime(dateinp,"%m/%d/%Y").date()

    else:
        date = dt.strptime(datearg,"%m/%d/%Y").date()

    if exercise == '':
        exerinp = input('Enter the exercise name: ')

    else:
        exerinp = exercise

    if laterFlag == 0:

        setsinp = int(input('Enter the number of sets for {exer}: '.format(exer=exercise)))
    
        for i in range(setsinp):
            repsinp = int(input('Enter your reps for set {num}: '.format(num = i + 1)))
            weightinp = int(input('Enter your weight for set {num}: '.format(num = i + 1)))


            volume.append(repsinp*weightinp)
            repsarr.append(repsinp)
            weights.append(weightinp)

            print('')

    elif laterFlag == 1:
        setsinp = int(input('Enter the number of sets for {exer}: '.format(exer=exercise)))
    
        for i in range(setsinp):
            repsinp = int(input('Enter your reps for set {num}: '.format(num = i + 1)))
            weightinp = -1


            volume.append(repsinp*weightinp)
            repsarr.append(repsinp)
            weights.append(weightinp)

            print('')
        


    temp_df.loc[len(temp_df)] = [date,laterFlag,exerinp,setsinp,repsarr,weights,sum(volume)]
    return temp_df

def addWorkout(exercises,date,laterFlag):
    temp_workout_df = pd.DataFrame()

    for i in exercises:
        temp_workout_df=pd.concat([temp_workout_df,addExercise(laterFlag,i,date)])

    return temp_workout_df

#def changeWorkout():

def main():
    # Turn csv into dataframe for when I want to graph progress
    dw_df = pd.read_csv('DailyWorkout.csv')

    '''
    if 1 in dw_df['DataNotFilled']:
        print('Are you ready to fill in data for the following dates?')
        temp = dw_df[dw_df['DataNotFilled'] == 1]
        print(temp['Dates'])
        chg = int(input('Enter 1 for yes and 0 for no'))

        if chg == 1:
            print('Please enter a number for the corresponding date you would like to change')
            for date in temp['Dates']:
                print('{num}. {dates}'.format(num = temp.index,dates = str(date) ) )

            changeWorkout()

    '''
    workoutArr = []
    numExer = int(input('How many exercises do you want to do: '))
    chosenDate = input('What date are you doing these exercises (MM/DD/YYYY): ')

    for i in range(numExer):
        workoutArr.append(input("\nWhat is exercise {num}: ".format(num = i + 1)))

    laterFlag = int(input('Is this for a future workout or a past one (0:past 1:future): '))
        

    addWorkout(workoutArr,chosenDate,laterFlag).to_csv('DailyWorkout.csv', mode='a', header=False, index=False)
    
    print(dw_df)


if __name__ == "__main__":
    main()