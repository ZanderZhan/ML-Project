# ML-Project

## Models
1. SVM
2. ELECTRA


## RQs

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

1. What other NLP models are there besides BERT?
2. Tell me more about ELECTRA