import unittest
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class TestDimensionalityReduction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the dataset
        cls.df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
        cls.X, cls.y = cls.df_wine.iloc[:, 1:].values, cls.df_wine.iloc[:, 0].values
        cls.X_train, cls.X_test, cls.y_train, cls.y_test = train_test_split(cls.X, cls.y, test_size=0.3, stratify=cls.y, random_state=0)
        
        # Standardize the features
        cls.sc = StandardScaler()
        cls.X_train_std = cls.sc.fit_transform(cls.X_train)
        cls.X_test_std = cls.sc.transform(cls.X_test)

    def test_pca_variance_explained(self):
        # Perform PCA
        pca = PCA(n_components=2)
        X_train_pca = pca.fit_transform(self.X_train_std)
        X_test_pca = pca.transform(self.X_test_std)
        
        # Check the explained variance ratio
        explained_variance_ratio = pca.explained_variance_ratio_
        self.assertAlmostEqual(explained_variance_ratio[0], 0.36951469, places=5)
        self.assertAlmostEqual(explained_variance_ratio[1], 0.18434927, places=5)

    def test_pca_transformed_shape(self):
        # Perform PCA
        pca = PCA(n_components=2)
        X_train_pca = pca.fit_transform(self.X_train_std)
        X_test_pca = pca.transform(self.X_test_std)
        
        # Check the shape of the transformed data
        self.assertEqual(X_train_pca.shape, (124, 2))
        self.assertEqual(X_test_pca.shape, (54, 2))

    def test_pca_transformed_values(self):
        # Perform PCA
        pca = PCA(n_components=2)
        X_train_pca = pca.fit_transform(self.X_train_std)
        X_test_pca = pca.transform(self.X_test_std)
        
        # Check the first transformed value
        np.testing.assert_array_almost_equal(X_train_pca[0], [2.38299011, 0.45458499], decimal=5)

if __name__ == '__main__':
    unittest.main()
