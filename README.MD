# AWS MNIST Classifier

A machine learning project for classifying handwritten digits from the **MNIST dataset** using **PyTorch**.

The project demonstrates model training locally or in an AWS environment and includes scripts for preparing the training workflow and storing the resulting model artifact.

## Features

* 🧠 MNIST handwritten digit classification
* 🔥 PyTorch-based convolutional neural network (CNN)
* 🖥️ CPU and CUDA/GPU support
* ☁️ AWS/SageMaker-oriented training workflow
* 💾 PyTorch model export as `model.pth`
* ⚙️ Configurable number of training epochs in the training entry point

## Technology Stack

| Technology      | Purpose                                 |
| --------------- | --------------------------------------- |
| **Python**      | Application and training logic          |
| **PyTorch**     | Neural network and model training       |
| **Torchvision** | MNIST dataset and image transformations |
| **CUDA**        | Optional GPU acceleration               |
| **AWS**         | Cloud-based ML environment              |
| **SageMaker**   | Training environment integration        |

## Project Structure

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

The repository separates the training code from the top-level scripts used to start the training workflow and handle data/model uploads.

## Model Architecture

The classifier uses a convolutional neural network with:

```text
Input: MNIST image
        │
        ▼
Conv2D (1 → 16)
        │
      ReLU
        │
   MaxPooling
        │
        ▼
Conv2D (16 → 32)
        │
      ReLU
        │
   MaxPooling
        │
        ▼
      Flatten
        │
        ▼
   Linear Layer
     1568 → 128
        │
      ReLU
        │
        ▼
   Linear Layer
     128 → 10
        │
        ▼
   Digit 0–9
```

The final layer contains ten outputs corresponding to the ten MNIST digit classes (`0`–`9`).

## Training

The training implementation uses:

* PyTorch
* `torchvision.datasets.MNIST`
* `DataLoader`
* Adam optimization
* Cross-entropy loss
* CUDA when available

The model is trained for five epochs in the SageMaker-oriented training implementation.

### Training locally

The repository contains a top-level training entry point:

```bash
python start_training.py
```

The training script automatically selects CUDA when an NVIDIA GPU is available and otherwise falls back to the CPU.

You can also configure the number of epochs through the script's command-line argument:

```bash
python start_training.py --epochs 10
```

## Output Model

The training workflow saves the trained PyTorch model as:

```text
model.pth
```

For the SageMaker training workflow, the model is written to:

```text
/opt/ml/model/model.pth
```

This allows the resulting model artifact to be consumed by an AWS-managed training workflow.

## Requirements

The project requires Python and the PyTorch ecosystem.

Install the dependencies according to the project's dependency configuration:

```bash
pip install -r requirements.txt
```

The training code uses:

```text
torch
torchvision
```

For GPU training, a compatible NVIDIA driver and CUDA-enabled PyTorch installation are required.

## AWS / SageMaker

The training code contains paths used by AWS SageMaker training jobs, including:

```text
/opt/ml/input/data/train
/opt/ml/model
```

The training script can therefore be used as part of a SageMaker training workflow.

A typical workflow is:

```text
MNIST Dataset
      │
      ▼
Training
      │
      ▼
PyTorch CNN
      │
      ▼
model.pth
      │
      ▼
AWS / SageMaker
```

## GPU Support

The training code automatically detects whether CUDA is available:

```python
device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)
```

This means the same training code can run on a CPU or use an available CUDA-capable GPU.

You can verify GPU availability with:

```bash
nvidia-smi
```

## What This Project Demonstrates

This project provides a compact example of:

* MNIST image classification
* Convolutional neural networks
* PyTorch model training
* GPU acceleration with CUDA
* Model serialization with PyTorch
* AWS/SageMaker-oriented ML workflows
* Separating training logic from the project entry point

## Possible Extensions

Possible future improvements include:

* [ ] Add a dedicated inference script
* [ ] Add model evaluation on a test dataset
* [ ] Report accuracy and loss metrics
* [ ] Add model inference examples
* [ ] Add automated model upload to S3
* [ ] Add Docker support
* [ ] Add AWS SageMaker deployment configuration
* [ ] Add experiment tracking
* [ ] Add CI/CD for training and testing

## Project Status

The repository currently focuses on the **MNIST training workflow and model generation**.

The core workflow is:

```text
MNIST
  │
  ▼
PyTorch CNN
  │
  ▼
Training
  │
  ▼
model.pth
```

## License

This project is licensed under the **MIT License**.

