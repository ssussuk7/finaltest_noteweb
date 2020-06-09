import matplotlib
import matplotlib.pyplot as plt
from torch.utils.data import Dataset,DataLoader
import numpy as np
import torchvision
from torchvision import transforms

trans = transforms.Compose([transforms.Resize((100,100)),
                           transforms.ToTensor(),
                           transforms.Normalize((0.5, 0.5, 0.5),(0.5, 0.5, 0.5))
                           ])
                           
trainset = torchvision.datasets.ImageFolder(root = "C:/Users/HP NOTE/.spyder-py3/test/test_images",
                                            transform = trans)

#print(trainset.__getitem__(18))
print(len(trainset))

classes = trainset.classes
print(classes)

trainloader = DataLoader(trainset,
                         batch_size = 16,
                         shuffle = False,
                         num_workers = 4)

dataiter = iter(trainloader)
images, labels = dataiter.next()
print(labels)

def imshow(img):
    img = img /2 + 0.5
    np_img = img.numpy()
    plt.imshow(np.transpose(np_img, (1,2,0)))
    
    print(np_img.shape)
    print((np.transpose(np_img,(1,2,0))).shape)
    
print(images.shape)
imshow(torchvision.utils.make_grid(images, nrow=4))
print(images.shape)
print((torchvision.utils.make_grid(images)).shape)
print("".join("%5s" %classes[labels[j]] for j in range(4)))