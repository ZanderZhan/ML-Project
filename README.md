# GitHub Issue Report Classification

## Environments
1. Python 3.12.10 (Better to install Python 3.10-13! It works correctly on 3.12.10)
2. Install dependencies: pandas, transformers ...

## Dataset
1. `dataset/raw`: contains the original dataset, do not edit these files
2. `dataset/preprocess`: contains the dataset which has been processed by `scripts/preprocessing.by`

To get the train data(Use the method 1, processing script is under changing), 
1. you can simply unzip the `dataset/preprocess/github-labels-top3-803k-train.csv.zip`
2. or you run the script `scripts/preprocessing.ipynb`


## Models
1. SVM
2. ELECTRA

## RQs
 just 3 RQs, cause the project requirements said we just need to define 2-3 RQs, 
 so keep it simple and adequate

- SVM, ELECTRA vs BERT
- change hyperparameters
- change the volume of dataset, see how it affects in each model


## DataSet
- id
- issue_url
- issue_label
- issue_created_at
- issue_author_association
- repository_url
- issue_title
- issue_body


## Preprocessing

### data cleaning
- drop rows with empty/NAN in `issue_body`/`issue_title`
- drop rows which label is not in [bug, enhancement, question]
- concatenate `issue_title` and `issue_body` into one metadata: `issue_data`.
- replace tabs and breaks in the `issue_data` with `spaces`, then remove repeating whitespaces
- tokenize `issue_data` data using `BertTokenizer`
- split data
  - 85% training data, in which 15% is validation data
  - 15% testing data

## Baseline



## AI-Assistance log

1. how does “DistilBERT/BERT” works?
2. what are the imbalance methods
3. how to choose stratified by label
4. What other NLP models are there besides BERT?
5. Tell me more about ELECTRA
6. How do I decide the number of epoch?