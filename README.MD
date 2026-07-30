# AWS MNIST Classifier

A machine learning project that classifies handwritten digits from the MNIST dataset. The trained model is stored in an Amazon S3 bucket and loaded by the application during runtime.

---

# Requirements

* Python 3.x
* AWS Account
* AWS CLI
* Amazon S3 Bucket
* IAM User with S3 permissions

---

## Project Structure

```text
aws-mnist-classifier/
│
├── training/
│   ├── start_training.py      # Starts the model training
│   ├── upload_data.py         # Uploads training data or model files to Amazon S3
│   ├── train.py               # Training logic
│   └── ...
│
├── models/                    # Saved model files
├── data/                      # Local dataset
├── requirements.txt
├── README.md
└── ...
```

## Workflow

The project follows this workflow:

1. Prepare the training dataset.
2. Run the training process:

```bash
python training/start_training.py
```

3. Upload the trained model or required files to Amazon S3:

```bash
python training/upload_data.py
```

4. The application downloads the model from the configured S3 bucket and performs digit classification.

## Main Files

| File                         | Description                                              |
| ---------------------------- | -------------------------------------------------------- |
| `training/start_training.py` | Starts the model training process.                       |
| `training/upload_data.py`    | Uploads the trained model or project files to Amazon S3. |
| `requirements.txt`           | Python dependencies required for the project.            |
| `README.md`                  | Project documentation and AWS setup instructions.        |

---

# Installation

Clone the repository:

```bash
git clone https://github.com/CodeByMaxx/aws-mnist-classifier.git
cd aws-mnist-classifier
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

# AWS Configuration

## 1. Create an IAM User

1. Open the **AWS Management Console**.
2. Navigate to **IAM**.
3. Select **Users** → **Create user**.
4. Give the user a name (e.g. `mnist-app`).
5. Create an **Access Key** for programmatic access.
6. Save the **Access Key ID** and **Secret Access Key**.

### Required Permissions

Attach a policy that allows access to your S3 bucket.

Minimum permissions:

* `s3:GetObject`
* `s3:ListBucket`

If the application uploads files:

* `s3:PutObject`

---

## 2. Configure AWS CLI

Install the AWS CLI and run:

```bash
aws configure
```

Enter:

* AWS Access Key ID
* AWS Secret Access Key
* Default Region (e.g. `eu-central-1`)
* Output format (`json`)

---

## 3. Create an S3 Bucket

1. Open **Amazon S3**.
2. Click **Create bucket**.
3. Choose a globally unique bucket name.
4. Select your preferred AWS Region.
5. Create the bucket.

Example:

```text
mnist-model-bucket/
└── mnist_model.keras
```

Upload your trained model to the bucket.

---

## 4. Configure the Project

Update the bucket name and model filename inside the application:

```python
BUCKET_NAME = "your-bucket-name"
MODEL_FILE = "mnist_model.keras"
```

---

# Running on an EC2 GPU Instance (Optional)

If you want to train the model on AWS using a GPU:

1. Open **EC2**.
2. Click **Launch Instance**.
3. Choose an Ubuntu AMI.
4. Select a GPU instance type such as:

   * `g4dn.xlarge`
   * `g5.xlarge`
   * `p3.2xlarge` (if available)
5. Create or select an existing key pair.
6. Launch the instance.

Connect via SSH:

```bash
ssh -i your-key.pem ubuntu@<EC2-PUBLIC-IP>
```

Check whether the GPU is available:

```bash
nvidia-smi
```

If a compatible NVIDIA driver is installed, this command displays the GPU model, driver version, memory usage, and running processes.

You can also verify that TensorFlow detects the GPU:

```python
import tensorflow as tf

print(tf.config.list_physical_devices("GPU"))
```

---

# Run the Project

```bash
python main.py
```

The application downloads the trained model from Amazon S3 and performs digit classification.

---

# License

This project is licensed under the MIT License.

