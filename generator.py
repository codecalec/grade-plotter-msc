import numpy as np
import matplotlib.pyplot as plt


def main():

    num_chkpoints = 15
    num_students = 20

    assignment_means = np.random.normal(0.6, 0.2, num_chkpoints)
    print(assignment_means)

    std = 0.2
    grades = np.vstack([np.random.normal(mean, std, num_students) for mean in assignment_means])
    grades = np.clip(grades, 0, 1)

    assert grades.shape == (num_chkpoints,num_students)

    header = ",".join(
        [
            f"s{num}"
            for num in np.random.randint(low=2000000, high=2900000, size=num_students)
        ]
    )
    np.savetxt("grades.csv", grades, delimiter=",", fmt="%.2f", header=header)


if __name__ == "__main__":
    main()
