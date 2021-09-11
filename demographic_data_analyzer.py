import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.groupby('sex').age.mean()[1], 1)
    
    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df['education'].value_counts()['Bachelors']
    total = df['education'].count()
    percentage_bachelors = round(bachelors * 100 / total, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    count_total = len(df.index)
    df_avanced = df.loc[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]
    df_avanced_rich = df_avanced.loc[(df['salary'] == '>50K')]
    count_avanced = len(df_avanced.index)
    count_avanced_rich = len(df_avanced_rich.index)
    higher_education = None
    lower_education = None
    df_lower = df.loc[((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'))]
    df_lower_rich = df_lower.loc[(df['salary'] == '>50K')]
    count_lower = len(df_lower.index)
    count_lower_rich = len(df_lower_rich.index)

    # percentage with salary >50K
    #higher_education_rich = round(count_avanced * 100 / count_total, 1)
    higher_education_rich = round(count_avanced_rich * 100 / count_avanced, 1)
    lower_education_rich = round(count_lower_rich * 100 / count_lower, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df.loc[df['hours-per-week'] == min_work_hours].index)
    num_rich = len(df.loc[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].index)

    rich_percentage = round(num_rich * 100 /num_min_workers, 1)

    # What country has the highest percentage of people that earn >50K?
    df_salary_count = df.groupby('native-country')['salary'].count().to_frame()
    df_rich_count = df.loc[df['salary'] == '>50K'].groupby('native-country')['salary'].count().to_frame()
    df_perc = round(100 * df_rich_count['salary'] / df_salary_count['salary'], 1)
    highest_earning_country = df_perc.idxmax()
    highest_earning_country_percentage = df_perc.max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[df['native-country'] == 'India']['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }



calculate_demographic_data(print_data=True)
