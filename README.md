# AWS MNIST Classifier

A small **PyTorch** project for training a convolutional neural network (CNN) on the **MNIST handwritten digit dataset**.

The repository contains a local training script as well as a training script following the directory conventions commonly used by managed ML environments such as Amazon SageMaker.

> **Project status:** This is a learning and experimentation project. It currently focuses on model training and does not provide a web application or production inference service.

---

## Overview

The model classifies grayscale handwritten digits from `0` to `9`.

The implementation uses:

* PyTorch
* torchvision
* MNIST
* a custom convolutional neural network
* Cross-Entropy loss
* Adam optimization
* CPU or CUDA acceleration when available

The trained model is saved as a PyTorch `state_dict`.

---

## Model Architecture

The CNN consists of two convolutional blocks followed by fully connected layers:

```text
MNIST Image
28 × 28 × 1
     │
     ▼
Conv2d
1 → 16 channels
     │
     ▼
ReLU
     │
     ▼
MaxPool2d
     │
     ▼
Conv2d
16 → 32 channels
     │
     ▼
ReLU
     │
     ▼
MaxPool2d
     │
     ▼
Flatten
     │
     ▼
Linear
32 × 7 × 7 → 128
     │
     ▼
ReLU
     │
     ▼
Linear
128 → 10
     │
     ▼
Digit 0–9
```

The final layer produces **10 output values**, one for each MNIST class.

---

## Tech Stack

| Component     | Technology           |
| ------------- | -------------------- |
| Language      | Python               |
| Deep Learning | PyTorch              |
| Dataset       | MNIST                |
| Data Loading  | torchvision          |
| Optimization  | Adam                 |
| Loss Function | Cross-Entropy Loss   |
| Hardware      | CPU / CUDA           |
| Model Format  | PyTorch `state_dict` |

---

## Project Structure

```text
aws-mnist-classifier/
│
├── training/
│   └── train.py
│
├── README.MD
├── start_training.py
└── upload_data.py
```

### Training scripts

`start_training.py`

Local training script using:

```text
/tmp/mnist
```

as the MNIST dataset directory.

`training/train.py`

Training script using the directory convention:

```text
/opt/ml/input/data/train
```

and saving the model to:

```text
/opt/ml/model/model.pth
```

This layout is suitable for experimentation with managed ML environments, but the repository does **not** currently contain a complete SageMaker deployment configuration.

---

## Installation

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install PyTorch and torchvision according to your local CPU/CUDA environment.

For example, install the appropriate packages from the official PyTorch installation instructions.

---

## Local Training

The simplest training entry point is:

```bash
python start_training.py
```

The script:

1. selects CUDA when available
2. falls back to CPU otherwise
3. downloads MNIST through `torchvision` if necessary
4. creates the CNN
5. trains the model
6. saves the model state

The default number of epochs is:

```text
5
```

It can be changed using:

```bash
python start_training.py --epochs 10
```

---

## Training Configuration

The current training setup uses:

| Parameter     |             Value |
| ------------- | ----------------: |
| Epochs        |               `5` |
| Batch size    |              `64` |
| Learning rate |           `0.001` |
| Optimizer     |              Adam |
| Loss          |     Cross-Entropy |
| Input         | 28 × 28 grayscale |
| Classes       |                10 |

CUDA is automatically selected when available:

```python
torch.device("cuda" if torch.cuda.is_available() else "cpu")
```

---

## Model Output

The model is saved as:

```text
/opt/ml/model/model.pth
```

The saved file contains the model's PyTorch `state_dict`.

The model can later be restored by creating the same CNN architecture and loading the saved state dictionary.

---

## Managed ML / SageMaker-Oriented Training

The repository contains:

```text
training/train.py
```

which follows the common directory conventions:

```text
/opt/ml/input/data/train
/opt/ml/model
```

This makes the script suitable as a starting point for integration with a managed training environment.

However, the repository currently does **not** contain:

* a SageMaker training job definition
* an estimator configuration
* an AWS infrastructure definition
* an inference endpoint
* a deployment script
* an S3 upload implementation

The project should therefore be considered a **training prototype**, rather than a complete AWS ML deployment.

---

## Dataset

MNIST is downloaded through `torchvision.datasets.MNIST`.

The dataset contains grayscale images of handwritten digits:

```text
0 1 2 3 4 5 6 7 8 9
```

Each image has a resolution of:

```text
28 × 28 pixels
```

The dataset is not stored in the Git repository.

---

## Current Limitations

The current project is intentionally small.

Known limitations include:

* no dedicated inference script
* no test/validation reporting in the training scripts
* no accuracy metric output
* no confusion matrix
* no model evaluation script
* no requirements file
* no automated tests
* no production inference service
* no complete SageMaker deployment configuration
* `upload_data.py` does not currently provide an implemented upload workflow

The local training script also writes its model to `/opt/ml/model/model.pth`, so this path may need adjustment when running it outside a managed environment.

---

## Possible Improvements

Future improvements could include:

* add a `requirements.txt`
* add a dedicated evaluation script
* calculate test accuracy
* add precision, recall and F1 metrics
* add a confusion matrix
* save training metrics
* create a reusable model module
* add an inference script
* add Docker support
* add proper SageMaker training configuration
* add S3 dataset/model management
* add automated tests
* add CI/CD

---

## Security

No AWS credentials should be stored in the repository.

Use standard AWS credential mechanisms such as:

* AWS CLI profiles
* environment variables
* IAM roles
* instance profiles

Never commit access keys or secret keys to source control.

---

## Author

**Markus**

Machine Learning / Cloud Engineering Project.

