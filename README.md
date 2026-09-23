# AWS MNIST Classifier

A PyTorch-based MNIST image classification project designed to run locally and in an AWS SageMaker-style training environment.

The project focuses on training a neural network to classify handwritten digits from the **MNIST dataset**, with support for CUDA when a GPU is available.

## ✨ Features

* MNIST digit classification with PyTorch
* GPU acceleration through CUDA when available
* CPU fallback for local development
* SageMaker-compatible training paths
* Automatic MNIST dataset download
* Configurable number of training epochs
* Model artifact export as `model.pth`
* Separate training entry points for local/SageMaker workflows

## 🛠️ Technology Stack

* **Python**
* **PyTorch**
* **Torchvision**
* **MNIST**
* **CUDA** when available
* **AWS SageMaker** training conventions

## 🧠 Machine Learning Workflow

The basic workflow is:

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
Model Evaluation
     │
     ▼
model.pth
```

## 📂 Project Structure

```text
aws-mnist-classifier/
├── training/
│   └── train.py
├── start_training.py
├── upload_data.py
└── README.md
```

The repository currently contains the training implementation and AWS-oriented training scripts. Additional application or inference components are not assumed to be part of the current project.

## 🚀 Training

The main training script can be started with:

```bash
python start_training.py
```

The number of epochs can be configured through the command-line interface:

```bash
python start_training.py --epochs 10
```

The training code automatically uses CUDA when it is available and otherwise falls back to CPU execution.

## 🖥️ Local Training

For local development, PyTorch selects the available compute device.

Conceptually:

```python
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)
```

This allows the same training code to run on a machine with an NVIDIA GPU as well as on a CPU-only development environment.

## ☁️ AWS / SageMaker

The `training/train.py` implementation follows the directory conventions commonly used by Amazon SageMaker training jobs.

Training data is expected in the SageMaker input directory:

```text
/opt/ml/input/data/train
```

The trained model is written to:

```text
/opt/ml/model/model.pth
```

This structure allows the training script to be adapted for execution inside a SageMaker training container.

## 💾 Model Output

After training, the model is saved as:

```text
model.pth
```

In the SageMaker-oriented workflow, the model artifact is written below:

```text
/opt/ml/model/model.pth
```

The model artifact can subsequently be used as the input for an inference workflow.

## 📊 Results

The current repository focuses on the training implementation.

No separate committed result visualization is assumed here. When evaluation screenshots, accuracy plots, confusion matrices, or prediction examples are added to the repository, they should be displayed in this section so that the README shows the actual ML result.

For example:

```text
Training
   │
   ▼
Evaluation
   │
   ├── Accuracy
   ├── Loss
   └── Example Predictions
```

## 🔧 Configuration

The training workflow supports configuring the number of epochs:

```bash
python start_training.py --epochs 10
```

The training environment determines whether CPU or CUDA execution is used.

## 📦 Dependencies

The current repository does not contain a root-level `requirements.txt`.

The project therefore relies on the Python environment providing the required PyTorch and Torchvision dependencies.

For a reproducible setup, a future improvement would be to add a dependency definition such as:

```text
requirements.txt
```

or preferably:

```text
pyproject.toml
```

with pinned or constrained versions.

## 🧪 Development Notes

The repository currently contains two training-oriented entry points:

* `start_training.py`
* `training/train.py`

`start_training.py` provides the convenient top-level training entry point, while `training/train.py` follows the directory conventions expected by a SageMaker-style training environment.

Keeping these responsibilities clearly separated is useful when the project is executed both locally and in AWS.

## 🔮 Possible Improvements

Potential next steps include:

* Add a dedicated evaluation script
* Report test accuracy and loss
* Add a confusion matrix
* Add example predictions
* Add an inference script
* Add reproducible dependency management
* Add automated tests
* Add an AWS SageMaker training configuration
* Upload datasets through a dedicated S3 workflow
* Add a deployment/inference endpoint

## 🎯 Project Purpose

This project demonstrates the basic workflow of taking a classical computer-vision dataset, training a PyTorch model, producing a model artifact, and structuring the training code so that it can be adapted to an AWS SageMaker environment.

The focus is on the **ML training workflow and AWS-oriented structure**, rather than on providing a complete production inference service.

## 📄 License

No license file is assumed here unless one is present in the repository. If the project is intended for reuse, an explicit license can be added.

---

**Project:** AWS MNIST Classifier
**Author:** Markus

