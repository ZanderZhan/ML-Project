import pandas as pd

# load dataset from csv
dataset = 'github-labels-top3-803k-train'
raw_data_set = pd.read_csv(f'../dataset/raw/{dataset}.csv')
print(raw_data_set.count())
# print(raw_data_set.issue_label)

# start processing the data

# 1. drop rows with empty/NAN in `issue_body`/`issue_title`
# empty_issue_body_data = raw_data_set[raw_data_set.issue_body.str.strip() == '']
# print(empty_issue_body_data)
raw_data_set = raw_data_set.dropna(subset=['issue_title', 'issue_body'])
raw_data_set = raw_data_set[raw_data_set.issue_body.str.strip() != '']
# print(raw_data_set.count())

# 2. drop rows which label is not in [bug, enhancement, question]
labels = ['bug', 'enhancement', 'question']
# label_not_include_data = raw_data_set[~raw_data_set.issue_label.isin(labels)]
# print(label_not_include_data)
raw_data_set = raw_data_set[raw_data_set.issue_label.isin(labels)]

# 3. concatenate `issue_title` and `issue_body` into one metadata: `issue`.
raw_data_set['issue_data'] = raw_data_set.issue_title + " " + raw_data_set.issue_body
# print(raw_data_set.count())
raw_data_set = raw_data_set.drop('issue_title', axis=1)
raw_data_set = raw_data_set.drop('issue_body', axis=1)
# print(raw_data_set.count())


# 4. replace tabs and breaks in the `issue_data` with `spaces`, then remove repeating whitespaces
# print(raw_data_set.issue_data.values[0])
raw_data_set.issue_data = raw_data_set.issue_data.replace(r'[\t\n\r ]+', ' ', regex=True)
# print(raw_data_set.issue_data.values[0])

# 5. output the dataset into file without tokenizing
raw_data_set.to_csv(f'../dataset/preprocess/{dataset}.csv')