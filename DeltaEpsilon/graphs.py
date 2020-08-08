import sympy as sm
from sympy.plotting import plot as splot
from sympy import plot_implicit


class Graphs:

    def plot(self, filename, input_epsilon):
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
        x = sm.Symbol('x')
        y = sm.Symbol('y')

        if self.current_equation == self.epsilon:

            # find delta/epsilon bounds
            input_delta = self.delta_exp.subs(self.epsilon, input_epsilon)
            y_upper_bound = self.limit + input_epsilon
            y_lower_bound = self.limit - input_epsilon
            x_upper_bound = self.x0 + input_delta
            x_lower_bound = self.x0 - input_delta

            # create graphs
            y_upper_graph = splot(y_upper_bound, show=False, line_color="red")
            y_lower_graph = splot(y_lower_bound, show=False, line_color="red")
            x_upper_graph = plot_implicit(sm.Eq(x, x_upper_bound),
                                          (x, self.x0 - input_delta * 3,
                                           self.x0 + input_delta * 3),
                                          (y, self.limit - input_epsilon * 3,
                                           self.limit + input_epsilon * 3),
                                          line_color="blue", show=False)
            x_lower_graph = plot_implicit(sm.Eq(x, x_lower_bound),
                                          (x, self.x0 - x_lower_bound * 3,
                                           self.x0 + x_lower_bound * 3),
                                          (y, self.limit - input_epsilon * 3,
                                           self.limit + input_epsilon * 3),
                                          line_color="blue", show=False)

            fx_graph = splot(self.fx, show=False, xlim=(self.x0 - x_lower_bound * 3,
                                                        self.x0 + x_lower_bound * 3),
                             ylim=(self.limit - input_epsilon * 3, self.limit + input_epsilon * 3),
                             line_color="black")

            # plot graphs
            fx_graph.extend(x_lower_graph)
            fx_graph.extend(x_upper_graph)
            fx_graph.extend(y_upper_graph)
            fx_graph.extend(y_lower_graph)
            fx_graph.save(filename)

    def __init__(self):
        """
        ------------------------------------------------------------------
        __init__: Initializes Delta Epsilon graphs component.
        ------------------------------------------------------------------
        """
        pass
