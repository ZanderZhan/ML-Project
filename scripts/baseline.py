import pandas as pd
from transformers import BertTokenizer


# load data from preprocess dataset
data = 'github-labels-top3-803k-train'
data_set = pd.read_csv(f'../dataset/preprocess/{data}.csv')

# tokenize `issue_data` data using `BertTokenizer`
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
encoded_data_train = tokenizer.batch_encode_plus(
    data_set.issue_data.values,
    add_special_tokens=True,
    return_attention_mask=True,
    padding='longest',
    truncation=True,
    return_tensors='pt'
)

input_ids_train = encoded_data_train['input_ids']
attention_masks_train = encoded_data_train['attention_mask']