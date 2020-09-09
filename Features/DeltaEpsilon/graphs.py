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
        graphs_extend = []

        # if proof is done
        if self.current_equation == self.epsilon:

            # find delta/epsilon bounds
            input_delta = self.delta_exp.subs(self.epsilon, input_epsilon)

            # is it delta?
            if str(self.delta) == 'delta':

                # is it bounded?
                if self.delta_bound != 0 and input_delta > self.delta_bound:
                    input_delta = self.delta_bound

                # create bounds
                x_upper_bound = self.x0 + input_delta
                x_lower_bound = self.x0 - input_delta
                x_dim = (x, self.x0 - input_delta * 3, self.x0 + input_delta * 3)

            # is it N?
            else:
                if self.x0 == sm.oo:
                    x_lower_bound = input_delta
                    x_upper_bound = None
                    x_dim = (
                        x, x_lower_bound - x_lower_bound * 0.5, x_lower_bound + x_lower_bound * 0.5)
                else:
                    x_lower_bound = None
                    x_upper_bound = input_delta
                    x_dim = (
                        x, x_upper_bound - x_upper_bound * 0.5, x_upper_bound + x_upper_bound * 0.5)

            # is it epsilon?
            if str(self.epsilon) == 'epsilon':
                y_upper_bound = self.limit + input_epsilon
                y_lower_bound = self.limit - input_epsilon
                graphs_extend.append(splot(y_lower_bound, show=False, line_color="red"))
                graphs_extend.append(splot(y_upper_bound, show=False, line_color="red"))
                y_dim = (y, self.limit - input_epsilon * 3, self.limit + input_epsilon * 3)

            # is it M?
            else:
                if self.limit == sm.oo:
                    y_lower_bound = input_epsilon
                    graphs_extend.append(splot(y_lower_bound, show=False, line_color="red"))
                    y_dim = (
                        y, y_lower_bound - y_lower_bound * 0.5, y_lower_bound + y_lower_bound * 0.5)
                else:
                    y_upper_bound = input_epsilon
                    graphs_extend.append(splot(y_upper_bound, show=False, line_color="red"))
                    y_dim = (
                        y, y_upper_bound - y_upper_bound * 0.5, y_upper_bound + y_upper_bound * 0.5)

            # create graphs for the x axis
            graphs_extend.append(plot_implicit(sm.Eq(x, x_upper_bound), x_dim, y_dim,
                                               line_color="blue", show=False))
            graphs_extend.append(plot_implicit(sm.Eq(x, x_lower_bound), x_dim, y_dim,
                                               line_color="blue", show=False))

            fx_graph = splot(self.fx, show=False, xlim=(x_dim[1], x_dim[2]),
                             ylim=(y_dim[1], y_dim[2]), line_color="black")

            # merge graphs
            for graph in graphs_extend:
                fx_graph.extend(graph)
            fx_graph.save(filename)

    def __init__(self):
        """
        ------------------------------------------------------------------
        __init__: Initializes Delta Epsilon graphs component.
        ------------------------------------------------------------------
        """
        pass
