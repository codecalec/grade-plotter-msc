import matplotlib.pyplot as plt
import pandas as pd

def save_outlying_assignments(averages, filename):

    # Find assignments which are sufficiently higher or lower than the mean
    easy_assignments = averages[(averages - averages.mean()) > averages.std()]
    hard_assignments = averages[(averages.mean() - averages) > averages.std()]

    # Save the assignments to a file 
    with open(filename, "w") as f:
        print("Easy Assignments:", file=f)
        for idx, average in easy_assignments.items(): 
            print("Assignment {}\tAvg={:.2f}".format(idx, average), file=f)

        print("Hard Assignments:", file=f)
        for idx, average in easy_assignments.items(): 
            print("Assignment {}\tAvg={:.2f}".format(idx, average), file=f)

def main():

    # Double check the csv is properly formatted
    # All entries should be in decimal (80% -> 0.80)
    # Might need to look at https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    df = pd.read_csv("grades_correct.csv")

    # Get class average for each assignment
    assignment_avg = df.mean(axis=1)

    # Plot class averages with the mean and std of the assignment marks
    plt.hist(assignment_avg, bins=100)
    plt.axvline(assignment_avg.mean(), color="red", linestyle="--", label=r"Average")
    plt.axvline(assignment_avg.mean() - assignment_avg.std(), color="grey", linestyle="--", label=r"1$\sigma$")
    plt.axvline(assignment_avg.mean() + assignment_avg.std(), color="grey", linestyle="--")
    plt.legend()
    plt.xlabel("Assignment average")
    plt.savefig("assignments.png", dpi=200)

    # Save the sufficiently outlying assignments
    save_outlying_assignments(assignment_avg, "summary.txt")

    print("Done!")
main()
