import json
import requests


def download_image(url, file_path, file_name):
    img_data = requests.get(url).content
    file_path_full = file_path + file_name + '.jpg'
    with open(file_path_full, 'wb') as handler:
        handler.write(img_data)


if __name__ == '__main__':
    data = json.load(open("memes.json", "r"))
    meme_local_dataset = []
    for image in data:
        url = image['base_img']
        id = image['id']
        filepath = 'image_' + str(id)
        print(filepath)
        download_image(url, 'images/', filepath)
        image['base_img'] = 'images/' + filepath + '.jpg'
        meme_local_dataset.append(image)
    json.dump(meme_local_dataset, open('meme_local_dataset.json', 'w+'))
