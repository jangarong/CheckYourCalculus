import sympy as sm
import numpy as np
import matplotlib.pyplot as plt


class Graphs:

    def moving_delta_epsilon(self, filename):
        """
        ------------------------------------------------------------------
        moving_delta_epsilon: If the associated proof has been finished,
        it will create a gif of the delta-epsilon lines.
        ------------------------------------------------------------------
        Parameters:
            filename - where to save graph
        ------------------------------------------------------------------
        """
        # we need to consider the following cases:
        # delta epsilon proofs => regular DONE
        # N/M or both option
        # mins on delta/epsilon/N/M?

        # issues/things to consider:
        #   vertical delta lines not working
        #   too much memory being consumed due to plotting.
        #   directory vs. file

        if self.current_equation == self.epsilon:
            # for temp_epsilon in np.arange(10.0, 0.0, -0.1):
            for temp_epsilon in [3]:

                # find delta/epsilon bounds
                y_upper_bound = self.limit + temp_epsilon
                y_lower_bound = self.limit - temp_epsilon
                # x_upper_bound = self.x0 + self.delta_exp.subs({str(self.epsilon), temp_epsilon})
                # x_lower_bound = self.x0 - self.delta_exp.subs({str(self.epsilon), temp_epsilon})

                # create graphs
                y_upper_graph = sm.plot(y_upper_bound, show=False)
                y_lower_graph = sm.plot(y_lower_bound, show=False)
                # x_upper_graph = plt.axvline(x=x_upper_bound)
                # x_lower_graph = plt.axvline(x=x_lower_bound)
                graph = sm.plot(self.fx, show=False)
                # graph.extend(y_upper_graph, y_lower_graph, x_upper_graph, x_lower_graph)
                graph.extend(y_upper_graph)
                graph.extend(y_lower_graph)
                graph.save(filename)

    def __init__(self):
        """
        ------------------------------------------------------------------
        __init__: Initializes Delta Epsilon graphs component.
        ------------------------------------------------------------------
        """
        pass
