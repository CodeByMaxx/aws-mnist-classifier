# AWS MNIST Classifier

A compact deep learning project for classifying handwritten digits from the **MNIST dataset** using **PyTorch**.

The project demonstrates a convolutional neural network (CNN), CPU/GPU training with CUDA and an AWS/SageMaker-oriented training workflow.

> **Project status:** The repository currently focuses on model training and model artifact generation. A separate inference application is not included yet.

---

## Overview

The classifier recognizes handwritten digits from `0` to `9`.

The current workflow is:

```text
MNIST Dataset
     │
     ▼
DataLoader
     │
     ▼
PyTorch CNN
     │
     ▼
Training
     │
     ▼
model.pth
     │
     ▼
SageMaker Model Artifact
```

The same training code can use either:

* CPU
* CUDA-enabled NVIDIA GPU

depending on the available PyTorch environment.

---

## Technology Stack

| Component     | Technology                      |
| ------------- | ------------------------------- |
| Language      | Python                          |
| Deep Learning | PyTorch                         |
| Dataset       | MNIST                           |
| Data Loading  | Torchvision / DataLoader        |
| Model         | Convolutional Neural Network    |
| Optimization  | Adam                            |
| Loss          | Cross-Entropy                   |
| GPU           | CUDA                            |
| Cloud ML      | AWS SageMaker-oriented workflow |

---

## Project Structure

```text
aws-mnist-classifier/
│
├── training/
│   └── train.py
│
├── start_training.py
├── upload_data.py
└── README.md
```

### Main files

| File                | Purpose                                     |
| ------------------- | ------------------------------------------- |
| `start_training.py` | Main configurable training entry point      |
| `training/train.py` | SageMaker-oriented training implementation  |
| `upload_data.py`    | Placeholder for future upload functionality |
| `README.md`         | Project documentation                       |

The repository currently contains no committed `main.py` or `requirements.txt`.

---

## Model Architecture

The classifier uses a small convolutional neural network:

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

The architecture is implemented with `torch.nn.Sequential`. The final layer contains ten outputs, one for each MNIST class.

---

## Training

The training pipeline uses:

* `torch`
* `torchvision`
* `DataLoader`
* Adam optimizer
* Cross-Entropy loss
* CUDA when available

The default training configuration is:

| Parameter     |         Value |
| ------------- | ------------: |
| Batch size    |          `64` |
| Learning rate |       `0.001` |
| Epochs        |           `5` |
| Optimizer     |          Adam |
| Loss          | Cross-Entropy |
| Image size    |     `28 × 28` |

The top-level `start_training.py` additionally accepts the number of epochs as a command-line argument.

---

## Training Locally

The main entry point is:

```bash
python start_training.py
```

The number of epochs can be changed:

```bash
python start_training.py --epochs 10
```

The script automatically selects CUDA when it is available:

```python
device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)
```

Otherwise, training runs on the CPU.

### GPU check

For an NVIDIA environment, you can check the installed driver with:

```bash
nvidia-smi
```

The training code itself uses `torch.cuda.is_available()` to determine whether CUDA can be used.

---

## MNIST Dataset

The dataset is downloaded automatically through:

```python
torchvision.datasets.MNIST(...)
```

The top-level training script stores the downloaded dataset under:

```text
/tmp/mnist
```

The SageMaker-oriented implementation uses:

```text
/opt/ml/input/data/train
```

as its training data location.

---

## Model Output

The trained model is saved as a PyTorch state dictionary:

```text
model.pth
```

For the SageMaker-oriented training workflow, the output path is:

```text
/opt/ml/model/model.pth
```

This location follows the directory structure expected by an AWS SageMaker training environment.

---

## AWS SageMaker

The project contains SageMaker-oriented paths:

```text
/opt/ml/input/data/train
/opt/ml/model
```

The intended workflow is:

```text
AWS SageMaker
      │
      ▼
MNIST Training Data
      │
      ▼
PyTorch CNN
      │
      ▼
model.pth
      │
      ▼
SageMaker Model Artifact
```

The top-level training script accepts command-line arguments for the number of epochs, making it suitable as a starting point for a managed training job.

---

## Training Implementations

There are currently two training-related implementations.

### `start_training.py`

The top-level script:

* parses `--epochs`
* downloads MNIST to `/tmp/mnist`
* selects CPU or CUDA
* trains the CNN
* saves the model to `/opt/ml/model/model.pth`

### `training/train.py`

The implementation under `training/` follows the SageMaker directory conventions more directly:

```text
/opt/ml/input/data/train
/opt/ml/model
```

It uses five training epochs by default and writes the resulting state dictionary to:

```text
/opt/ml/model/model.pth
```

---

## Important: Local vs. SageMaker Execution

The current training code is strongly oriented toward an AWS/SageMaker environment because the model output is written to:

```text
/opt/ml/model/model.pth
```

Therefore, a completely standalone local workflow may require adapting the output path to a local directory.

For example:

```text
models/model.pth
```

would be a more typical local output location.

---

## Dependencies

The repository currently does **not contain a committed `requirements.txt`**.

The training code imports:

```text
torch
torchvision
```

Therefore, a local environment needs a compatible PyTorch installation before running the training scripts.

For a reproducible project setup, a future version should add a dependency file such as:

```text
requirements.txt
```

or a modern Python project configuration such as:

```text
pyproject.toml
```

---

## AWS Upload

The repository contains:

```text
upload_data.py
```

However, the current file is empty. It does not currently implement an S3 upload workflow.

An AWS upload step can therefore be considered a future extension rather than an implemented feature.

---

## Current Workflow

The currently implemented core workflow is:

```text
MNIST
  │
  ▼
Torchvision
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

## What This Project Demonstrates

This project provides a compact example of:

* MNIST image classification
* Convolutional neural networks
* PyTorch model training
* CPU/GPU training
* CUDA detection
* Torchvision dataset handling
* PyTorch model serialization
* AWS SageMaker-oriented training paths

---

## Future Improvements

Possible next steps include:

* add `requirements.txt` or `pyproject.toml`
* add a dedicated inference script
* add test-set evaluation
* report accuracy and loss
* add confusion matrix
* add example predictions
* move local model output to a configurable directory
* implement S3 upload
* add a SageMaker training configuration
* add Docker support
* add automated tests
* add CI/CD
* add model versioning

---

## License

The current repository documentation states that the project is licensed under the MIT License.

---

## Author

**Markus**

