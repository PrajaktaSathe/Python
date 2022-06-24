import torch
import torchvision # torch package for vision related things
import torch.nn.functional as F  # Parameterless functions, like (some) activation functions
import torchvision.datasets as datasets  # Standard datasets
import torchvision.transforms as transforms  # Transformations we can perform on our dataset for augmentation
from torch import optim  # For optimizers like SGD, Adam, etc.
from torch import nn  # All neural network modules
from torch.utils.data import DataLoader  # Gives easier dataset managment by creating mini batches etc.
from tqdm import tqdm  # For nice progress bar!

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
in_channels = 3
num_classes = 10
learning_rate = 0.001
batch_size = 1024
num_epochs = 5
load_model = True

# Load Data
train_dataset = datasets.CIFAR10(
    root="dataset/", train=True, transform=transforms.ToTensor(), download=True
)
test_dataset = datasets.CIFAR10(root="dataset/", train=False, transform=transforms.ToTensor(), download=True)

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)

'''
class CNN(nn.Module):
  def __init__(self,in_channels=1, num_classes=10):
        super(CNN,self).__init__()
        self.conv1 = nn.Conv2d(in_channels = in_channels,out_channels = 8,kernel_size=(3, 3),stride=(1, 1),padding=(1, 1),)
        self.pool = nn.MaxPool2d((2,2), (2,2))
        self.conv2 = nn.Conv2d(in_channels=8,
            out_channels=16,
            kernel_size=(3, 3),
            stride=(1, 1),
            padding=(1, 1),
        )
        self.dropout1 = nn.Dropout(0.3)
        self.dropout2 = nn.Dropout(0.3)

        self.fc1 = nn.Linear(1024, 512)
        self.fc2 = nn.Linear(512, 64)
        self.fc3 = nn.Linear(64, num_classes)

  def forward(self, x):
      x = self.pool(F.relu(self.conv1(x)))
      x = self.dropout1(x)
      x = self.pool(F.relu(self.conv2(x)))
      x = torch.flatten(x, 1)
      x = self.dropout1(x)
      x = F.relu(self.fc1(x))
      x = self.dropout1(x)
      x = F.relu(self.fc2(x))
      x = self.fc3(x)
      return x
'''

'''
# Initialize network
model = CNN(in_channels=in_channels, num_classes=num_classes).to(device)
'''

# Simple Identity class that let's input pass without changes
class Identity(nn.Module):
    def __init__(self):
        super(Identity, self).__init__()

    def forward(self, x):
        return x

# Load pretrain model & modify it
model = torchvision.models.vgg19(pretrained=True)

# If you want to do finetuning then set requires_grad = False
# Remove these two lines if you want to train entire model,
# and only want to load the pretrain weights.
for param in model.parameters():
    param.requires_grad = False

model.avgpool = Identity()
model.classifier = nn.Sequential(
    nn.Linear(512, 100), nn.ReLU(), nn.Dropout(),nn.Linear(100, num_classes)
)
model.to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(),lr = learning_rate)

# Train Network
for epoch in range(num_epochs):
    losses = []
    # if epoch % 3 == 0:
    #     checkpoint = {"state_dict": model.state_dict(), "optimizer": optimizer.state_dict()}
    #     # Try save checkpoint
    #     save_checkpoint(checkpoint)

    for batch_idx, (data, targets) in enumerate(tqdm(train_loader)):
        # Get data to cuda if possible
        data = data.to(device=device)
        targets = targets.to(device=device)

        # forward
        scores = model(data)
        loss = criterion(scores, targets)

        # backward
        optimizer.zero_grad()
        loss.backward()
        losses.append(loss.item())
        # gradient descent or adam step
        optimizer.step()

    print(f"Cost at epoch {epoch} is {sum(losses)/len(losses):.5f}")

# Check accuracy on training & test to see how good our model
def check_accuracy(loader, model):
    num_correct = 0
    num_samples = 0
    model.eval()

    with torch.no_grad():
        for x, y in loader:
            x = x.to(device=device)
            y = y.to(device=device)

            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)

        print(
                f"Got {num_correct} / {num_samples} with accuracy {float(num_correct)/float(num_samples)*100:.2f}"
            )
    model.train()

check_accuracy(train_loader, model)


'''
A self created CNN model as mentioned above when trained on CIFAR10 dataset gives an accuracy of ~ 46%,
whereas, when vgg19 is fine-tuned the accuracy improves upto 60%when trained fpr 5 epochs.   

'''