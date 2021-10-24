import urllib.request as lmao
import json

gameid = input("Enter game id: ")
url = "https://play.kahoot.it/rest/kahoots/" + gameid
q = json.loads(lmao.urlopen(url).read())["questions"]
position_list = ["Top Reft", "Top Right", "Bottom Left", "Bottom Right"]

for index, slide in enumerate(q):
    if slide.get("type") == "quiz":
        for i in range(len(slide.get("choices"))):
            if slide["choices"][i]["correct"] == True:
                print("Question number: {}\n{}\n{}\n".format(
                    index + 1, slide["choices"][i].get("answer"), position_list[i]))
