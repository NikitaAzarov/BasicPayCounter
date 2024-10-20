import sys
import os
from datetime import datetime

PER_HOUR = 35

def shiftWokringTime(filePath):
    days = 0
    totalWorkingTime = 0
    with open(filePath, "r") as file:
        for line in file:
            line = line.strip()
            line = line.replace(" ", "")
            if line:
                date = datetime.strptime(line[0:10], "%Y-%m-%d")
                timeStart = datetime.strptime(line[10:15], "%H:%M")
                timeEnd =  datetime.strptime(line[15:20], "%H:%M")
                totalTime = (timeEnd - timeStart).seconds / 3600
                totalWorkingTime += totalTime
                days += 1
    totalWorkingTime = round(totalWorkingTime, 2)
    avgDayWorkingTime = round(totalWorkingTime / days, 2)
    print(f"You worked {days} days ({totalWorkingTime} hours).")
    print(f"Average working day: {avgDayWorkingTime}.")
    print(f"Your salary is {round(totalWorkingTime * PER_HOUR, 2)} shekel.\n")

def printReport(filePath):
    with open(filePath, "r") as file:
        for line in file:
            line = line.strip()
            line = line.replace(" ", "")
            if line:
                totalTime = round((datetime.strptime(line[15:20], "%H:%M") - datetime.strptime(line[10:15], "%H:%M")).seconds / 3600, 2)
                print(line[0:10])
                print(f"{line[10:15]} - {line[15:20]} ({totalTime})\n")


def main():
    if len(sys.argv) != 2:
        print("Are you debil?\n")
        print("Use: python SalaryCounter.py <file path>")
        return

    abs_txt_file_path = os.path.abspath(sys.argv[1])

    printReport(abs_txt_file_path)
    shiftWokringTime(abs_txt_file_path)



if __name__ == "__main__":
    main()
    input("\nPress enter to exit...")
