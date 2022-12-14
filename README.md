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
1. Get the preprocessed CC News corpus containing the **idiom single-tokens**. Prepare the context data from this (Mostly, you only need to prepare this once). Use the script `prepare_data.sh` to do this.  
2. Use this context data to obtain BERTRAM embddings, insert the BERTRAM tokens into another BERT model and save it. Use the script `train_and_update_bertram_embeddings_hpc.sh` to do this. **Note**, the model produced with added bertram tokens will have a wrong vocab size in its config. This needs to be corrected.  
3. The model saved by step 2 needs to be converted to a SequenceClassification model before proceeding to the next step. Use the notebook `exp_helpers/MLM_to_SeqClass_model_converter.ipynb` to do this.  
4. Get the MAGPIE dataset containing **idiom single-tokens** for sequence classification. **IMP:** Rename the single tokens (`<ID...ID>`) as BERTRAM tokens (`<BERTRAM:ID...ID>`) in train, dev & test datasets. Use the script `replace_with_bertram_tokens.sh` to do this. (Mostly, you only need to prepare this once).  
5. Train a Sequence Classification task on MAGPIE dataset & record the results. Use `hpc.sh` to do this.  


| Experiment | Code  | Context Dataset | Single Token Type | Source MAGPIE Dataset | Base Model | No of Examples | BERTRAM Status | Idiom Detection Status | Updated model |
|:-----------|:------|:----------------|:------------------|:---------------|:-----------|:---------------|:---------------|:----------------------|:--------------|
| bt0       | [bt0](./experiments/bt0/) | [all_replace_data.txt](./data/cc_processed/exp3B_1/) | `Option-1` | [exp3B_1/tmp/](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus/tree/3B_retraining/experiments/exp3B_1) | bert-base-uncased | 20 | DONE (Took 00:01:39) | Done (4 GPUs) | [bert-base-uncased_option1_with_bertram_bt0_SC](./local_models/bert-base-uncased_option1_with_bertram_bt0_SC) |
| bt1       | [bt1](./experiments/bt1/) | *same as bt0* | `Option-1` | *same as bt0* | bert-base-uncased | 50 | DONE (Took 00:07:38) | Done (4 GPUs) | [bert-base-uncased_option1_with_bertram_bt1_SC](./local_models/bert-base-uncased_option1_with_bertram_bt1_SC) |
| bt2       | [bt2](./experiments/bt2/) | *same as bt0* | `Option-1` | *same as bt0* | bert-base-uncased | 200 | DONE (Took 00:18:23) | Done (RTX5000 x 1) | [bert-base-uncased_option1_with_bertram_bt2_SC](./local_models/bert-base-uncased_option1_with_bertram_bt2_SC) |

### Results
The results on **Sequence Classifier task on MAGPIE dataset** task using the BERTRAM embeddings in a BERT model.
| Experiment | Dev Accuracy | Dev F1 | Test Accuracy | Test F1 |
|:-----------|:-------------|:-------|:--------------|:--------|
| bt_0       | 85.47 | 80.59 | 83.86 | 80.47 |
| bt_1       | 86.67 | 82.06 | 83.8 | 79.6 |
| bt_2       | 84.73 | 80.59 | 84.73 | 80.59 |

## Error Analysis & Study
NOTE: Refer to [Error Analysis & Study](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus#error-analysis-study). All the implementations are copied from there.

The precomputed grouping of PIEs has been copied from `idiom-principle-on-magpie-corpus` repository and is available at [data/PIE_segregation](./data/PIE_segregation/).

The classification reports has been copied from `idiom-principle-on-magpie-corpus` repository and is available at [exp_helpers/produce_test_results.py](./exp_helpers/produce_test_results.py).

The classification reports (both overall and segreated) is generated for the best experiment `bt_2` (folder named `bt2`).

## References

[1] D. Phelps, ???drsphelps at SemEval-2022 Task 2: Learning idiom representations using BERTRAM.??? arXiv, May 25, 2022. Accessed: Jun. 19, 2022. [Online]. Available: http://arxiv.org/abs/2204.02821

[2] T. Schick and H. Sch??tze, ???BERTRAM: Improved Word Embeddings Have Big Impact on Contextualized Model Performance.??? arXiv, Apr. 29, 2020. Accessed: Jun. 19, 2022. [Online]. Available: http://arxiv.org/abs/1910.07181

[3] Hessel Haagsma, Johan Bos, and Malvina Nissim. 2020. MAGPIE: A Large Corpus of Potentially Idiomatic Expressions. In Proceedings of the 12th Language Resources and Evaluation Conference, pages 279???287, Marseille, France. European Language Resources Association.
