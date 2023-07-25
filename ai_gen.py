import os
import replicate
import requests
from PIL import Image


def ai_get(prompt: str):
    os.environ["REPLICATE_API_TOKEN"] = "r8_HbmvW2w1R6OmLcqFLvB8DsNQSPEc5501xzCPY"

    output = replicate.run(
        "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
        input={"prompt": prompt}
    )

    return output[0]


def download_picture(url: str, name: str):
    response = requests.get(url)
    if response.status_code:
        fp = open(name, 'wb')
        fp.write(response.content)
        fp.close()


def insert_image(print_path, t_shirt_path, distances, final_path, mask_path=None):
    im1 = Image.open(print_path)
    im2 = Image.open(t_shirt_path)

    im1 = im1.resize(distances[0], Image.LANCZOS)

    if mask_path is not None:
        mask = Image.open(mask_path).resize(im1.size)
        im2.paste(im1, distances[1], mask)
    else:
        im2.paste(im1, distances[1])

    im2.show()
    im2.save(final_path)


if __name__ == "__main__":
    # url = ai_get("An astronaut riding a horse")
    # download_picture(url, "./pictures/print1.png")
    insert_image("./pictures/print1.png", "./pictures/shirts/black_t-shirt.png",
                 ((1000, 400), (1000, 300)), "./pictures/final.png")