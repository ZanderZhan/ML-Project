# GitHub Issue Report Classification

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
- drop rows with empty `issue_body`
- drop rows which label is not in [bug, enhancement, question]
- concatenate `issue_title` and `issue_body` into one metadata: `issue`.
- replace tabs and spaces in the `issue` with `spaces`, then remove repeating whitespaces
- tokenize `issue` data using `BertTokenizer`


## Baseline


## AI-Assistance log

1. how does “DistilBERT/BERT” works?
2. what are the imbalance methods
3. how to choose stratified by label
4. What other NLP models are there besides BERT?
5. Tell me more about ELECTRA