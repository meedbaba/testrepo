import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi there, welcome to the US bikeshare databse')
    print('Gain meaningful insights by eploring the database', '\n')
    print('Acceptable Inputs :')
    
    acceptable_cities = ['chicago' , 'new york city', 'washington']
    acceptable_months = ['all','january','febuary','march','april','may','june']
    acceptable_days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    instr = {0 : acceptable_cities,
             1 : acceptable_months,
             2 : acceptable_days}
    print(f'acceptable cities are: {instr[0]}\nacceptable months type are: {instr[1]}\nacceptable day format are: {instr[2]}', '\n')
    print('Let\'s explore some US bikeshare data!')
    
    city = ''
    month = ''
    day = ''
    check = True
    # get user input for month
    while check is True:
        city_input = (input("specify the city you would like to see data for. Could be chicago, new york city, or washington: ")).lower()
        if city_input in acceptable_cities:
            city = city_input
            break
        else:
            print('invalid input. kindly enter either chicago, new york city, or washington')
            check = True
        
    # get user input for month (all, january, february, ... , june)
    while check is True:
        month_input = (input('which month would you like to filter by? (january, february, ... , june) or all for no filter: ')).lower()
        if month_input in acceptable_months:
            month = month_input
            break
        else:
            print('invalid input. kindly refer to the acceptable month list above')
            check = True
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while check is True:
        day_input = (input('which day of the week would you like to filter by? (sunday, monday, ... , saturday) or all : ')).lower()
        if day_input in acceptable_days:
            day = day_input
            break
        else:
            print('invalid input. kindly refer to the acceptable days format above')
            check = True
    print('-'*40)
    print('calculating first statistics')
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    try:
        print(f'The most freqent month integer is: {popular_month}')
    except KeyError as ke:
        print(f'KeyError occurred: {ke}')
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    try:
        print(f'The most freqent day is: {popular_day}')
    except KeyError:
        print('Errata : there is no such column [day of week] in the dataframe')
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most freqent hour is: {popular_hour}')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40, '\n')
    print('calculating next statistics')

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'The most commonly used start station is: {popular_start_station}')

    #display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'The most commonly used end station is: {popular_end_station}')

    #display most frequent combination of start station and end station trip
    df['both_stations'] = df['Start Station'] + ', ' + df['End Station']
    most_frequent_combined_station = df['both_stations'].mode()[0]
    print(f'The most commonly used combined station is: {most_frequent_combined_station}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40, '\n')
    print('calculating next statistics')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'Total travel time is: {total_travel_time}')
    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print(f'The average trip duration is: {average_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40, '\n')
    print('calculating next statistics')

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('what is the breakdown of user type')
    user_types = df['User Type'].value_counts()
    try:
        print(user_types, '\n')
    except KeyError as ke:
        print(f'KeyError occurred: {ke}')
    print('calculating next statistics', '\n')

    # Display counts of gender
    print('what is the breakdown of user gender')
    
    try:
        gender_type = df['Gender'].value_counts()
        print(gender_type, '\n')
    except KeyError:
        print('Error: there is no column [Gender] in the dataframe')
    print('calculating next statistics', '\n')

    # Display earliest, most recent, and most common year of birth
    print('what are the earliest, most recent, and most common year of birth')
    try:
        birth_year_stat = {'earliest' : df['Birth Year'].min(),
                           'most recent' : df['Birth Year'].max(),
                           'most common' : df['Birth Year'].mode()[0]}
        print(f"The oldest rider was born in: {birth_year_stat['earliest']}")
        print(f"The youngest rider was born in: {birth_year_stat['most recent']}")
        print(f"The most frequent riders were born in: {birth_year_stat['most common']}")
    except KeyError:
        print("Error : Column [Birth Year] Does not exist in this Dataframe")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('done calculating' '\n')
    
def display_raw_data(df):
    """Displays rows rows of individual trip data based on user input."""
    print('\ndisplaying individual trip data...\n')
    start_time = time.time()
    
    view_data = (input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')).lower()
    start_loc = 0
    while view_data != 'no':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
    print('you are done viewing individual trip data')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
