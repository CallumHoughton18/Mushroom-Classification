import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import os

class TrainingDiagnostics():
    def __init__(self):
        plt.cla()
        self.mainfig = plt.figure()

    def plot_cost(self, cost_values):
        ax = self.mainfig.add_subplot(221)
        ax.title.set_text("Cost over time")
        ax.set_ylabel("Cost")
        ax.set_xlabel("iteration step")
        ax.plot(cost_values)

    def plot_learning_curve(self, X, y, X_validation, y_validation, model, max_training_size=None, training_examples_steps=100):
        max_training_size = X.shape[0] if max_training_size==None else max_training_size
        error_training = []
        error_validation = []
        steps = range(training_examples_steps, max_training_size, training_examples_steps)
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

        ax = self.mainfig.add_subplot(222)
        ax.title.set_text("Learning Curves")
        ax.set_ylabel("Cost")
        ax.set_xlabel("# Of Training Examples")
        ax.legend(['training set', 'cross validation set'])
        ax.plot(steps, error_training)
        ax.plot(steps, error_validation)

    def save_diagostics(self, folder_path):
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
            
        figure_path = os.path.join(folder_path, 'diagnostics.png')
        self.mainfig.savefig(figure_path)







