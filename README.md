# AWS MNIST Classifier

A PyTorch-based MNIST image classifier designed for local training and AWS SageMaker-compatible workflows.

The project demonstrates a simple deep learning training pipeline using PyTorch and Torchvision, with support for CPU and CUDA-enabled GPU environments.

## Features

* MNIST dataset training with PyTorch
* Torchvision-based data loading
* Automatic CPU / CUDA device selection
* Configurable number of training epochs
* SageMaker-compatible training paths
* Model artifact export as `model.pth`
* Local training support
* Simple structure suitable for experimenting with AWS machine learning workflows

## Machine Learning Workflow

```text
MNIST Dataset
     │
     ▼
Data Loading
     │
     ▼
PyTorch Model
     │
     ▼
Training
     │
     ▼
Model Artifact
     │
     ▼
model.pth
```

## Technology Stack

* **Python**
* **PyTorch**
* **Torchvision**
* **MNIST**
* **CUDA** (when available)
* **AWS SageMaker** compatibility

## Project Structure

```text
aws-mnist-classifier/
├── training/
│   └── train.py
├── README.MD
├── start_training.py
└── upload_data.py
```

### `start_training.py`

Local training entry point.

It:

* loads the MNIST dataset
* selects CUDA when available
* falls back to CPU otherwise
* trains the PyTorch model
* saves the trained model to:

```text
/opt/ml/model/model.pth
```

### `training/train.py`

SageMaker-oriented training script.

The script expects training data under:

```text
/opt/ml/input/data/train
```

and writes the trained model to:

```text
/opt/ml/model/model.pth
```

### `upload_data.py`

Reserved for the data-upload workflow. The current file does not contain an implemented upload pipeline.

## Local Training

Install the required Python packages for your environment, including PyTorch and Torchvision.

Start training with:

```bash
python start_training.py
```

The number of epochs can be configured:

```bash
python start_training.py --epochs 10
```

The default device selection uses CUDA when it is available:

```text
CUDA → GPU
CPU  → CPU fallback
```

## AWS SageMaker

The training code follows the directory conventions commonly used by SageMaker training jobs.

Training input:

```text
/opt/ml/input/data/train
```

Model output:

```text
/opt/ml/model/model.pth
```

This makes the training code suitable as a basis for running the classifier inside a SageMaker training environment.

## Model Artifact

After training, the model is stored as:

```text
model.pth
```

The artifact can subsequently be used as the input for an inference workflow.

## Results

This repository focuses on the training implementation. If training metrics, predictions, confusion matrices, or screenshots are added to the repository, they can be presented here as the visual results of the classifier.

Example:

```markdown
![MNIST Classification Results](path/to/result.png)
```

## Dependencies

The repository currently does not contain a root-level `requirements.txt`.

For a reproducible project setup, the dependencies used by the training scripts should eventually be documented in a dedicated dependency file such as:

```text
requirements.txt
```

or:

```text
pyproject.toml
```

## Possible Improvements

The current project provides the basic training workflow. Possible extensions include:

* Add a dedicated evaluation step
* Calculate accuracy and other classification metrics
* Add a confusion matrix
* Add an inference script for individual MNIST images
* Store training metrics
* Add reproducible dependency versions
* Complete the data-upload workflow
* Add a complete SageMaker training configuration

## Project Purpose

The project is intended as a compact example of a PyTorch image-classification workflow that can be used locally and adapted for AWS SageMaker.

It demonstrates the connection between:

* dataset handling
* PyTorch model training
* GPU acceleration
* model artifact creation
* cloud-oriented training paths

## Author

**Markus**

## License

No license is documented in this README.

