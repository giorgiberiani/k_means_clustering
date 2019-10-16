import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def preprocess_data(data_source_1, data_source_2):
    '''
    Removs redundant fields from dataset and encodes categorical values
    :param data_source_1: dataframe
    :param data_source_2: dataframe
    :return: numpy.ndarray -- Preprocessed data
    '''
    data_source_1 = data_source_1.iloc[:, 3:]
    data_source_2 = data_source_2.iloc[:, 3:-1]

    train_data = pd.concat([data_source_1, data_source_2], axis=1).values
    label_encoder = LabelEncoder()

    one_hot_encoder = OneHotEncoder(categories='auto')
    train_data[:, 0] = label_encoder.fit_transform(train_data[:, 0])
    train_data[:, 1] = label_encoder.fit_transform(train_data[:, 1])
    train_data[:, 2] = label_encoder.fit_transform(train_data[:, 2])
    train_data = one_hot_encoder.fit_transform(train_data).toarray()
    return train_data

def k_means_clustering(train_data):
    '''
    Shows the “elbow” method output and trains the model
    :param train_data: numpy.ndarray -- Preprocessed data
    :return: numpy.ndarray -- trained model
    '''

    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(train_data)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

    # Fitting K-Means to the dataset
    kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
    kmeans = kmeans.fit_predict(train_data)
    return kmeans







if __name__ == '__main__':

    data_source_1 = pd.read_csv('data/datasource1.csv')
    data_source_2 = pd.read_csv('data/datasource2.csv')

    train_data = preprocess_data(data_source_1, data_source_2)
    k_means_clustering(train_data)


