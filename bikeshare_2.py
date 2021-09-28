import time
import pandas as pd
import numpy as np
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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    """use value counts to find each unique count for month and find the max id value associate with max value count returned
       Use Months list to print out the text string value for the month in the data frame
    """
    print("The highest rider usage month is {} \n".format(MONTHS[df['month'].value_counts().idxmax()].title()))

    month_counts = df['month'].value_counts().sort_index()
    if month_counts.size > 1:
        print("See pop up graph for riders per month, statistics will continue after closing the plot")
        month_counts.plot(kind = 'line',title = 'Total Rider per Month',xlabel ='months',ylabel='number of riders')
        plt.show(block=True)
    """
       Generate a Series based for month by month usage month_counts
       only plot if all the months are included in the data set otherwise skip
       plt.show generates an independent window the user can view or save, with blocking disabled so the reset of the statistics are displayed
    """
    # display the most common day of week

    """use value counts to find each unique count for day of the week and find the max id value associate with max value count returned"""

    print("The highest rider usage Day of the Week is {} \n".format(df['day_of_week'].value_counts().idxmax().title()))

    # display the most common start hour based on id of the max value count for the series extracted from the dataframe

    print("The highest rider usage departure Hour of the Day is {}:00 \n".format(df['hour'].value_counts().idxmax()))

    print("The highest rider usage arrival Hour of the Day is {}:00 \n".format(df['last_hour'].value_counts().idxmax()))
    # display the most common start hour based on id of the max value count for the series extracted from the dataframe

    print("The Earliest Hour of the Day rider departure is {}:00 \n".format(df['hour'].min()))

    print("The Latest Hour of the Day rider arrival is {}:00 \n".format(df['last_hour'].max()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station based on id of the max value count for the series extracted from the dataframe

    print("The most used starting station is {} \n".format(df['Start Station'].value_counts().idxmax().title()))


    start_station_counts = df['Start Station'].value_counts().nlargest(20).sort_index()
    if start_station_counts.size > 1:
        print("See pop up graph for riders per station, statistics will continue after plot window is closed")
        start_station_counts.plot(kind = 'bar',title = 'Total Rider per Per Top 20 Start Stations',xlabel ='Stations',ylabel='number of riders')
        plt.show(block=True)


    # display the most common end station based on id of the max value count for the series extracted from the dataframe

    print("The most common destination is {} \n".format(df['End Station'].value_counts().idxmax().title()))

    df['trip'] = df['Start Station'] + " to " + df['End Station']

    """
     create a trip combination to analyze by concatenating start and end station strings together
     display the most common trip based on id of the max value count for the series extracted from the dataframe
    """

    print("The most common trip is {} \n".format(df['trip'].value_counts().idxmax().title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    max_travel_in_seconds = df['Trip Duration'].max()
    # find the max value of trip duration and then format into hours, minutes and seconds using time library
    print("The longest travel time in Hours, Minutes, Seconds is {} \n".format(time.strftime("%H:%M:%S", time.gmtime(max_travel_in_seconds))))
    # display mean travel time

    average_travel_in_seconds = df['Trip Duration'].mean()
    # find the mean value of trip duration and then format into hours, minutes and seconds using time library

    print("The average travel time in Hours, Minutes, Seconds is {} \n".format(time.strftime("%H:%M:%S", time.gmtime(average_travel_in_seconds))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Total riders by User Types \n{}".format(df['User Type'].value_counts().to_string(header=False)))

    # Display counts of gender

    try:
        print("\nTotal riders by Gender:\n{}\n".format(df['Gender'].value_counts().to_string(header=False)))
    except KeyError:
        print("\nNo Gender Data Available \n")

    """
      Since not all datasets contain gender and birthyear, Try using KeyError exception and
      print a results string to the user indicating no data available
    """
    # Display earliest, most recent, and most common year of birth

    try:
        print("The youngest rider was born in {}\n".format(df['Birth Year'].max()))
        print("The oldest rider was born in {}\n".format(df['Birth Year'].min()))
        print("The most common rider was born in {}\n".format(df['Birth Year'].value_counts().idxmax()))
    except KeyError:
        print("\nNo Birth Year Data Available \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

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
                    time_stats(df)
                    continue_stats = input("Display Next set of statistics any entry or skip: ")
                    if continue_stats != 'skip':
                        station_stats(df)
                    continue_stats = input("Display Next set of statistics any entry or skip: ")
                    if continue_stats != 'skip':
                        trip_duration_stats(df)
                    continue_stats = input("Display Next set of statistics any entry or skip: ")
                    if continue_stats != 'skip':
                        user_stats(df)
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
