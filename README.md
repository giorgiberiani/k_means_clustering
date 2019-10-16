# k-Means clustering
```bash
    This is python implementatnion of k-means clustering on radomly generated datasets.
    For data preparation I have used 'Faker' and 'random'. I have used Faker to generate random 
    name, address and date, for other fields I have used pythons 'random' library.
    I am using 'Pandas' to read and manipulation on generated dataset and matplotlib for data visualization.
    To get optimal number of clusters I am using the “elbow” method, and then train model. For training I am using 'scikit-learn' library.
    
    
```

# Installation
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Data preparation
```bash
    To generate dataset run python 'data_preparation.py'
    It will generate datasets and sves as csv in data folder 
```

# Data visualization
```bash
    Run python 'data_visualization.py' for data visualization,
    It will show gender -> expertize mapping for only verified users in percentage and
    daily basis of the  gender -> expertize mapping for Male(Software engineer) Female(Graphics designer)
    for  the second month(October 1-30)
```

# k-means
```bash
    Run python 'k_means_clustering.py' to train model.
    At first it will show graph generated with the “elbow” method, and then trains model on generated dataset.
```
