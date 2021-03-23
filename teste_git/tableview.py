def  print_csv(filepath):
    csv_file = open(filepath)
    for line in csv_file:
        print(line)

    csv_file.close()
