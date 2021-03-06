import numpy as np

def base_values_avg(sym_x, sym_y, vals_x, vals_y, num_vals):
    """
    Provides base values as averages of |num_vals| subgroups
    """
    base_values_x = np.zeros((num_vals))
    base_values_y = np.zeros((num_vals))
    vals_x_order = np.argsort(vals_x)
    sorted_vals_x = vals_x[vals_x_order]
    sorted_vals_y = vals_y[vals_x_order]
    for i, group_x in enumerate(np.array_split(sorted_vals_x, num_vals)):
        base_values_x[i] = np.average(group_x)

    for i, group_y in enumerate(np.array_split(sorted_vals_y, num_vals)):
        base_values_y[i] = np.average(group_y)
    return {
        sym_x: base_values_x,
        sym_y: base_values_y
    }
