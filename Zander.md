## Commands

- Clear the metadata keys(added by JetBrains IDEs)

```terminaloutput
jupyter nbconvert \
    --ClearOutputPreprocessor.enabled=True \
    --ClearMetadataPreprocessor.enabled=True \
    --TagRemovePreprocessor.enabled=True \
    --ClearMarkDownMetadataPreprocessor.enabled=True \
    --inplace BERT.ipynb
```

- Using nohup to run the jupyter in the background
```terminaloutput
nohup jupyter nbconvert --to notebook --execute BERT.ipynb --output BERT_executed.ipynb > bert.txt 2>&1 &
```

- Kill the nohup process
```terminaloutput
ps aux | grep nbconvert
kill [process]
```

## BERT
```terminaloutput
jupyter nbconvert \
    --ClearOutputPreprocessor.enabled=True \
    --ClearMetadataPreprocessor.enabled=True \
    --TagRemovePreprocessor.enabled=True \
    --ClearMarkDownMetadataPreprocessor.enabled=True \
    --inplace BERT.ipynb
```
```terminaloutput
nohup jupyter nbconvert --to notebook --execute BERT.ipynb --output BERT_executed.ipynb > bert.txt 2>&1 &
```

### ELECTRA
```terminaloutput
jupyter nbconvert \
    --ClearOutputPreprocessor.enabled=True \
    --ClearMetadataPreprocessor.enabled=True \
    --TagRemovePreprocessor.enabled=True \
    --ClearMarkDownMetadataPreprocessor.enabled=True \
    --inplace ELECTRA.ipynb
```
```terminaloutput
nohup jupyter nbconvert --to notebook --execute ELECTRA.ipynb --output ELECTRA_executed.ipynb > electra.txt 2>&1 &
```

### FUNNEL
```terminaloutput
jupyter nbconvert \
    --ClearOutputPreprocessor.enabled=True \
    --ClearMetadataPreprocessor.enabled=True \
    --TagRemovePreprocessor.enabled=True \
    --ClearMarkDownMetadataPreprocessor.enabled=True \
    --inplace FUNNEL.ipynb
```
```terminaloutput
nohup jupyter nbconvert --to notebook --execute FUNNEL.ipynb --output FUNNEL_executed.ipynb > funnel.txt 2>&1 &
```

### GPT2
```terminaloutput
jupyter nbconvert \
    --ClearOutputPreprocessor.enabled=True \
    --ClearMetadataPreprocessor.enabled=True \
    --TagRemovePreprocessor.enabled=True \
    --ClearMarkDownMetadataPreprocessor.enabled=True \
    --inplace GPT2.ipynb
```
```terminaloutput
nohup jupyter nbconvert --to notebook --execute GPT2.ipynb --output GPT2_executed.ipynb > gpt2.txt 2>&1 &
```