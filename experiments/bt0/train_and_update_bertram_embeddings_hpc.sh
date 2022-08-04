#!/bin/bash
#$ -l h_rt=3:00:00  #time needed
#$ -pe smp 1 #number of cores
#$ -l rmem=4G #Maximum amount (xx) of real memory to be requested per CPU core
#$ -l gpu=1 # Number of GPUs per every CPU core
#$ -o ./output.txt  #This is where your output and errors are logged.
#$ -j y # normal and error outputs into a single file (the file above)
#$ -M dahaniyanarayana1@sheffield.ac.uk #Notify you by email, remove this line if you don't like
#$ -m ea #Email you when it finished or aborted
#$ -cwd # Run job from current directory


module load apps/python/conda
# Only needed if we're using GPU* Load the CUDA and cuDNN module
module load libs/cudnn/7.3.1.20/binary-cuda-9.0.176
source activate /data/acp20dah/dissertation/venv_old_trans

# Copied this snippet from ./bertram/bertram_embeddings.sh
# This script is used to get the embeddings for the BERTram model and update the language model.
export BASE_DIR="../.."
export BERTRAM_MODEL=$BASE_DIR/"local_models/bertram-add-for-bert-base-uncased"
export BERT_MODEL="bert-base-uncased"
export OUTPUT_DIR=$BASE_DIR/"local_models/bert-base-uncased_option1_with_bertram"
export EXAMPLES_FOLDER="./context_data"
export NO_EXAMPLES=20

python3 $BASE_DIR/bertram/train_embeddings.py \
   --bertram_model $BERTRAM_MODEL \
   --bert_model $BERT_MODEL \
   --output_dir $OUTPUT_DIR \
   --examples_folder $EXAMPLES_FOLDER \
   --no_examples $NO_EXAMPLES
