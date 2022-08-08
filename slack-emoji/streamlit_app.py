import cv2
import torch
import numpy as np
from torchvision import transforms
import streamlit as st
from PIL import Image, ImageDraw


st.write(
        f'<span style="font-size: 78px; line-height: 1">📸</span>',
        unsafe_allow_html=True,
    )
"""
# Slack emoji generator

Create an animated Slack emoji from your co-workers photo!
"""


def make_transparent_foreground(pic, mask):
    # split the image into channels
    b, g, r = cv2.split(np.array(pic).astype('uint8'))
    # add an alpha channel with and fill all with transparent pixels (max 255)
    a = np.ones(mask.shape, dtype='uint8') * 255
    # merge the alpha channel back
    alpha_im = cv2.merge([b, g, r, a], 4)
    # create a transparent background
    bg = np.zeros(alpha_im.shape)
    # setup the new mask
    new_mask = np.stack([mask, mask, mask, mask], axis=2)
    # copy only the foreground color pixels from the original image where mask is set
    foreground = np.where(new_mask, alpha_im, bg).astype(np.uint8)

    return foreground


def remove_background(input_image):
    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model

    # move the input and model to GPU for speed if available
    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')

    with torch.no_grad():
        output = model(input_batch)['out'][0]
    output_predictions = output.argmax(0)

    # create a binary (black and white) mask of the profile foreground
    mask = output_predictions.byte().cpu().numpy()
    background = np.zeros(mask.shape)
    bin_mask = np.where(mask, 255, background).astype(np.uint8)

    foreground = make_transparent_foreground(input_image, bin_mask)

    return foreground, bin_mask


@st.experimental_memo
def inference(img):
    foreground, _ = remove_background(img)
    return foreground


torch.hub.download_url_to_file('https://pbs.twimg.com/profile_images/691700243809718272/z7XZUARB_400x400.jpg',
                               'demis.jpg')
torch.hub.download_url_to_file('https://hai.stanford.edu/sites/default/files/styles/person_medium/public/2020-03/hai_1512feifei.png?itok=INFuLABp',
                               'lifeifei.png')
model = torch.hub.load('pytorch/vision:v0.6.0', 'deeplabv3_resnet101', pretrained=True)
model.eval()

img_file = st.file_uploader("Upload a portrait photo", type=["png","jpg","jpeg"])
if img_file:
    
    col1, col2 = st.columns(2)
    col1.write("Uploaded image:")
    col2.write("Background removed:")
    
    img = Image.open(img_file)
    size = 256, 256
    img.thumbnail(size)
    with col1:
        st.image(img, use_column_width=True)
    
    crop = st.slider("Crop", 0, 100, 0)
    img = img.crop((crop, crop, img.width - crop, img.height - crop))
    
    h,w = img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((np.array(img),npAlpha))
    
    col2.image(npImage)


    
    with col2:
        output = inference(npImage)
        st.image(output, use_column_width=True)
    # output = inference(Image.open("demis.jpg"))
