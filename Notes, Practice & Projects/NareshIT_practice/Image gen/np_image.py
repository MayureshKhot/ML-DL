import numpy as np
import pandas as pandas
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO # Used for buffered input output in memory, it stores the image in memory for temp

def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

image_url = 'https://i.pinimg.com/736x/6a/de/0f/6ade0f41f7b6323ae57f81fa29c9a6b0.jpg'
image = load_image_from_url(image_url)

# Display an original image
plt.figure(figsize=(6,4))
plt.imshow(image)
plt.title('Image')
plt.axis('off')
plt.show()

# Image to array
image_np = np.array(image)
print('Image Shape', image_np.shape)

#greyscale image
image_grey = image.convert("L")

plt.figure(figsize=(6,6))
plt.imshow(image_grey)
plt.title('Greay image')
plt.axis('off')
plt.show()