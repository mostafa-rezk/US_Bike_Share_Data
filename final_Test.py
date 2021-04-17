import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    try:
        city = input("Enter your city: ")
        month = int(input('Enter month '))
        day = int(input('Enter day '))
        city = city.lower()
        if city in CITY_DATA:
            final_city_file = CITY_DATA[city]
            return [final_city_file, month, day]
        else:
            raise NameError("city name : " + city + " is not exist")

    except Exception as e:
        print(str(e))
        pass


def load_data(city, month, day):
    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    df = df[df['month'] == month]
    df = df[df['day_of_week'] == day]

    print(df)

    return df


def time_stats(df):

    start_time = time.time()
    popular_month = df['month'].mode()[0]
    popular_week = df['day_of_week'].mode()[0]
    popular_hour = df['hour'].mode()[0]
    print(popular_month)
    print(popular_week)
    print(popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    start_time = time.time()
    popular_start_station = df['Start Time'].mode()[0]
    popular_end_station = df['End Time'].mode()[0]
    popular_trip_duration = df['Trip Duration'].mode()[0]
    print(popular_start_station)
    print(popular_end_station)
    print(popular_trip_duration)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    start_time = time.time()
    total_travel_time = df['Trip Duration'].sum()
    mean_time = df['Trip Duration'].mean()
    print(total_travel_time)
    print(mean_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    start_time = time.time()
    user_type = df['User Type'].value_counts()
    gender = df['Gender'].value_counts()
    earlist_birthday = df['Birth Year'].min()
    most_recent = df['Birth Year'].max()
    most_common = df['Birth Year'].mode()
    print(user_type)
    print(gender)
    print(earlist_birthday)
    print(most_recent)
    print(most_common)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


userInputs = get_filters()
print(userInputs)
if isinstance(userInputs, list):
    res = load_data(userInputs[0], userInputs[1], userInputs[2])
    time_stats(res)
    station_stats(res)
    trip_duration_stats(res)
