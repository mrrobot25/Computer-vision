import torch
import numpy as np
from torch.utils.data import Dataset,Dataloader
class data(Dataset):
	def __init__(self):
		self.x=torch.arange(-2,2,0.1).view(-1,1)
		self.y=torch.zeros(self.x.shape[0])
		self.y=self.y[(self.x>-1.0)[:,0]*(self.x<1.0)[:,0]]=1
		self.y=self.y[(self.x<=1.0)[:,0]]=2
		self.y=self.y.type(LongTensor)
		self.len=self.x.shape[0]

dataset=data()
print(dataset)
