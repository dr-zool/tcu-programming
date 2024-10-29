temp_file = open("../example2/temp.txt", "w")
print("first line", file = temp_file)
print("second line", file = temp_file)
temp_file.close()