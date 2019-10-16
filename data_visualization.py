import matplotlib.pyplot as plt

import pandas as pd


def gender_expertize_mapping(data_source_1, data_source_2):
    '''

    :param data_source_1: dataframe
    :param data_source_2: dataframe
    :return:
    '''
    verified = data_source_2[data_source_2['status'] == 'verified']
    verified_users = data_source_1[(data_source_1['userID'].isin(verified['userID']))]
    verified_females = verified_users[(verified_users['gender'] == 'female')]
    verified_males = verified_users[(verified_users['gender'] == 'male')]
    female_percentage = verified_females.expertize.value_counts(normalize=True).sort_index().mul(100).round(1).astype(
        str) + ' %'
    male_percentage = verified_males.expertize.value_counts(normalize=True).sort_index().mul(100).round(1).astype(
        str) + ' %'

    expertize = ['graphics designer', 'other', 'software engineer']
    percentage_df = pd.DataFrame({'expertize': expertize, 'male': male_percentage, 'female': female_percentage})
    plot_percentage_table(percentage_df)

def plot_percentage_table(df):
    fig, ax = plt.subplots()

    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    fig.tight_layout()
    plt.show()


def daily_basis(data_source_1, data_source_2):
    october_users = data_source_2[data_source_2['registration_time'] >= '2019-10-01']
    _october_users = data_source_1[(data_source_1['userID'].isin(october_users['userID']))]
    _october_users.insert(5, "registration_time", october_users.iloc[:, -1].map(lambda date: date.split('-')[-1]), True)
    male_software_engineer = _october_users[
        (_october_users['gender'] == 'male') & (_october_users['expertize'] == 'software engineer')]
    female_graphics_designer = _october_users[
        (_october_users['gender'] == 'female') & (_october_users['expertize'] == 'graphics designer')]

    male_software_engineer_daily_basis = male_software_engineer[
        'registration_time'].value_counts().sort_index().to_frame()
    female_graphics_designer_daily_basis = female_graphics_designer[
        'registration_time'].value_counts().sort_index().to_frame()
    plot_daily_basis(male_software_engineer_daily_basis, female_graphics_designer_daily_basis)


def plot_daily_basis(male_software_engineer_daily_basis, female_graphics_designer_daily_basis):
    '''
    Plots daily basis increment graph of the  gender -> expertize mapping for Male(Software engineer)
    Female(Graphics designer) for  the second month(October 1-30)
    :param male_software_engineer_daily_basis: dataframe
    :param female_graphics_designer_daily_basis: dataframe
    :return:
    '''
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('daily basis')
    ax1.plot(list(range(1, 30)), male_software_engineer_daily_basis.iloc[:, 0], label='Male(Software engineer) ')
    ax1.plot(list(range(1, 30)), female_graphics_designer_daily_basis.iloc[:, 0], label='Female(Graphics designer)')
    plt.legend(loc='upper left');
    plt.show()


if __name__ == "__main__":
    data_source_1 = pd.read_csv('data/datasource1.csv')
    data_source_2 = pd.read_csv('data/datasource2.csv')
    gender_expertize_mapping(data_source_1, data_source_2)
    daily_basis(data_source_1, data_source_2)
