class main:
    def main():
        days = ["thu", "fri", "sat", "sun", "mon", "tue", "wed"]
        day_index = int(input()) % 7
        print(days[day_index])
    
    if __name__ == "__main__":
        main()