# AWS MNIST Classifier

A small end-to-end machine learning project for classifying handwritten digits from the **MNIST dataset**.

The project combines **TensorFlow/Keras**, local model training, **Amazon S3** model storage, and optional **AWS EC2 GPU** training.

The main goal is to demonstrate how a trained ML model can be moved from a local development environment into a simple cloud-based workflow.

## Architecture

```text
                 ┌────────────────────┐
                 │    MNIST Dataset   │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │   Model Training   │
                 │  TensorFlow/Keras  │
                 └─────────┬──────────┘
                           │
                           ▼
                  mnist_model.keras
                           │
                           ▼
                 ┌────────────────────┐
                 │     Amazon S3      │
                 │   Model Storage    │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │    Application     │
                 │  Model Download    │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Digit Classification│
                 └────────────────────┘
```

## Technology Stack

| Component        | Technology                   |
| ---------------- | ---------------------------- |
| Language         | Python                       |
| Machine Learning | TensorFlow / Keras           |
| Dataset          | MNIST                        |
| Cloud Storage    | Amazon S3                    |
| Cloud Compute    | Amazon EC2                   |
| GPU Support      | NVIDIA CUDA / TensorFlow GPU |
| CLI              | AWS CLI                      |

## Project Structure

```text
aws-mnist-classifier/
│
├── training/
│   ├── start_training.py
│   ├── upload_data.py
│   ├── train.py
│   └── ...
│
├── models/
│   └── ...
│
├── data/
│   └── ...
│
├── requirements.txt
├── start_training.py
├── upload_data.py
└── README.MD
```

The main components are separated into training, data, and model handling.

## Workflow

The project follows four main steps:

```text
1. Prepare MNIST data
        │
        ▼
2. Train the model
        │
        ▼
3. Upload model to S3
        │
        ▼
4. Download model and classify digits
```

### 1. Training

Start model training with:

```bash
python training/start_training.py
```

The resulting model is stored locally before being uploaded to Amazon S3.

### 2. Upload

Upload the required model/data files:

```bash
python training/upload_data.py
```

### 3. Model Storage

The trained model can be stored in an S3 bucket:

```text
mnist-model-bucket/
└── mnist_model.keras
```

### 4. Inference

The application downloads the configured model from S3 and uses it for digit classification.

## Requirements

For local development:

* Python 3.x
* TensorFlow
* AWS CLI
* AWS account
* Amazon S3 bucket

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## AWS Configuration

The project uses Amazon S3 to store the trained model.

The application requires access to the configured S3 bucket.

### IAM Permissions

The IAM identity used by the application needs only the permissions required by the workflow.

For downloading the model:

```text
s3:GetObject
s3:ListBucket
```

If the application uploads files:

```text
s3:PutObject
```

For production deployments, prefer an IAM role or another short-lived credential mechanism over long-lived access keys.

## AWS CLI

Install the AWS CLI and configure the local environment:

```bash
aws configure
```

Provide:

```text
AWS Access Key ID
AWS Secret Access Key
Default Region
Output format
```

Example region:

```text
eu-central-1
```

Never commit AWS credentials to the repository.

## S3 Bucket

Create an S3 bucket with a globally unique name.

For example:

```text
mnist-model-bucket/
└── mnist_model.keras
```

The application can then be configured to use the bucket:

```python
BUCKET_NAME = "your-bucket-name"
MODEL_FILE = "mnist_model.keras"
```

Keep bucket names and other environment-specific configuration separate from credentials.

## Local Training

Run:

```bash
python training/start_training.py
```

The training process creates the model artifact locally.

The resulting model can then be uploaded:

```bash
python training/upload_data.py
```

## AWS GPU Training

The project can also be used with an AWS EC2 GPU instance.

A typical workflow is:

```text
Local Development
       │
       ▼
    AWS EC2
       │
       ▼
GPU-based Training
       │
       ▼
   Model File
       │
       ▼
    Amazon S3
```

Example GPU-capable EC2 instance types include:

* `g4dn.xlarge`
* `g5.xlarge`
* `p3.2xlarge`

Availability and pricing depend on the selected AWS region and account.

Connect to an EC2 instance through SSH:

```bash
ssh -i your-key.pem ubuntu@<EC2-PUBLIC-IP>
```

Check GPU availability:

```bash
nvidia-smi
```

TensorFlow can also be checked with:

```python
import tensorflow as tf

print(tf.config.list_physical_devices("GPU"))
```

## Running the Application

After the model has been uploaded to S3 and the application is configured, run:

```bash
python main.py
```

The application downloads the trained model and performs digit classification.

## Machine Learning Workflow

The complete ML lifecycle can be summarized as:

```text
MNIST
  │
  ▼
Training
  │
  ▼
Evaluation
  │
  ▼
Keras Model
  │
  ▼
S3
  │
  ▼
Model Download
  │
  ▼
Inference
```

This separation allows the model artifact to be stored independently from the application that performs inference.

## Cloud Architecture

The project demonstrates a simple separation between compute and model storage:

```text
┌─────────────────┐
│  EC2 / Local    │
│                 │
│ Model Training  │
└────────┬────────┘
         │
         │ upload
         ▼
┌─────────────────┐
│   Amazon S3     │
│                 │
│ Model Artifact  │
└────────┬────────┘
         │
         │ download
         ▼
┌─────────────────┐
│   Application   │
│                 │
│    Inference    │
└─────────────────┘
```

## Security Considerations

AWS credentials must never be stored directly in source code or committed to Git.

Avoid committing:

```text
AWS Access Key IDs
AWS Secret Access Keys
Private keys
.env files
Local AWS credentials
```

For AWS-hosted workloads, IAM roles are preferable to embedding credentials in the application.

S3 permissions should also follow the principle of least privilege.

## What This Project Demonstrates

This project provides a compact example of:

* MNIST image classification
* TensorFlow/Keras model training
* Model artifact management
* Amazon S3 integration
* AWS CLI usage
* IAM permissions
* EC2 GPU preparation
* Local/cloud ML workflows
* Separation of training and inference

## Possible Extensions

Potential improvements include:

* FastAPI inference service
* Dockerized inference
* Automated model deployment
* Model versioning
* ML experiment tracking
* Automated evaluation
* CI/CD
* Infrastructure as Code
* AWS Lambda inference
* AWS SageMaker deployment
* CloudWatch monitoring
* Automated retraining
* S3 versioning

## Project Status

The core workflow is:

```text
Training → S3 → Model Download → Classification
```

The project is intended as a compact demonstration of integrating a machine-learning model with AWS services while keeping local development possible.

## License

This project is licensed under the **MIT License**.

