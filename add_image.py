
import torchvision
from torch.utils.tensorboard import SummaryWriter

dataset_transform=torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])

train_set=torchvision.datasets.CIFAR10(root='./DATASET',train=True,transform=dataset_transform,download=True)
test_set=torchvision.datasets.CIFAR10(root='./DATASET',train=False,transform=dataset_transform,download=True)

# print(test_set[0])
# print(test_set.classes)

# img,target=test_set[0]
# print(img)
# print(target)
# img.show()

writer = SummaryWriter(log_dir='logs')

for i in range(10):
    img,target=test_set[i]
    #print(img)
    writer.add_image('Pics'+str(i),img_tensor=img,global_step=0)

writer.close()