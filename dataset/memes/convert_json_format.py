def convert(file_path, file_ouptut_name):
    import json
    json_path = file_path
    with open(json_path, 'r') as j:
        data = json.load(j)
    new_data = dict()
    new_data_train = dict()
    new_data_val = dict()
    new_data_test = dict()
    new_data['images'] = []
    new_data_train['images'] = []
    new_data_val['images'] = []
    new_data_test['images'] = []
    img_counter = 0
    sentence_id_count = 0
    for img in data:
        new_image = dict()
        new_image['sentids'] = []
        new_image['imgid'] = img_counter
        new_image['sentences'] = []
        meme_count = 5
        for meme in img["generated_memes"]:
            meme_count -= 1
            new_image['sentids'].append(sentence_id_count)
            raw_cap_list =  [meme['caption_text'].split(" | ")[0]]
            for sentence in raw_cap_list:
                new_token = dict()
                word_list = sentence.split(" ")
                new_word_list = []
                for i in word_list:
                    if len(i) > 0 and i != "w/" and "." not in i and i != ' ':
                        temp = i
                        temp_li = []
                        if "\n" in i:
                            temp_li = temp.split("\n")
                            for l in temp_li:
                                new_word_list.append(l.strip("!").strip("\n"))
                        else:
                            new_word_list.append(i.strip("!").strip("\n"))
                new_token["tokens"] = new_word_list
                new_token["raw"] = raw_cap_list[0]
                new_token["imgid"] = img_counter
                new_token["sentid"] = sentence_id_count
                new_image["sentences"].append(new_token)
            if img_counter < 50:
                new_image['split'] = "train"
            else:
                if img_counter < 65:
                    new_image['split'] = "val"
                else:
                    new_image['split'] = "test"
            new_image['filename'] = img['base_img']
            sentence_id_count += 1
            if meme_count == 0:
                break

        img_counter += 1
        new_data['images'].append(new_image)
        if new_image['split'] == "train":
            new_data_train['images'].append(new_image)
        if new_image['split'] == "val":
            new_data_val['images'].append(new_image)
        if new_image['split'] == "test":
            new_data_test['images'].append(new_image)
    new_data['dataset'] = "meme"
    new_data_train['dataset'] = "meme"
    new_data_val['dataset'] = "meme"
    new_data_test['dataset'] = "meme"
    json.dump(new_data, open(file_ouptut_name + ".json", 'w+'))
    json.dump(new_data_train, open(file_ouptut_name + "_train.json", 'w+'))
    json.dump(new_data_val, open(file_ouptut_name + "_val.json", 'w+'))
    json.dump(new_data_test, open(file_ouptut_name + "_test.json", 'w+'))


if __name__ == "__main__":
    convert('E:\Data Science MSc\Q4\CV\LRP\LRP-imagecaptioning-pytorch\dataset\memes\meme_local_dataset.json', 'meme_regenerate')




