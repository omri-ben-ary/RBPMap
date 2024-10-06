import pandas as pd
import torch
from torch.utils.data import Dataset
from sklearn.preprocessing import LabelEncoder

class RNADataset(Dataset):
    def __init__(self, texts, labels, device='cpu'):
        self.texts = texts
        label_encoder = LabelEncoder()
        labels = label_encoder.fit_transform(labels)
        print(set(labels))  # or set(your_label_tensor.tolist())
        self.labels = torch.tensor(labels).to(device)
    
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, idx):
        text = self.texts.iloc[idx]
        label = self.labels[idx]
        return text, label
