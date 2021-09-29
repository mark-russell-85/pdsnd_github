import time
import pandas as pd
import numpy as np
import data_analysis as da
import matplotlib.pyplot as plt
pd.options.plotting.backend

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all', 'january', 'february', 'march', 'april','may', 'june']
DAYS = ['all', 'monday', 'tuesday','wednesday','thursday','friday','saturday','sunday']
"""
predefine constants for list or months for validity checks, using all as the first
item in the list so indexes align to month and day numbers so there is a ready list
"""
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    The queries can be combined in a single function as an improvement
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    repeat_query = True
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while repeat_query == True:
        city = input("Enter a city name: chicago, new york city or washington; enter exit to restart: ").lower()
        if city == 'exit':
            return city, city, city
        elif city not in CITY_DATA:
            print("City {} not found, please re-enter a valid name or exit to stop\n".format(city))
        else:
            repeat_query = False
    repeat_query = True
    """
    query for the city name from the user and check if in the name is invalid
    If not valid reprompt the user for a correct entry
    If user selects exit, return exit in all parameters
    """
    # get user input for month (all, january, february, ... , june)
    while repeat_query == True:
        month = input("Enter a month or all: all, january, february, ... , june; enter exit to restart: ").lower()
        if month == 'exit':
            return month, month, month
        elif month not in MONTHS:
            print("Entered Month {} not found, please re-enter a valid month or allor exit to stop\n".format(month))
        else:
            repeat_query = False
    repeat_query = True
    """
    query for the month or all from the user and check if in the month is invalid
    If not valid reprompt the user for a correct entry
    If user selects exit, return exit in all parameters
    """
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while repeat_query == True:
        day = input("Enter a specific day or all: all, monday, tuesday, ... , sunday; enter exit to restart: ").lower()
        if day == 'exit':
            return day, day, day
        if day not in DAYS:
            print("Entered Day {} not found, please re-enter a valid month or all or exit to stop\n".format(day))
        else:
            repeat_query = False
    repeat_query = True
    """
    query for the day or all from the user and check if in the day is invalid
    If not valid reprompt the user for a correct entry
    If user selects exit, return exit in all parameters
    """
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
        # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    #use date time functions for month and hour to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['last_hour'] = df['End Time'].dt.hour

        #create a hour column to analyze mst popular hour

    df['day_of_week'] = df['Start Time'].dt.strftime('%A')
    """
    using python strftime formatting method to extact day of week name
    string for comparison in the filter for the new column datatype
    """
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month)
        # filter by month to create the new dataframe
        # do not compensate for 0 index since all value is always in 0
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    # print(df)
    return df

def view_raw_data(df):
    """Displays raw data on bikeshare users for the selected city and time period."""

    # Display columns of the dataset first
    print(df.columns)

    last_item = df.last_valid_index() + 1
    index = 5
    start_item = 0
    next_5_rows = 'yes'
    # prompt user to start viewing data
    while next_5_rows == 'yes':
        print(df[start_item:start_item + index])
        if start_item + index <= last_item - index:
            start_item = start_item + index
            # determine there are 5 more data items, then adjust start_item
        elif start_item + index > last_item - index:
            start_item = start_item + index
            index = last_item - start_item
            #if there are more items, but less then 5 remaining, move up start point and adjust index to remaining number of items + 1

        if index == 0:
            print("End of Raw Data, please select yes on restart query\n")
            return()
            # Send the user back to main, so either continue with stats or select a new dataset

        #iterate to the next start index in the dataframe
        next_5_rows = input("Do you want to display next 5 rows of data: Enter yes or no.\n").lower()
        # ensure the user enters a correct response if no requeue a question
        while next_5_rows != 'yes' and  next_5_rows != 'no':
            next_5_rows = input("You entered {} Please Enter yes or no.\n".format(next_5_rows)).lower()

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()


        #set a booleen check to regulate selection of raw lines

        """
        Only load data and produce statistics or raw datasets for selected city
        if city does not equal exit, else prompt to restart
        """
        if city != 'exit':
            print("For the selected City of {} and Month of {} and Day of {}: \n".format(city,month,day))
            df = load_data(city, month, day)
            # get user input for raw or stats selection
            """
                variable repeat_query used to track if user successfully entered raw, stats or exit..  False == successful entry
            """
            repeat_query = True

            while repeat_query == True:
                raw_or_stats = input("Please select viewing of raw or statistics by entering raw or stats else exit to restart: ").lower()
                #set string value of input into raw_or_stats for determining if user wishes to exit, view raw data, view statistics or incorrectly enters an answer
                if raw_or_stats == 'exit':
                    repeat_query = False
                # break loop when the user wants to exit
                elif raw_or_stats != 'raw' and raw_or_stats != 'stats':
                    print("User entered {} which is not valid, please re-enter raw or stats or exit to stop\n".format(raw_or_stats))
                # user error entry, display entered text and correct set of choices
                elif raw_or_stats == 'stats':
                # user selected statistical data by entering stats - run all and display all the statistics functions for the selected dataframe
                    da.time_stats(df)
                    continue_stats = input("Display Next set of statistics any entry or skip: ")
                    if continue_stats != 'skip':
                        da.station_stats(df)
                    continue_stats = input("Display Next set of statistics any entry or skip: ")
                    if continue_stats != 'skip':
                        da.trip_duration_stats(df)
                    continue_stats = input("Display Next set of statistics any entry or skip: ")
                    if continue_stats != 'skip':
                        da.user_stats(df)
                    repeat_query = True
                else:
                # user selected raw by entering raw - call function to allow the user to cycle through the raw data
                    view_raw_data(df)
                    repeat_query = True

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        # requery user if yes or no was not entered by the user
        while restart != 'yes' and  restart != 'no':
              restart = input("You entered {} Please Enter yes or no.\n".format(restart)).lower()
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
