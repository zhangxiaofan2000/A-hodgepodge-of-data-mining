# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""##### Helper Funtion 1 : Drop Columns"""



class HousingPricePrediction:
    def __init__(self, train_file, test_file):
        self.df_train = pd.read_csv(train_file)
        self.df_test = pd.read_csv(test_file)


    def drop_columns(self, df, column):
        return df.drop(columns=column, inplace=True, axis=1)

    """##### Helper Funtion 2 : Missing Value Summary"""

    def find_missing(self, df):
        total_missing = df.isnull().sum().sort_values(ascending=False)
        pct_missing = (df.isnull().sum() / len(df.index)).sort_values(ascending=False)
        missing_data_summary = pd.concat([total_missing, pct_missing],
                                         axis=1, keys=['Total Missing Records', 'Percentage'])
        return missing_data_summary.head(30)

    def combine_columns(self, column1, column2, output_column):
        output_column = column1 + column2
        return output_column

    def change_to_numeric_train(self, column, values, nums):
        self.df_train[column] = self.df_train[column].replace(values, nums)

    def change_to_numeric_test(self, column, values, nums):
        self.df_test[column] = self.df_test[column].replace(values, nums)
    def head(self):
        return self.df_train.head()
    def info(self):
        return self.df_train.info()

    def find_missing(self):
        return self.find_missing(self.df_train)

    def data_cleaning(self):
        self.drop_columns(self.df_train,
                          ['Id', 'PID', 'Pool QC', 'Garage Yr Blt', 'Misc Feature', 'Alley', 'Fence', 'Fireplace Qu'])

        self.drop_columns(self.df_test, ['PID', 'Pool QC', 'Misc Feature', 'Garage Yr Blt', 'Alley', 'Fence', 'Fireplace Qu'])

        self.df_train.info()

        self.df_train['FloorSqft'] = self.df_train['1st Flr SF'] + self.df_train['2nd Flr SF']

        self.df_test['FloorSqft'] = self.df_test['1st Flr SF'] + self.df_test['2nd Flr SF']

        self.df_train['Half Bath'].replace({1: 0.5, 2: 1})
        self.df_train['Bsmt Half Bath'].replace({1: 0.5, 2: 1})
        self.df_train['Total Bath'] = self.df_train['Half Bath'] + self.df_train['Bsmt Half Bath'] + self.df_train['Bsmt Full Bath'] + \
                                 self.df_train[
                                     'Full Bath']

        self.df_test['Half Bath'].replace({1: 0.5, 2: 1})
        self.df_test['Bsmt Half Bath'].replace({1: 0.5, 2: 1})
        self.df_test['Total Bath'] = self.df_test['Half Bath'] + self.df_test['Bsmt Half Bath'] + self.df_test['Bsmt Full Bath'] + self.df_test[
            'Full Bath']

        self.df_train['total age'] = self.df_train['Yr Sold'] - self.df_train['Year Built']
        self.df_train['remod age'] = self.df_train['Yr Sold'] - self.df_train['Year Remod/Add']

        self.df_test['total age'] = self.df_test['Yr Sold'] - self.df_test['Year Built']
        self.df_test['remod age'] = self.df_test['Yr Sold'] - self.df_test['Year Remod/Add']

        self.drop_columns(self.df_train,
                          ['1st Flr SF', '2nd Flr SF', 'Bsmt Full Bath', 'Bsmt Half Bath', 'Full Bath', 'Half Bath',
                      'Mo Sold',
                      'Year Built', 'Yr Sold', 'Year Remod/Add'])

        self.drop_columns(self.df_test,
                          ['1st Flr SF', '2nd Flr SF', 'Bsmt Full Bath', 'Bsmt Half Bath', 'Full Bath', 'Half Bath',
                      'Mo Sold',
                      'Year Built', 'Yr Sold', 'Year Remod/Add'])

        num_columns = [i for i in self.df_train.columns if self.df_train.dtypes[i] != 'object']
        num_columns.remove('SalePrice')

        self.change_to_numeric_train('BsmtFin Type 1', ['Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ'], range(1, 7))
        self.df_train['BsmtFin Type 1'].fillna(0, inplace=True)

        self.change_to_numeric_train('BsmtFin Type 2', ['Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ'],
                                     range(1, 7))
        self.df_train['BsmtFin Type 2'].fillna(0, inplace=True)

        self.change_to_numeric_train('Bsmt Exposure', ['No', 'Mn', 'Av', 'Gd'], range(1, 5))
        self.df_train['Bsmt Exposure'].fillna(0, inplace=True)

        self.change_to_numeric_train('Bsmt Cond', ['Po', 'Fa', 'TA', 'Gd', 'Ex'], range(1, 6))
        self.df_train['Bsmt Cond'].fillna(0, inplace=True)

        self.change_to_numeric_train('Bsmt Qual', ['Po', 'Fa', 'TA', 'Gd', 'Ex'], range(1, 6))
        self.df_train['Bsmt Qual'].fillna(0, inplace=True)

        self.change_to_numeric_test('BsmtFin Type 1', ['Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ'], range(1, 7))
        self.df_test['BsmtFin Type 1'].fillna(0, inplace=True)

        self.change_to_numeric_test('BsmtFin Type 2', ['Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ'],
                                    range(1, 7))
        self.df_test['BsmtFin Type 2'].fillna(0, inplace=True)

        self.change_to_numeric_test('Bsmt Exposure', ['No', 'Mn', 'Av', 'Gd'], range(1, 5))
        self.df_test['Bsmt Exposure'].fillna(0, inplace=True)

        self.change_to_numeric_test('Bsmt Cond', ['Po', 'Fa', 'TA', 'Gd', 'Ex'], range(1, 6))
        self.df_test['Bsmt Cond'].fillna(0, inplace=True)

        self.change_to_numeric_test('Bsmt Qual', ['Po', 'Fa', 'TA', 'Gd', 'Ex'], range(1, 6))
        self.df_test['Bsmt Qual'].fillna(0, inplace=True)

        self.df_train['Lot Frontage'].fillna(0.0, inplace=True)
        self.df_train['Mas Vnr Type'].fillna('None', inplace=True)
        self.df_train['Mas Vnr Area'].fillna(0.0, inplace=True)

        self.df_train['Garage Finish'] = self.df_train['Garage Finish'].replace(['Fin', 'RFn', 'Unf'], [3, 2, 1])
        self.df_train['Garage Finish'].fillna(0, inplace=True)

        self.change_to_numeric_train('Garage Qual', ['Ex', 'Gd', 'TA', 'Fa', 'Po'], [5, 4, 3, 2, 1])
        self.df_train['Garage Qual'].fillna(0, inplace=True)

        self.change_to_numeric_train('Garage Cond', ['Ex', 'Gd', 'TA', 'Fa', 'Po'], [5, 4, 3, 2, 1])
        self.df_train['Garage Cond'].fillna(0, inplace=True)

        self.df_train['Garage Type'].fillna('None', inplace=True)

        self.df_test['Lot Frontage'].fillna(0.0, inplace=True)
        self.df_test['Mas Vnr Type'].fillna('None', inplace=True)
        self.df_test['Mas Vnr Area'].fillna(0.0, inplace=True)

        self.df_test['Garage Finish'] = self.df_test['Garage Finish'].replace(['Fin', 'RFn', 'Unf'], [3, 2, 1])
        self.df_test['Garage Finish'].fillna(0, inplace=True)

        self.change_to_numeric_test('Garage Qual', ['Ex', 'Gd', 'TA', 'Fa', 'Po'], [5, 4, 3, 2, 1])
        self.df_test['Garage Qual'].fillna(0, inplace=True)

        self.change_to_numeric_test('Garage Cond', ['Ex', 'Gd', 'TA', 'Fa', 'Po'], [5, 4, 3, 2, 1])
        self.df_test['Garage Cond'].fillna(0, inplace=True)

        self.df_test['Garage Type'].fillna('None', inplace=True)

        self.df_train.dropna(subset=['Total Bath', 'Garage Area', 'Garage Cars'], inplace=True)

        self.df_train['Exter Qual'].unique()

        condition_rank = {'Ex': 6, 'Gd': 5, 'TA': 4, 'Fa': 3, 'Po': 2, 'NA': 1}


        self.df_train['Kitchen Qual'] = self.df_train['Kitchen Qual'].map(condition_rank)

        self.df_test['Kitchen Qual'] = self.df_test['Kitchen Qual'].map(condition_rank)

        self.df_train['Exter Qual'] = self.df_train['Exter Qual'].map(condition_rank)

        self.df_test['Exter Qual'] = self.df_test['Exter Qual'].map(condition_rank)

        self.df_train['Exter Cond'] = self.df_train['Exter Cond'].map(condition_rank)

        self.df_test['Exter Cond'] = self.df_test['Exter Cond'].map(condition_rank)

        cat_columns = self.df_train.select_dtypes(include=object).keys()

        num_columns = [i for i in self.df_train.columns if self.df_train.dtypes[i] != 'object']
        num_columns.remove('SalePrice')

        num_columns = [i for i in self.df_train.columns if self.df_train.dtypes[i] != 'object']
        num_columns.remove('SalePrice')

        len(num_columns)

        list_remove = []

        print(list_remove)

        for ele in list_remove:
            num_columns.remove(ele)

        len(num_columns)

        self.df_train.info()

        X = self.df_train[num_columns]
        y = self.df_train['SalePrice']
        return X, y

    def plot(self):
        corr_matrix = self.df_train.corr()
        corr_matrix['SalePrice'].sort_values(ascending=False)


        plt.figure(figsize=(2, 24))
        sns.heatmap(self.df_train.corr()[['SalePrice']].sort_values('SalePrice', ascending=False),
                    annot=True);
        plt.show()


    def hist_scatter(self, df, feature):
        plt.figure(figsize=(25, 10))

        plt.subplot(1, 2, 1)
        sns.histplot(data=df[feature], x=df[feature], color='#ade8f4', kde=False, bins=8)
        plt.axvline(df[feature].mean(), color='r', linestyle='dashed', linewidth=5)
        plt.title(f'{feature} Distribution', size=15)

        plt.subplot(1, 2, 2)
        sns.regplot(x=df['SalePrice'], y=df[feature], color='#0077b6', line_kws={"color": "r"})
        plt.title(f'{feature} vs Sale Price', size=15)
        plt.xlabel('Sale Price', size=12)
        plt.ylabel(f'{feature}', size=12)
        plt.show()
    def hist_scatter_all(self):
        # Create a list of column names
        columns = ['Overall Qual', 'FloorSqft', 'Gr Liv Area', 'Garage Area',
                   'Garage Cars', 'Total Bsmt SF', 'Total Bath', 'Lot Area']

        for column in columns:
            self.hist_scatter(self.df_train, column)




if __name__ == '__main__':

    HPP = HousingPricePrediction(r".\data\housingprice\train.csv",r".\data\housingprice\test.csv")
    X,y =HPP.data_cleaning()
    HPP.plot()
    HPP.hist_scatter_all()


    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)
    X_train.head()

    from sklearn.model_selection import cross_val_score
    cross_val_score(LinearRegression(), X_train, y_train, cv=5).mean()

    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr.score(X_train, y_train)
    lr.score(X_test, y_test)


    print(lr.score(X_train, y_train),lr.score(X_test, y_test))


