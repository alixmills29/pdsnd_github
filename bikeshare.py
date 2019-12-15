import time
import pandas as pd
import numpy as np
import statistics

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    city = input("Please enter the name of the city you would like to analyze (chicago, new york city, washington). \n").lower()

    while city not in cities:
        print("You have entered an invallid city name. \n")
        city = input("Please enter the city you would like to analyze. \n").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april", "may", "june", "all"]
    month = input("Please enter the month you would like to analyze (january, february, march, april, may, june). If you would like to analyze all months type 'all'\n").lower()
    while month not in months:
        print("You have entered an invallid month. \n")
        month = input("Please enter the month you would like to analyze again. \n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    day = input("Please enter the day you would like to analyze (monday, tuesday, wednesday, thursday, friday, saturday, sunday). If you would like to analyze all days type 'all'\n").lower()
    while day not in days:
        print("You have entered an invallid day. \n")
        day = input("Please enter the day you would like to analyze again. \n").lower()

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

    # load data file into a dataframe
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

    # TO DO: display the most common month
    popular_month = statistics.mode(df['month'])
    print('Most Frequent Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = statistics.mode(df['day_of_week'])
    print('Most Frequent Day of Week:', popular_day)

    # TO DO: display the most common start hour
        # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

        # find the most common hour (from 0 to 23)
    popular_hour = statistics.mode(df['hour'])

    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = statistics.mode(df['Start Station'])
    print('Most Frequent Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = statistics.mode(df['End Station'])
    print('Most Frequent End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start Station and End Station'] = df['Start Station'].map(str) + ", " + df['End Station']
    popular_start_and_end_station = df['Start Station and End Station'].mode()
    print('Most Frequent Start and End Station Combination: ', popular_start_and_end_station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time: ", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time: ", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types Count:\n', user_types)


    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender_count = df['Gender'].value_counts()
        print('Gender Count:\n', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        most_recent_birth_year = int(df["Birth Year"].max())
        most_common_birth_year = int(df["Birth Year"].mode().loc[0])
        print("Most Recent Birth Year: {} \n Most Common Birth Year: {}".format(most_recent_birth_year, most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def see_data(df):
    answer = input("Do you want to see 5 lines of data? (yes, no)")
    n = 0
    while answer == 'yes':
        n += 5
        print(df.head(n))
        answer = input("Do you want to see 5 more lines? (yes, no)")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
