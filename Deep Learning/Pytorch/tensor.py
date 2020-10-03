from torch.utils.data import Dataset
from torchvision import transforms
import torch
class Data(Dataset):
	def __init__(self,length=50,transform=None):
		self.length=length
		self.x=2*torch.ones(length,2)
		self.y=torch.ones(length,1)
		self.transform=transform
	
	def __getitem__(self,index):
		sample=self.x[index],self.y[index]
		if self.transform:
			sample=self.transform(sample)
		return sample
	def __len__(salf):
		return self.length

class mul(object):
	def __init__(self,xmul=5,ymul=3):
		self.xmul=xmul
		self.ymul=ymul
		
	def __call__(self,sample):
		x=sample[0]
		y=sample[1]
		x=x*self.xmul
		y=y*self.ymul
		sample=x,y
		return sample

class squareroot(object):
	def __call__(self,sample):
		x=sample[0]
		y=sample[1]
		x=torch.sqrt(x)
		y=torch.sqrt(y)
		sample=x,y
		return sample

new_transformed_data=transforms.Compose([mul(),squareroot()])

dataset=Data()
multi=mul()
print(dataset[5])
for i in range(20):
	x_,y_=dataset[i]
	print('before transformation')
	print(x_,y_)
	print('after transformation')
	x,y=new_transformed_data(dataset[i])
	print(x,y)
