import torch
from torch.utils.data import DataLoader,Dataset

class Data(Dataset):
	def __init__(self):
		self.x=torch.arange(-3.0,3.0,0.1).view(-1,1)
		self.f=self.x-1
		self.y=self.f+0.1*torch.tensor(self.x.size())
		self.len=self.x.shape[0]

	def __getitem__(self,index):
		samples=self.x[index],self.y[index]
		return samples


	def __len__(self):
		return self.len

dataset=Data()
data_trainer=DataLoader(dataset=dataset,batch_size=1)
COST=[]


from torch import nn,optim
class linear_regression(nn.Module):
	def __init__(self,input_size,output_size):
		super(linear_regression,self).__init__()
		self.linear=nn.Linear(input_size,output_size)

	def forward(self,x):
		yhat=self.linear(x)
		return yhat

criterion=nn.MSELoss()
	
model=linear_regression(1,1)
model.state_dict()['linear.weight'][0] = -15
model.state_dict()['linear.bias'][0] = -10
optimizer=optim.SGD(model.parameters(),lr=0.01)


def training_model(iter):

	for epoch in range(iter):
		for x,y in data_trainer:
			yhat=model(x)
			loss=criterion(yhat,y)
			optimizer.zero_grad()
			loss.backward()
			
			optimizer.step()

training_model(50)
			

