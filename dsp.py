import numpy as np

def generate_features(draw_graphs, raw_data, axes, sampling_freq, scale_axes):
    # features is a 1D array, reshape so we have a matrix
    raw_data = raw_data.reshape(int(len(raw_data) / len(axes)), len(axes))

    features = []
    graphs = []

    # split out the data from all axes
    for ax in range(0, len(axes)):
        X = []
        for ix in range(0, raw_data.shape[0]):
            X.append(float(raw_data[ix][ax]))

        # X now contains only the current axis
        fx = np.array(X)

        # process the signal here
        fx = fx * scale_axes

        # we need to return a 1D array again, so flatten here again
        for f in fx:
            features.append(f)

    return { 'features': features, 'graphs': graphs }
