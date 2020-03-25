"""
Contains TrainingDiagnostic class
"""
import os

import matplotlib.pyplot as plt

class TrainingDiagnostics():
    """
    Contains functionality to generate graphs
    for ML model diagnostics
    """
    def __init__(self):
        plt.cla()
        self.mainfig = plt.figure()

    def plot_cost(self, cost_values):
        """Plots given costs on a graph"""
        graph_ax = self.mainfig.add_subplot(221)
        graph_ax.title.set_text("Cost over time")
        graph_ax.set_ylabel("Cost")
        graph_ax.set_xlabel("iteration step")
        graph_ax.plot(cost_values)

    def plot_learning_curve(self, x_matrix, y_vector, x_matrix_validation, y_vector_validation,
                            model, max_training_size=None, training_examples_steps=100):
        """Plots learning curve of model on a graph"""
        max_training_size = x_matrix.shape[0] if max_training_size is None else max_training_size
        error_training = []
        error_validation = []
        steps = range(training_examples_steps, max_training_size, training_examples_steps)
        for i in steps:
            x_subset = x_matrix[:i, :]
            y_subset = y_vector[:i]
            model.train(x_subset, y_subset)

            cost_hypothesis = model.hypothesis(x_subset, model.theta)
            cost_training_set = model.cost_function(cost_hypothesis, y_subset)
            error_training.append(cost_training_set)

            cost_validation_hypothesis = model.hypothesis(x_matrix_validation, model.theta)
            cost_validation_set = model.cost_function(cost_validation_hypothesis,
                                                      y_vector_validation)
            error_validation.append(cost_validation_set)

        graph_ax = self.mainfig.add_subplot(222)
        graph_ax.title.set_text("Learning Curves")
        graph_ax.set_ylabel("Cost")
        graph_ax.set_xlabel("# Of Training Examples")
        graph_ax.plot(steps, error_training, label="Training Set")
        graph_ax.plot(steps, error_validation, label="Validation Set")
        graph_ax.legend(loc="upper right")


    def save_diagostics(self, folder_path):
        """Saves generated diagnostics to disk"""
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        figure_path = os.path.join(folder_path, 'diagnostics.png')
        self.mainfig.savefig(figure_path)
