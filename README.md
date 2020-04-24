# Mushroom Classification

A project, prototyped in Octave and implemented in Python, to use machine learning to classify a mushroom as poisonous/edible using the mushroom dataset from the UCI Machine Learning repository which can be viewed [here](https://www.kaggle.com/uciml/mushroom-classification).

The Python implementation purposely only uses NumPy and Pandas for linear algebra and data manipulation, this project contains **NO DEPENDENCY ON MACHINE LEARNING LIBRARIES** as the purpose was to implement logistic regression from scratch, rather than provide an efficient scalable solution.

# Python Implementation - Info

A virtual environment should be used to work on the project, in the `src` folder of the project. Once the virtual environment is setup a `paths.pth` should be added to the virtual environments `site-packages` folder. This should contain the absolute path to the `src` folder for the project.

Absolute paths also need to be set as environment variables for the `train.py` script within the `mushroom_classifier` module to work and export the models to the `trained_models` and `current_model` directories, the required environment variables are:

`export DATASET_DIR=ABSOLUTE-PATH-TO-DATASET-FOLDER(ie the files folder)`
`export CURRENT_MODEL_DIR=ABSOLUTE-PATH-TO-CURRENT-MODEL-FOLDER`
`export TRAINED_MODELS_DIR=ABSOLUTE-PATH-TO-TRAINED-MODEL-FOLDER`

The API also requires the path to the features definition file specified via a environment variable:
`export FEATURE_DEFINITION_PATH=ABSOLUTE-PATH-TO-DEFINITION-FILE`

To use the provided dataset in this repository set the `DATASET_DIR` environment variable to the absolute path of the `files` folder, as to correctly run the `train.py` script a `mushrooms.csv` file and `unseen_mushrooms.csv` file need to be present in the `DATASET_DIR` directory.

Before the `train.py` script is ran, you should run the available tests for the `mushroom_classifier` module.

The workflow currently, is to train the model and store it, with the relevant columns for reindexing and graph diagnostics, in a folder based on the current time. This folder is then stored in the directory specified in the `TRAINED_MODELS_DIR` environment variable. 

If the currently trained model has a high enough accuracy, and correctly predicts the completely known examples as specified in the `unseen_mushrooms.csv` file, this model and all its files will be exported and overwrite anything in the current model directory, as specified by the `CURRENT_MODEL_DIR` environment variable.