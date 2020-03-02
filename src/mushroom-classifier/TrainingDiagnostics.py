import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np

def plot_cost(cost_values):
    plt.title("Cost over time")
    plt.ylabel("Cost")
    plt.xlabel("iteration step")
    plt.plot(cost_values)
    plt.savefig("cost.png")

def plot_learning_curve(X, y, X_validation, y_validation, model, training_examples_steps=100):
    m = X.shape[0]
    error_training = []
    error_validation = []
    steps = range(training_examples_steps, 500, training_examples_steps)
    for i in steps:
        X_subset = X[:i,:]
        y_subset = y[:i]
        model.train(X_subset, y_subset)

        cost_hypothesis = model.hypothesis(X_subset, model.theta)
        cost_training_set = model.cost_function(cost_hypothesis, y_subset)
        error_training.append(cost_training_set)

        cost_validation_hypothesis = model.hypothesis(X_validation, model.theta)
        cost_validation_set = model.cost_function(cost_validation_hypothesis, y_validation)
        error_validation.append(cost_validation_set)

    plt.title("Learning Curve")
    plt.ylabel("Cost")
    plt.xlabel("# Of Training Examples")
    plt.plot(steps, error_training)
    fig = plt.plot(steps, error_validation)    
    return fig






