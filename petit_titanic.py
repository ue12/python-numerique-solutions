import pandas as pd

filename = "petit-titanic.csv"

# comme le .csv ne contient pas le header qui indique
# le nom des colonnes, il nous faut le fournir à read_csv

columns = ['PassengerId', 'Survived', 'Pclass',
           'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',
           'Fare', 'Cabin', 'Embarked']

petit_df = pd.read_csv(filename, names=columns, sep=";", index_col='PassengerId')
