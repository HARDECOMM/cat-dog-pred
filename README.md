**Streamlit_app_url:** https://cat-dog-pred-rsr3newzqqbqfg78rvudiw.streamlit.app/

🐱🐶 Cats vs Dogs Image Classifier

Custom MobileNetV2 model classifying cat 🐱 vs dog 🐶 images, deployed as an interactive Streamlit web app for real-time predictions.

**Mechanism:**: (Upload an image → Get instant prediction with confidence!)

**🎯 Aim**
Build and deploy a lightweight computer vision model using transfer learning to distinguish cats from dogs with ~98% test accuracy.

**🧩 Key Features**
--Efficient Model: Fine-tuned MobileNetV2 (ImageNet pretrained).

--Real-Time Web App: Streamlit UI for image uploads and predictions.

--High Accuracy: Cross-entropy loss + Adam optimizer.

--Easy Deploy: One-click setup; works on Streamlit Cloud.

**📂 Dataset**
Kaggle Cats and Dogs (~25k images):

## 📁 dataset Structure
```
cats-and-dogs/
├── training/
│   ├── cats/      # 8k+ images
│   └── dogs/
└── test/
    ├── cats/      # 2k images
    └── dogs/
```
    
**⚙️ Quick Setup**
Clone & install:

git clone https://github.com/HARDECOMM/cat-dog-pred.git
cd cat-dog-pred
pip install -r requirements.txt
Add your trained model: model/cat_dog_model.pth

**Run:** streamlit run app.py

Streamlit Cloud: Fork → Connect repo → Deploy (free!).

🧠 Model Breakdown
Architecture: MobileNetV2 backbone (frozen features) + custom 2-class head.

Preprocessing: Resize to 
224
×
224
224×224, normalize.

Inference: Argmax on softmax probabilities.

Perf: ~98% test accuracy (varies by epochs/dataset).

Input Image → MobileNetV2 → [0.92 Dog, 0.08 Cat] → 🐶 Dog (92%)

## 📁 Project Structure
```
cats-dogs-streamlit/
├── model/              # cat_dog_model.pth
├── app.py             # Streamlit app
├── requirements.txt   # Dependencies
└── README.md          # Project docs
```

**📊 Results**
Metric	Value
Test Acc.	98%
Inference	<1s
Model Size	9MB

**🔗 Resources**

PyTorch ImageFolder
MobileNetV2
dogs & cat Dataset

Built with ❤️ for computer vision portfolios. Star if useful! ⭐
