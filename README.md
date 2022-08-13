# BERTRAM on MAGPIE dataset
Use BERTRAM [2] to get single-token embeddings for idioms on the MAGPIE [3] dataset.  
High level objectives:
1. Get single-token embeddings for idioms in the MAGPIE dataset using pretrained BERTRAM model
    - Use sentences from `CC News Corpus` as contexts to obtain the BERTRAM embeddings.  
    - Insert the new tokens of the form `<BERTRAM:IDsomeidiomtokenID>` into `bert-base-uncased` model with these embeddings.
2. Use these embeddings to train a **Sequence Classifier task on MAGPIE dataset** to clasify idiom/literal meanings. Code for this downstream task is already available in [idiom-principle-on-magpie-corpus](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus) repository. Specifically, we only need `./exp_helpers/run_glue_f1_macro.py` file, which has been copied from [here](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus/exp_helpers/run_glue_f1_macro.py).  
    - Note that, while inserting the single-tokens into the MAGPIE dataset, make sure to use the format: `<BERTRAM:ID...ID>`

## Dataset used
### CC News Corpus with MAAGPIE idioms
This data is already prepared [here](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus#variations-of-exp3) for a different task(training a BERT model with single-token representations).  
Below files are taken from above repository:

| File | Taken from |
| ---- | ---------- |
|[all_replace_data.txt](./data/cc_processed/exp3B_1/)| [exp3B_1](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus/experiments/exp3B_1/pretrain_data/)|

### MAGPIE dataset
The dataset [MAGPIE_filtered_split_{*}.jsonl](https://github.com/hslh/magpie-corpus) is used for Idiom Detection using SequenceClassification task.

## Setup
* The BERTRAM model used directly from the original author's work. The submodule `bertram` contains the code for the same.  
* The BERTRAM model available from the original authors has been trained on `bert-base-uncased` model, and is available [here for download](https://github.com/DarshanAdiga/bertram#-pre-trained-models). Hence the same will be used the Sequence Classification task on MAGPIE dataset.
* **Very IMP**: The orignal BERTRAM implementation (`./bertram`) uses the old version of `transformers` library. Hence, a dedicated virtual environment is recommended for these experiments.

## Single Token Representation
The setup is similar as described [here](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus#single-token-representation).  
Both `Option-1` and `Option-2` are to be experimented with in this repository.  

## Experiments
**Steps Followed**:
1. Get the preprocessed CC News corpus containing the **idiom single-tokens**. Prepare the context data from this.  
2. Use this context data to obtain BERTRAM embddings, insert the BERTRAM tokens into another BERT model and save it. **Note**, the model produced with added bertram tokens will have a wrong vocab size in its config. This needs to be corrected.  
3. The model saved by step 2 needs to be converted to a SequenceClassification model before proceeding to the next step.  
4. Get the MAGPIE dataset containing **idiom single-tokens** for sequence classification. **IMP:** Rename the single tokens (`<ID...ID>`) as BERTRAM tokens (`<BERTRAM:ID...ID>`) in train, dev & test datasets.  
5. Train a Sequence Classification task on MAGPIE dataset & record the results.  


| Experiment | Code  | Context Dataset | Single Token Type | Source MAGPIE Dataset | Base Model | No of Examples | BERTRAM Status | Idiom Detection Status | Updated model |
|:-----------|:------|:----------------|:------------------|:---------------|:-----------|:---------------|:---------------|:----------------------|:--------------|
| bt0       | [bt0](./experiments/bt0/) | [all_replace_data.txt](./data/cc_processed/exp3B_1/) | `Option-1` | [exp3B_1/tmp/](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus/tree/3B_retraining/experiments/exp3B_1) | bert-base-uncased | 20 | DONE | Done (4 GPUs) | [bert-base-uncased_option1_with_bertram_SC](./local_models/bert-base-uncased_option1_with_bertram_SC) |
| bt1       | [bt1](./experiments/bt1/) | [all_replace_data.txt](./data/cc_processed/exp3B_1/) | `Option-1` | [exp3B_1/tmp/](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus/tree/3B_retraining/experiments/exp3B_1) | bert-base-uncased | 50 | TODO | TODO | TODO |
| bt2       | [bt2](./experiments/bt2/) | [all_replace_data.txt](./data/cc_processed/exp3B_1/) | `Option-1` | [exp3B_1/tmp/](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus/tree/3B_retraining/experiments/exp3B_1) | bert-base-uncased | 200 | TODO | TODO | TODO |

### Results
The results on **Sequence Classifier task on MAGPIE dataset** task using the BERTRAM embeddings in a BERT model.
| Experiment | Dev Accuracy | Dev F1 | Test Accuracy | Test F1 |
|:-----------|:-------------|:-------|:--------------|:--------|
| bt_0       | 85.47 | 80.59 | 0.0 | 0.0 |
| bt_1       | 0.0 | 0.0 | 0.0 | 0.0 |

## References

[1] D. Phelps, “drsphelps at SemEval-2022 Task 2: Learning idiom representations using BERTRAM.” arXiv, May 25, 2022. Accessed: Jun. 19, 2022. [Online]. Available: http://arxiv.org/abs/2204.02821

[2] T. Schick and H. Schütze, “BERTRAM: Improved Word Embeddings Have Big Impact on Contextualized Model Performance.” arXiv, Apr. 29, 2020. Accessed: Jun. 19, 2022. [Online]. Available: http://arxiv.org/abs/1910.07181

[3] Hessel Haagsma, Johan Bos, and Malvina Nissim. 2020. MAGPIE: A Large Corpus of Potentially Idiomatic Expressions. In Proceedings of the 12th Language Resources and Evaluation Conference, pages 279–287, Marseille, France. European Language Resources Association.
