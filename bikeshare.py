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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWhich city would you like to explore: chicago, new york city or washington?\n").lower()
        if city not in CITY_DATA:
            print("\nInvalid input\n")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month would you like to filter by? Name a month between january and june to filter by, or "all" to apply no month filter\n').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month in months:
            break
        else:
            print('Unvaild Input, Please name the month to filter by, or "all" to apply no month filter\n')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day would you like to filter by? Name a day to filter by, or "all" to apply no day filter\n').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday', 'sunday']
        if day == 'all':
            break
        elif day in days:
            break
        else:
            print('Invalid input, Please name a day to filter by, or "all" to apply no day filter')
            continue

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
    df['day_of_week'] = df['Start Time'].dt.day_name()

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
    common_month = df['month'].mode()[0]
    print('The most common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().index[0]
    print('Most commonly used start station:', format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().index[0]
    print('Most commonly used end station:', format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+' / '+df['End Station']
    common_trip = df['combination'].value_counts().index[0]
    print('Most frequent combination of start and end station trip:', format(common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time: {} hours.'.format(total_time/3600))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time: {} minutes.'.format(mean_time/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print ('Counts of user types:\n',user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('Counts of gender:\n',df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year_of_birth=df['Birth Year'].min()
        print('Earliest year of birth: %i.'%(earliest_year_of_birth))
        most_recent_year_of_birth=df['Birth Year'].max()
        print('Most recent year of birth: %i.'%(most_recent_year_of_birth))
        most_common_year_of_birth=df['Birth Year'].value_counts().index[0]
        print('Most common year of birth: %i.'%(most_common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#prompt the user if they want to see 5 lines of raw data
def raw(df):
    raw = 1
    while True:
        raw_data = input("\nWould you like to see 5 lines of raw data? Yes or No\n")
        if raw_data.lower() == 'yes':
            print(df.iloc[raw:raw+5])
            raw = raw+5
        elif raw_data.lower() == 'no':
            break
        again = input("\nWould you like to see more 5 lines of raw data? Yes or No\n").lower()
        if again == 'yes':
            print(df.iloc[raw:raw+5])
            raw = raw+5
        elif again == 'no':
            break
        else:
            print("\nInvalid input\n")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
