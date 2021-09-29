import time
import pandas as pd
import numpy as np

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
