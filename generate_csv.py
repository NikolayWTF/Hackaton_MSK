import csv
with open("Forest_Group.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["1.JPG", "5.JPG", "10.JPG", "11.JPG"])
    file_writer.writerow(["1000", "897", "32", "23"])
    file_writer.writerow(["89", "167", "1289", "41"])
