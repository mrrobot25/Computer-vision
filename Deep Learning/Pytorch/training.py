import  pandas as pd
import torch
import numpy as np
from torch.utils.data import Dataset

class Data(Dataset):
	def __init__(self,train=True):
		self.X=torch.arange(-3.0,3.0,0.1).view(-1,1)
		self.f=3*self.X+1
		self.y=self.f+0.1*torch.randn(self.X.size())
		self.len=self.X.shape[0]
		
		if train==True:
			self.y[0]=0
			self.y[50:55]=20
		else:
			pass

	def __getitem__(self,index):

		return self.X[index],self.y[index]

	def __len__(self):
		return self.len

	
dataset = Data()
for i in dataset:
	print(i)
