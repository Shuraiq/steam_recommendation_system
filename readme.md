## Steam Game Recommender

- The main objective of this application is to recommend games to users.
- The games suggested to the user is based on the reviews that he has written. 
- The recommended games to a particular user are based on the reviews that have been written for the games. 

In a nutshell, a user is represented by all the reviews that he has written and a game is represented by all the reviews that have been written. And the recommeded games to a user or to a game are based on how close these vectors of each reviews are.

The application(website) that we developed where the model we developed is implemented is here: https://steam-recommendations.herokuapp.com/

### Setup

To implement the code we have two main folders: Frontend and ML, that implement the website and the trained model respectively. Each of the folders has its own environments. The setup of each of these folders is as follows.

#### ML

Step 1: Enter into the folder using the command - cd ML

Step 2: Create a conda environment. Command to - conda create --name myenv --file requirements.txt. 

Step 3: Activate a conda environment. Command to activate - conda activate nameofenv. Refer the link https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf for more details.

#### Frontend

Step 1: Enter into the folder using the command - cd Frontend

Step 2: Create an environment of your choice (conda or venv), preferably venv. Refer the link https://docs.python.org/3/library/venv.html

Step 3: Activate the environment

Step 4: Install the packages using the requirements.txt using the command - pip install -r requirements.txt

Step 5: To run the application - streamlit run Home.py


### Building the model

As you might have observed there are many .ipynb files in thie folder. Lets go through them in the chronologiacal order

Step 1: We need to combine all the .csv files into one. Now run the cells in the file named "CSVFormation.ipynb". Which will create a dataframe of all the combined csvs (Approppriate path to the csv files need to be given).

Step 2: Along with the combined dataframe we also get large, medium and small datasets from the combined dataframe. These dataframes will also be converted to csvs which will need to be put into the folder named Dataset. 

Step 3: Now run the cells in the file names "Dataset Creation.ipynb" which will create the approppriate datasets for training a model.

Step 4: Run the cells in the file named "Vector.ipynb", which will train and save a model named "model28_11".

Step 5: The files namingly "woring_model","Dict_formation","review_sentiment" in the mentioned order which will develop and save the data needed accordingly.

Step 6: The files with the data will be stored accordingly.
 
### Building the Frontend

The files developed by the model are copied and put in the Frontend folder, which will be used by the application.

Run the application using the command streamlit run Home.py
