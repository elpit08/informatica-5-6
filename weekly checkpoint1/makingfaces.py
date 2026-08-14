def main():
    user_text = input("Write a message ")
    print(f"{user_text}".replace(':)', '😃').replace(':(','😞'))

if __name__ == "__main__":
    main()
