import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader
import torchvision.datasets as dataset
import torchvision.transforms as transforms
from tqdm import tqdm
from yaml import load

# Create a fully connected Network
class NN(nn.Module):
    def __init__(self,input_size,no_of_classes):
        super(NN,self).__init__() 
        
        '''
        Add some more layers to imporve the performance of the model
        '''
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(input_size, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, no_of_classes),
        )
        
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

# Setting up the device
device =torch.device('cuda'if torch.cuda.is_available () else 'cpu')

# Hyper Parameters
input_size = 784  ## Input size of the image
num_classes = 10
learning_rate = 0.0001
batch_size = 64
num_epochs = 5

# Load dataset
train_dataset = dataset.MNIST(root='dataset/',train=True,transform=transforms.ToTensor(),download=True)
test_dataset = dataset.MNIST(root='dataset/',train=False,transform=transforms.ToTensor(),download=True)
train_loader = DataLoader(dataset=train_dataset,batch_size=batch_size,shuffle=True)
test_loader = DataLoader(dataset=test_dataset,batch_size=batch_size,shuffle=True)

# Initialize the network
model = NN(input_size=input_size,no_of_classes = num_classes)

# Loss Function and Optimizer
loss_fcn = nn.CrossEntropyLoss()
optimizer = optim.RMSprop(model.parameters(),lr = learning_rate)

# Train the Netork
for epoch in range(num_epochs):
    for batch_idx,(data,targets) in enumerate (tqdm(train_loader)):
        # Get data to cuda if possible
        data = data.to(device = device)
        '''
        shape = 64,1,28,28  -- Batch size,No of channels,width,height
        '''
        targets = targets.to(device = device)

        # Reshape the Tensor
        data = data.reshape(data.shape[0],-1)
        '''
        shape = 64,784  -- Batch size,No of channels x width x height
        '''
        
        # Forward Pass 
        score = model(data)
        loss = loss_fcn(score,targets)

        # Backpass
        optimizer.zero_grad()
        loss.backward()

        optimizer.step()

def check_acc(loader,model):
    
    num_correct = 0
    num_samples = 0
    model.eval()

    with torch.no_grad():
        for x,y in loader:
            x = x.to(device = device)
            y = y.to(device = device)
            x = x.reshape(x.shape[0],-1)

            scores = model(x)
            _,predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)


    model.train()
    return num_correct / num_samples

print(f"Accuracy on training set: {check_acc(train_loader, model)*100:.2f}")
print(f"Accuracy on test set: {check_acc(test_loader, model)*100:.2f}")