import matplotlib.pyplot as plt
import pandas as pd

def main():

    df = pd.read_csv("grades.csv")

    assignment_avg = df.mean(axis=1)

    plt.hist(assignment_avg, bins=100)
    plt.axvline(assignment_avg.mean(), color="red", linestyle="--", label=r"Average")
    plt.axvline(assignment_avg.mean() - assignment_avg.std(), color="grey", linestyle="--", label=r"1$\sigma$")
    plt.axvline(assignment_avg.mean() + assignment_avg.std(), color="grey", linestyle="--")
    plt.legend()
    plt.xlabel("Assignment average")
    plt.savefig("assignments.png", dpi=200)

    easy_assignments = assignment_avg[(assignment_avg - assignment_avg.mean()) > assignment_avg.std()]
    hard_assignments = assignment_avg[(assignment_avg.mean() - assignment_avg) > assignment_avg.std()]

    print("These assignments are too easy")
    print(easy_assignments)

    print("These assignments are too hard")
    print(hard_assignments)

main()
