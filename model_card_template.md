# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is made by Nicholas Shewfelt. By way of creation for this model,  I used the RandomForestClassifier from sklearn. All default parameters were used.

## Intended Use
This model is intended to take the census.csv file and predict whether or not an individual make greater than 50 thousand dollars a year based off of the other variables in the individuals row. This model is meant to be used for the Udaicty Machine Learning class only.

## Training Data
The training data us encoded using OneHotEncoding and LabelBinarizer. This is done so we can run our model on this subset of training data. 

The size of the training dataset is 80% of the total dataset.

## Evaluation Data
The evaluation data makes up the remaining 20% of the dataset and is used to measure the models performance against the evaluation data.

## Metrics
Precision: 0.7460 | Recall: 0.6286 | F1: 0.6823

## Ethical Considerations
This model uses US census data that has been made public. There is no PII (Personally Identifiable Information) so therefor since the dataset is public and there is no PII there are also no ethical considerations. 

## Caveats and Recommendations
I recommend to keep in mind that this dataset is used for US citizens and therefor will not be accurate in other countries. 

A caveat is that we must remember that the data is static (meaning we are not adding any new data to the dataset overtime) so therefore the results of this dataset will not age well with time and should be used only as a point in time reference. If this caveat should need to be resolves simply plug in current data and then the model will run on the modern dataset just as well as it does for the census.csv file we currently have.
