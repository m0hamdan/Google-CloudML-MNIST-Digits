# Deploying ML models on GCP MLE using Tensorflow Estimators
<br/>
### Table of Contents

1. [Project Motivation](#motivation)
2. [Dependencies](#depend)
3. [Datasets](#data)
4. [Content](#files)
5. [Instructions](#instructions)
6. [Licensing](#licensing)
7. [Acknowledgements](#ack)

### Project Motivation:<a name="motivation"></a>
This sample creates and trains MNIST model in Jupyter using Tensorflow and then deploys the trained model to Google Cloud MLE to serve the model, and accept prediction requests by REST API/Google MLE Client API.

### Dependencies <a name="depend"></a>
refer to requirements.txt

### Datasets <a name="data"></a>
Tensorflow MNIST dataset

### Content <a name="files"></a>
1. main.py: uses Google Cloud MLE Client API to make prediction calls
2. MNIST Notebook.ipynb: A jupyter notebook file used to create and train the model then use gsutil tool to upload the trained model to Google Cloud Storage (Bucket)

### Instructions <a name="instructions"></a>
1. Clone the repository: git clone https://github.com/m0hamdan/Dog_Breed_Identification_App.git 
2. Run the following command in the repo root directory: python main.py

### Licensing <a name="licensing"></a>
None

### Acknowledgements <a name="ack"></a>
1. Tensorflow webiste as I used the model created here https://www.tensorflow.org/tutorials/estimators/cnn



