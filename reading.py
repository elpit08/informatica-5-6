def largest(file):
    with open(file) as num_list:
        all_numbers = []
        for _ in num_list:
            all_numbers.append(_)

        print(max(all_numbers))



def main():
    #with open("sample.txt") as new_file:
        #content = new_file.read()
        #print(content)
    #count = 0
    #with open("sample.txt" ) as hoco_week:
        #for _ in hoco_week:
            #_ = _.replace("\n","")
            #count += 1
            #print(f"{count}: {_}")
    largest("random_numbers.txt")



if __name__=="__main__":
    main()
