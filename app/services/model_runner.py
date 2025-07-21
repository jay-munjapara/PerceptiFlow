import torch
from torchvision import models, transforms
from PIL import Image

model = models.resnet18(pretrained=True)
model.eval()


def predict(image_path: str):
    image = Image.open(image_path)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor()
    ])
    input_tensor = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)
    return output.argmax().item()
