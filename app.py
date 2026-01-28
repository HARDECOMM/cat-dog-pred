import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

st.set_page_config(page_title="Cats vs Dogs Classifier")

device = torch.device("cpu")

model = models.mobilenet_v2(weights="IMAGENET1K_V1")
model.classifier[1] = nn.Linear(model.last_channel, 2)
model.load_state_dict(torch.load("model/cat_dog_model.pth", map_location=device))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

st.title("🐱🐶 Cats vs Dogs Classifier")
st.write("Upload an image and the model will predict cat or dog.")

file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file).convert("RGB")
    st.image(img, use_container_width=True)

    x = transform(img).unsqueeze(0)

    with torch.no_grad():
        out = model(x)
        probs = torch.softmax(out, dim=1)
        conf, pred = torch.max(probs, 1)

    label = "Cat 🐱" if pred.item() == 0 else "Dog 🐶"
    st.subheader(f"Prediction: {label}")
    st.write(f"Confidence: {conf.item()*100:.2f}%")
