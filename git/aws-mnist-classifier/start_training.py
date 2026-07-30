import argparse

import torch
import torch.nn as nn
import torch.optim as optim

import torchvision
import torchvision.transforms as transforms

from torch.utils.data import DataLoader


# ==========================================
# Argumente von SageMaker lesen
# ==========================================

def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--epochs",
        type=int,
        default=5
    )

    return parser.parse_args()



# ==========================================
# 1. Neuronales Netzwerk (CNN)
# ==========================================

class CNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(

            nn.Conv2d(
                in_channels=1,
                out_channels=16,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(2),


            nn.Conv2d(
                in_channels=16,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(2),


            nn.Flatten(),


            nn.Linear(
                32 * 7 * 7,
                128
            ),

            nn.ReLU(),


            nn.Linear(
                128,
                10
            )
        )


    def forward(self, x):

        return self.network(x)



# ==========================================
# 2. Training
# ==========================================

def train():

    args = parse_args()

    epochs = args.epochs


    device = torch.device(
        "cuda" if torch.cuda.is_available()
        else "cpu"
    )

    print("Training auf:", device)
    print("Epochs:", epochs)



    # ======================================
    # MNIST Daten
    # ======================================

    transform = transforms.Compose([
        transforms.ToTensor()
    ])


    train_data = torchvision.datasets.MNIST(

        root="/tmp/mnist",

        train=True,

        download=True,

        transform=transform

    )


    train_loader = DataLoader(

        train_data,

        batch_size=64,

        shuffle=True

    )



    # ======================================
    # Modell
    # ======================================

    model = CNN()

    model.to(device)



    optimizer = optim.Adam(

        model.parameters(),

        lr=0.001

    )


    loss_function = nn.CrossEntropyLoss()



    # ======================================
    # Training Loop
    # ======================================

    for epoch in range(epochs):

        total_loss = 0


        for images, labels in train_loader:


            images = images.to(device)

            labels = labels.to(device)



            output = model(images)



            loss = loss_function(

                output,

                labels

            )



            optimizer.zero_grad()

            loss.backward()

            optimizer.step()



            total_loss += loss.item()



        print(
            f"Epoch {epoch + 1}/{epochs} "
            f"Loss: {total_loss:.2f}"
        )



    # ======================================
    # Modell speichern für SageMaker
    # ======================================

    model_path = "/opt/ml/model/model.pth"


    torch.save(

        model.state_dict(),

        model_path

    )


    print("Modell gespeichert:", model_path)



# ==========================================
# Start
# ==========================================

if __name__ == "__main__":

    train()
