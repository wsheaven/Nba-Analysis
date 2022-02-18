import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics


all_seasons = pd.read_csv('all_seasons.csv')

## Split by year 
grouped = all_seasons.groupby(all_seasons.season)
all_seasons19 = grouped.get_group("2018-19")

grouped2 = all_seasons.groupby(all_seasons.season)
all_seasons18 = grouped2.get_group("2017-18")

grouped3 = all_seasons.groupby(all_seasons.season)
all_seasons17 = grouped3.get_group("2016-17")

# print(df_new)

features = []

features.append(all_seasons19.drop(columns = ['Unnamed: 0', 'season','draft_number', 'draft_round', 'player_name', 'team_abbreviation', 'college', 'country', 'draft_year', 'mvp', ]))

features.append(all_seasons18.drop(columns = ['Unnamed: 0', 'season','draft_number', 'draft_round', 'player_name', 'team_abbreviation', 'college', 'country', 'draft_year', 'mvp', ]))

features.append(all_seasons17.drop(columns = ['Unnamed: 0', 'season','draft_number', 'draft_round', 'player_name', 'team_abbreviation', 'college', 'country', 'draft_year', 'mvp', ]))

target = all_seasons.mvp

# target = []

# target.append(all_seasons19.mvp)
# target.append(all_seasons18.mvp)
# target.append(all_seasons17.mvp)

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size = 0.34, random_state = 76)

# Create the classification model
classifier_RF = RandomForestClassifier(n_estimators=1000)

# Train or fit the model 
classifier_RF.fit(x_train, y_train)

y_predicted = classifier_RF.predict(x_test)

#############################################

print(metrics.accuracy_score(y_test, y_predicted))


feature_df = pd.DataFrame({'features':features.columns, 'importance':classifier_RF.feature_importances_})
print(feature_df.sort_values('importance', ascending = False))


