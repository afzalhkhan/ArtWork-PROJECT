# Cell 1 - Install deps
!pip install transformers datasets torch

# Cell 2 - Run
import numpy as np
import torch
import torch.nn.functional as F
from transformers import CLIPModel, CLIPProcessor
from datasets import load_dataset

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")  # Should say cuda

clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
clip_model.eval()

ds = load_dataset("Artificio/WikiArt")
train_data = ds['train']
print(f"Total images: {len(train_data)}")

EMBEDDING_DIM = clip_model.config.projection_dim
embeddings = []
batch_size = 64  # Larger batch on GPU

for i in range(0, len(train_data), batch_size):
    batch = train_data[i:i + batch_size]
    images = batch['image']
    batch_len = len(images)

    try:
        inputs = clip_processor(images=images, return_tensors="pt")
        pixel_values = inputs['pixel_values'].to(device)

        with torch.no_grad():
            vision_outputs = clip_model.vision_model(pixel_values=pixel_values)
            pooled = vision_outputs.pooler_output
            projected = clip_model.visual_projection(pooled)
            features = F.normalize(projected, p=2, dim=-1)

        embeddings.append(features.cpu().numpy())

    except Exception as e:
        print(f"Error at batch {i}: {e}")
        embeddings.append(np.zeros((batch_len, EMBEDDING_DIM)))

    if i % (batch_size * 20) == 0:
        print(f"Progress: {min(i + batch_size, len(train_data))}/{len(train_data)}")

all_embeddings = np.vstack(embeddings)
np.save("combined_embeddings.npy", all_embeddings)
print(f"Done! Shape: {all_embeddings.shape}")

# Cell 3 - Download
from google.colab import files
files.download("combined_embeddings.npy")