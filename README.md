# BERTRAM on MAGPIE dataset
Use BERTRAM [2] to get single-token embeddings for idioms on the MAGPIE [3] dataset.
High level objectives:
1. Get single-token embeddings for idioms in the MAGPIE dataset using pretrained BERTRAM model
    - Use sentences from `CC News Corpus` as contexts to obtain the BERTRAM embeddings.  
    - Insert the new tokens of the form `<BERTRAM:IDsomeidiomtokenID>` into `bert-base-uncased` model with these embeddings.
2. Use these embeddings to train a **Sequence Classifier task on MAGPIE dataset** to clasify idiom/literal meanings. Code for this downstream task is already available in [idiom-principle-on-magpie-corpus](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus) repository. 

## Dataset used
Original dataset is available: [MAGPIE_filtered_split_{*}.jsonl](https://github.com/hslh/magpie-corpus).

### CC News Corpus with MAAGPIE idioms
This data is already prepared [here](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus#variations-of-exp3) for a different task(training a BERT model with single-token representations).  
Below files are taken from above repository:

| File | Taken from |
| ---- | ---------- |
|[all_replace_data.txt](./data/cc_processed/exp3B_1/)| [exp3B_1](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus/experiments/exp3B_1/pretrain_data/)|

## Single Token Representation
The setup is similar as described [here](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus#single-token-representation).  
Both `Option-1` and `Option-2` are to be experimented with in this repository.  

## Setup
* The BERTRAM model used directly from the original author's work. The submodule `bertram` contains the code for the same.  
* The BERTRAM model available from the original authors has been trained on `bert-base-uncased` model, and is available [here for download](https://github.com/DarshanAdiga/bertram#-pre-trained-models). Hence the same will be used the Sequence Classification task on MAGPIE dataset.

## Experiments

| Experiment | Code  | Dataset | Single Token Type | Base Model | No of Examples | Status | Updated model |
|:-----------|:------|:--------|:------------------|:-----------|:---------------|:-------|:--------------|
| bt_0       | [bt_0](./experiments/bt_0/) | [all_replace_data.txt](./data/cc_processed/exp3B_1/) | `Option-1` |bert-base-uncased | 20 | TODO | [bert-base-uncased_option1_with_bertram](./local_models/bert-base-uncased_option1_with_bertram) |
| bt_1       | [bt_1](./experiments/bt_1/) | [all_replace_data.txt](./data/cc_processed/exp3B_1/) | `Option-1` |bert-base-uncased | 50 | TODO | TODO |
| bt_2       | [bt_2](./experiments/bt_2/) | [all_replace_data.txt](./data/cc_processed/exp3B_1/) | `Option-1` |bert-base-uncased | 200 | TODO | TODO |

### Results
The results on **Sequence Classifier task on MAGPIE dataset** task using the BERTRAM embeddings in a BERT model.
| Experiment | Dev Accuracy | Dev F1 | Test Accuracy | Test F1 |
|:-----------|:-------------|:-------|:--------------|:--------|
| bt_0       | 0.0 | 0.0 | 0.0 | 0.0 |

## References

[1] D. Phelps, “drsphelps at SemEval-2022 Task 2: Learning idiom representations using BERTRAM.” arXiv, May 25, 2022. Accessed: Jun. 19, 2022. [Online]. Available: http://arxiv.org/abs/2204.02821

[2] T. Schick and H. Schütze, “BERTRAM: Improved Word Embeddings Have Big Impact on Contextualized Model Performance.” arXiv, Apr. 29, 2020. Accessed: Jun. 19, 2022. [Online]. Available: http://arxiv.org/abs/1910.07181

[3] Hessel Haagsma, Johan Bos, and Malvina Nissim. 2020. MAGPIE: A Large Corpus of Potentially Idiomatic Expressions. In Proceedings of the 12th Language Resources and Evaluation Conference, pages 279–287, Marseille, France. European Language Resources Association.
