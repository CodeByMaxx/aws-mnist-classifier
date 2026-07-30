import torch
import torch.nn as nn
import torch.optim as optim

import torchvision
import torchvision.transforms as transforms

from torch.utils.data import DataLoader


# ==========================================
# 1. Neuronales Netzwerk (CNN)
# ==========================================

class CNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(

            # Erste Convolution-Schicht
            nn.Conv2d(
                in_channels=1,
                out_channels=16,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(2),


            # Zweite Convolution-Schicht
            nn.Conv2d(
                in_channels=16,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(2),


            # Bild in Zahlenliste umwandeln
            nn.Flatten(),


            # Klassifikation
            nn.Linear(
                32 * 7 * 7,
                128
            ),

            nn.ReLU(),


            # 10 Klassen (0-9)
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

    # GPU benutzen falls vorhanden
    device = torch.device(
        "cuda" if torch.cuda.is_available()
        else "cpu"
    )

    print("Training auf:", device)



    # MNIST Daten vorbereiten

    transform = transforms.Compose([
        transforms.ToTensor()
    ])


    train_data = torchvision.datasets.MNIST(
        root="/opt/ml/input/data/train",
        train=True,
        download=True,
        transform=transform
    )


    train_loader = DataLoader(
        train_data,
        batch_size=64,
        shuffle=True
    )



    # Modell erstellen

    model = CNN()

    model.to(device)



    # Optimierer und Fehlerfunktion

    optimizer = optim.Adam(
        model.parameters(),
        lr=0.001
    )


    loss_function = nn.CrossEntropyLoss()



    # Training starten

    epochs = 5


    for epoch in range(epochs):

        total_loss = 0


        for images, labels in train_loader:


            images = images.to(device)
            labels = labels.to(device)



            # Vorhersage

            output = model(images)



            # Fehler berechnen

            loss = loss_function(
                output,
                labels
            )



            # Lernen

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()



            total_loss += loss.item()



        print(
            f"Epoch {epoch+1}/{epochs} "
            f"Loss: {total_loss:.2f}"
        )



    # ======================================
    # Modell für SageMaker speichern
    # ======================================

    model_dir = "/opt/ml/model"

    os.makedirs(
     model_dir,
     exist_ok=True
    )

    torch.save(
     model.state_dict(),
     f"{model_dir}/model.pth"
    )

    print("Modell gespeichert")



# ==========================================
# Programmstart
# ==========================================

if __name__ == "__main__":
    train()
