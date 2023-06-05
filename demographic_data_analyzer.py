import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    print(df.info)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    print('RACE COUNTS', race_count)

    # What is the average age of men?
    
    sex = df['sex'].value_counts()
    print('sex', sex)
    men = df.loc[df['sex'] == 'Male', 'age'] 
    print('Male', men)
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)
    print('Average Age Men', average_age_men)
    # What is the percentage of people who have a Bachelor's degree?
    bachelor = df['education'] == 'Bachelors'
    print ('BACHELORS', bachelor)
    bachelor_total = df.loc[bachelor].value_counts().sum()
    educated = df['education'].value_counts().sum()
    percentage_bachelors = round(bachelor_total * 100 / educated, 1)
    print('PERCENTAGE BACHELORS', percentage_bachelors)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    master = df['education'] == 'Masters'
    doctor = df['education'] == 'Doctorate'
    higher_education = bachelor | master | doctor
    print('HI ED GROUP', higher_education)
  
    lower_education = (df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')

    # percentage with salary >50K
    hi_ed_rich = df.loc[higher_education & (df['salary'] == '>50K')].value_counts().sum()
    hi_ed_total = df.loc[bachelor | master | doctor].value_counts().sum()
    
    print('HI ED RICH', hi_ed_rich)
    higher_education_rich = round(hi_ed_rich * 100 / hi_ed_total, 1)

    lo_ed_rich = df.loc[lower_education & (df['salary'] == '>50K')].value_counts().sum()
    lo_ed_total = df.loc[lower_education].value_counts().sum()
    print('LO ED RICH', lo_ed_rich)
    lower_education_rich = round(lo_ed_rich * 100 / lo_ed_total, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    
    min_work_hours = df['hours-per-week'].value_counts().min()
    print('MIN WORK HOURS', min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == 1 & (df['salary'] == '>50K')].value_counts().sum()
    print('MIN WORKERS RICH', num_min_workers )
    rich_percentage = num_min_workers * 100 / df.loc[df['hours-per-week'] == 1].value_counts().sum()
    print('RICH PERCENTAGE', rich_percentage)

    # What country has the highest percentage of people that earn >50K?
    rich_ppl_by_country =  df.loc[df['salary'] == '>50K', 'native-country'].value_counts()
    country_population = df['native-country'].value_counts()
    print('POPULATION BY COUNTRY', country_population)
    print('RICH BY COUNTRY', rich_ppl_by_country)
    rich_percent_by_country = round(rich_ppl_by_country * 100 / country_population, 2)
    print('% RICH BY COUNTRY', rich_percent_by_country)
    highest_earning_country = rich_percent_by_country.idxmax()
    print('RICHEST COUNTRY', highest_earning_country)
    highest_earning_country_percentage = round(rich_percent_by_country.max(), 1)
    print('HIGHEST %RICH', highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    india = df['native-country'] == 'India'
    india_rich = df.loc[india & (df['salary'] == '>50K'), 'occupation'].value_counts()
    print('INDIA RICH', india_rich)
    top_IN_occupation = india_rich.idxmax()
    print('TOP OCCUPATION', top_IN_occupation)

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
