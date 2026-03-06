# generate_embeddings.py
import numpy as np
import torch
from transformers import CLIPModel, CLIPProcessor
from datasets import load_dataset

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

ds = load_dataset("Artificio/WikiArt")
train_data = ds['train']

embeddings = []
batch_size = 32

for i in range(0, len(train_data), batch_size):
    batch = train_data[i:i+batch_size]
    images = batch['image']
    
    inputs = clip_processor(images=images, return_tensors="pt", padding=True).to(device)
    
    with torch.no_grad():
        features = clip_model.get_image_features(**inputs)
        features = features / features.norm(dim=-1, keepdim=True)
    
    embeddings.append(features.cpu().numpy())
    print(f"Processed {min(i+batch_size, len(train_data))}/{len(train_data)}")

all_embeddings = np.vstack(embeddings)
np.save("combined_embeddings.npy", all_embeddings)
print(f"Saved embeddings with shape: {all_embeddings.shape}")