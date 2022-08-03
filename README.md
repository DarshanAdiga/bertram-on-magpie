# BERTRAM on MAGPIE dataset
Use BERTRAM [2] to get single-token embeddings for idioms on the MAGPIE [3] dataset.
High level objectives:
1. Get single-token embeddings for idioms in the MAGPIE dataset using pretrained BERTRAM model
    - Use sentences from `CC News Corpus` as contexts to obtain the BERTRAM embeddings. This data is already prepared [here](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus#variations-of-exp3) for a different task(training a BERT model with single-token representations).
    - Insert the new tokens of the form `<BERTRAM:IDsomeidiomtokenID>` into `bert-base-uncased` model with these embeddings.
2. Use these embeddings to train a Sequence Classifier task on MAGPIE dataset to clasify idiom/literal meanings.

## Dataset used
Original dataset is available: [MAGPIE_filtered_split_{*}.jsonl](https://github.com/hslh/magpie-corpus).

## Single Token Representation
The setup is similar as described [here](https://github.com/DarshanAdiga/idiom-principle-on-magpie-corpus#single-token-representation).  
Both `Option-1` and `Option-2` are to be experimented with in this repository.  

## Setup
* The BERTRAM model used directly from the original author's work. The submodule `bertram` contains the code for the same.  
* The original BERTRAM model has been trained on `bert-base-uncased` model, hence the same will be used the Sequence Classification task on MAGPIE dataset.

## Experiments

## References

[1] D. Phelps, “drsphelps at SemEval-2022 Task 2: Learning idiom representations using BERTRAM.” arXiv, May 25, 2022. Accessed: Jun. 19, 2022. [Online]. Available: http://arxiv.org/abs/2204.02821

[2] T. Schick and H. Schütze, “BERTRAM: Improved Word Embeddings Have Big Impact on Contextualized Model Performance.” arXiv, Apr. 29, 2020. Accessed: Jun. 19, 2022. [Online]. Available: http://arxiv.org/abs/1910.07181

[3] Hessel Haagsma, Johan Bos, and Malvina Nissim. 2020. MAGPIE: A Large Corpus of Potentially Idiomatic Expressions. In Proceedings of the 12th Language Resources and Evaluation Conference, pages 279–287, Marseille, France. European Language Resources Association.
