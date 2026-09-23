# AWS MNIST Classifier

A compact **PyTorch** project for training a convolutional neural network on the **MNIST handwritten digit dataset**.

The project demonstrates:

* PyTorch model training
* CNN-based image classification
* MNIST dataset handling
* CPU/GPU execution with CUDA
* configurable training epochs
* AWS SageMaker-compatible model output paths

> **Current scope:** The repository currently contains training code. It does **not** contain a completed inference application or implemented S3 upload script.

---

## Overview

The model classifies handwritten digits from:

```text
0
1
2
3
4
5
6
7
8
9
```

The current training workflow is:

```text
MNIST Dataset
     │
     ▼
Torchvision
     │
     ▼
DataLoader
     │
     ▼
PyTorch CNN
     │
     ▼
Adam + Cross-Entropy
     │
     ▼
CPU / CUDA
     │
     ▼
model.pth
```

---

## Technology Stack

| Component     | Technology                      |
| ------------- | ------------------------------- |
| Language      | Python                          |
| Deep Learning | PyTorch                         |
| Dataset       | MNIST                           |
| Dataset API   | Torchvision                     |
| Model         | Convolutional Neural Network    |
| Optimizer     | Adam                            |
| Loss          | Cross-Entropy                   |
| GPU           | CUDA via PyTorch                |
| Cloud Target  | AWS SageMaker-oriented workflow |

---

## Repository Structure

```text
aws-mnist-classifier/
│
├── training/
│   └── train.py
│
├── start_training.py
├── upload_data.py
└── README.MD
```

The current repository does **not** contain:

```text
main.py
requirements.txt
models/
data/
```

as committed root-level project components.

---

## Model Architecture

The CNN consists of two convolutional layers followed by fully connected layers:

```text
Input
28 × 28 × 1
    │
    ▼
Conv2D
1 → 16 channels
    │
    ▼
ReLU
    │
    ▼
MaxPool
    │
    ▼
Conv2D
16 → 32 channels
    │
    ▼
ReLU
    │
    ▼
MaxPool
    │
    ▼
Flatten
    │
    ▼
Linear
1568 → 128
    │
    ▼
ReLU
    │
    ▼
Linear
128 → 10
    │
    ▼
Digits 0–9
```

The architecture is implemented using `torch.nn.Sequential`. The final layer has ten outputs, corresponding to the ten MNIST classes.

---

## Training Configuration

The main training script uses:

| Parameter      |                      Value |
| -------------- | -------------------------: |
| Batch size     |                       `64` |
| Learning rate  |                    `0.001` |
| Default epochs |                        `5` |
| Optimizer      |                       Adam |
| Loss           |              Cross-Entropy |
| Input          | `28 × 28` grayscale images |

MNIST images are converted to tensors using:

```python
transforms.ToTensor()
```

---

## Local Training

The main entry point is:

```text
start_training.py
```

Install a compatible PyTorch/Torchvision environment first.

Then run:

```bash
python start_training.py
```

The number of epochs can be changed:

```bash
python start_training.py --epochs 10
```

The script accepts the `--epochs` command-line argument and defaults to five epochs.

---

## CPU / GPU

The training script automatically selects CUDA when available:

```python
device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)
```

Therefore:

```text
CUDA available
      │
      ▼
 NVIDIA GPU
```

or:

```text
CUDA unavailable
      │
      ▼
 CPU
```

The selected device is printed when training starts.

For NVIDIA environments, you can also check the GPU with:

```bash
nvidia-smi
```

---

## Dataset

The main training script downloads MNIST automatically using Torchvision:

```python
torchvision.datasets.MNIST(
    root="/tmp/mnist",
    train=True,
    download=True
)
```

The dataset is therefore not required to be committed to the repository.

---

## Training Loop

For each epoch, the script:

1. loads a batch of images
2. moves images and labels to the selected device
3. performs a forward pass
4. calculates Cross-Entropy loss
5. clears gradients
6. performs backpropagation
7. updates model weights
8. accumulates the training loss

The training loss is printed after every epoch.

---

## Model Output

The main training script saves the trained model as a PyTorch state dictionary:

```text
/opt/ml/model/model.pth
```

using:

```python
torch.save(
    model.state_dict(),
    model_path
)
```

This output path follows the directory convention used by Amazon SageMaker training jobs.

### Important

The current script does **not** create the `/opt/ml/model` directory itself before saving.

Therefore, running it locally may require changing the output path or creating the directory first.

A more portable local path would be something such as:

```text
models/model.pth
```

---

## SageMaker-Oriented Training

The repository also contains:

```text
training/train.py
```

This implementation follows SageMaker-style paths:

```text
/opt/ml/input/data/train
/opt/ml/model
```

The training data is loaded through Torchvision and the trained model is saved as:

```text
/opt/ml/model/model.pth
```

The repository therefore currently contains two closely related training implementations:

```text
start_training.py
        │
        ├── local MNIST path: /tmp/mnist
        └── output: /opt/ml/model/model.pth

training/train.py
        │
        ├── SageMaker input path
        └── output: /opt/ml/model/model.pth
```

---

## AWS Status

The project is **SageMaker-oriented**, but the current repository does not contain a complete AWS deployment implementation.

In particular:

* there is no AWS SDK code in the current training scripts
* there is no implemented S3 uploader
* there is no inference service
* there is no `main.py`

The file:

```text
upload_data.py
```

is currently empty.

Therefore, S3 upload and runtime model loading should be considered **future work**, not currently implemented functionality.

---

## Dependencies

The repository currently does not contain a committed:

```text
requirements.txt
```

The training code imports:

```text
torch
torchvision
```

as well as the Python standard library modules used by the scripts.

For reproducible setup, the project should add either:

```text
requirements.txt
```

or:

```text
pyproject.toml
```

with pinned or appropriately constrained PyTorch/Torchvision versions.

---

## Current Limitations

The current project is primarily a **training prototype**.

Known limitations include:

* no test-set evaluation
* no accuracy reporting
* no confusion matrix
* no inference script
* no web application
* no implemented S3 upload
* no committed dependency file
* local output path is not portable
* `training/train.py` currently uses `os.makedirs()` without importing `os`

The last point means the current `training/train.py` implementation needs a small code fix before its model-saving section can execute successfully.

---

## Recommended Next Steps

Possible improvements:

1. Add `requirements.txt` or `pyproject.toml`
2. Add a shared CNN/model module
3. Remove duplication between the two training scripts
4. Make dataset and output paths configurable
5. Add validation/test evaluation
6. Report accuracy
7. Add confusion matrix
8. Add an inference script
9. Implement S3 upload
10. Add an actual SageMaker training configuration
11. Add Docker support
12. Add automated tests

---

## Project Goal

The goal of this project is to provide a small and understandable example of a PyTorch image-classification workflow that can run locally and can be adapted to an AWS SageMaker environment.

The central concepts are:

```text
PyTorch
   +
CNN
   +
MNIST
   +
CUDA
   +
SageMaker-compatible model output
```

---

## Author

**Markus**

