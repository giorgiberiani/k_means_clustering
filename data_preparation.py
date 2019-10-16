from faker import Faker
import pandas as pd
import string
import datetime
import random


def generate_datasource1(number_of_rows, faker):
    user_id = list(range(number_of_rows))
    adrerss = []
    gender = []
    expertize = []
    fullname = []
    for i in range(number_of_rows):
        gender.append(random.choice(['male', 'female']))
        expertize.append(random.choice(['software engineer', 'graphics designer', 'other']))
        adrerss.append(faker.address())
        fullname.append(faker.name())
    random_data = {'userID': user_id, 'fullname': fullname, 'adress': adrerss, 'gender': gender,
                   'expertize': expertize}

    save_to_csv('data/datasource1.csv', random_data)


def generate_datasource2(number_of_rows, faker):
    user_id = list(range(number_of_rows))
    user_name = []
    password = []
    status = []
    registration_time = []
    for i in range(number_of_rows):
        status.append(random.choice(['verified', 'unverified']))
        registration_time.append(random_date(faker))
        password.append(random_password())
        user_name.append(faker.name())
    random_data = {'userID': user_id, 'username': user_name, 'password': password, 'status': status,
                   'registration_time': registration_time}
    save_to_csv('data/datasource2.csv', random_data)


def save_to_csv(file_name, data):
    random_data = pd.DataFrame(data)
    random_data.to_csv(file_name, index=False)


def random_password(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def random_date(faker):
    start_date = datetime.datetime.strptime('01092019', '%d%m%Y').date()
    end_date = datetime.datetime.strptime('30102019', '%d%m%Y').date()
    return faker.date_between(start_date=start_date, end_date=end_date)


if __name__ == '__main__':
    faker = Faker()
    number_of_rows = 25000
    generate_datasource1(number_of_rows, faker)
    generate_datasource2(number_of_rows, faker)
