import matplotlib.pyplot as plt


def plot_cost(cost_values):
    plt.title("Cost over time")
    plt.ylabel("Cost")
    plt.xlabel("iteration step")
    plt.plot(cost_values)

    plt.savefig("cost.png")

def plot_learning_curve(X, y, X_val, y_val, lambda_val):
    m = X.shape[0]

    #for i in range(m):
        #TODO: Learning Curve implementation
