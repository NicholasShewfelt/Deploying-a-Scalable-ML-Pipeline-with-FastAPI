import pytest
# TODO: add necessary import
import os
import sys
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin

root_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root_dir)

from ml.model import train_model, compute_model_metrics, inference

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # add description for the first test
    Test pipeline of training model
    """
    # Your code here
    X = np.random.rand(20, 5)
    y = np.random.randint(2, size=20)
    model = train_model(X, y)
    assert isinstance(model, BaseEstimator) and isinstance(
        model, ClassifierMixin)
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # add description for the second test
    Test compute_model_metrics
    """
    # Your code here
    y_true, y_preds = [1, 1, 0], [0, 1, 1]
    precision, recall, fbeta = compute_model_metrics(y_true, y_preds)
    assert precision is not None
    assert recall is not None
    assert fbeta is not None
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    Test inference of model
    """
    # Your code here
    X = np.random.rand(20, 5)
    y = np.random.randint(2, size=20)
    model = train_model(X, y)
    y_preds = inference(model, X)
    assert y.shape == y_preds.shape
    pass
