🐱🐶 Cats vs Dogs Image Classifier
[ [ [

Custom MobileNetV2 model classifying cat 🐱 vs dog 🐶 images, deployed as an interactive Streamlit web app for real-time predictions.

(Upload an image → Get instant prediction with confidence!)

🎯 Aim
Build and deploy a lightweight computer vision model using transfer learning to distinguish cats from dogs with ~95% test accuracy.

🧩 Key Features
Efficient Model: Fine-tuned MobileNetV2 (ImageNet pretrained).

Real-Time Web App: Streamlit UI for image uploads and predictions.

High Accuracy: Cross-entropy loss + Adam optimizer.

Easy Deploy: One-click setup; works on Streamlit Cloud.

📂 Dataset
Kaggle Cats and Dogs (~25k images):

text
cats-and-dogs/
├── train/    # 20k+ images
│   ├── cats/
│   └── dogs/
└── test/     # 5k images
    ├── cats/
    └── dogs/
⚙️ Quick Setup
Clone & install:

text
git clone <your-repo-url>
cd cats-dogs-streamlit
pip install -r requirements.txt
Add your trained model: model/cat_dog_model.pth

Run: streamlit run app.py

Streamlit Cloud: Fork → Connect repo → Deploy (free!).

🧠 Model Breakdown
Architecture: MobileNetV2 backbone (frozen features) + custom 2-class head.

Preprocessing: Resize to 
224
×
224
224×224, normalize.

Inference: Argmax on softmax probabilities.

Perf: ~95% test accuracy (varies by epochs/dataset).

text
Input Image → MobileNetV2 → [0.92 Dog, 0.08 Cat] → 🐶 Dog (92%)
📁 Folder Structure
text
cats-dogs-streamlit/
├── model/          # cat_dog_model.pth
├── app.py          # Streamlit app
├── requirements.txt
├── demo.gif        # Optional demo
└── README.md
📊 Results
Metric	Value
Test Acc.	95%
Inference	<1s
Model Size	14MB
🔗 Resources
PyTorch ImageFolder

MobileNetV2

Dataset

Built with ❤️ for computer vision portfolios. Star if useful! ⭐