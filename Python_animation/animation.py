import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(data, dur=10, y_lims="static", x_axis=None, t_axis=None):
    """
    Animates a one-dimensional plot with N points over T timesteps.

    data   -- Two-dimensional (T,N) array with the plots over time.
    dur    -- Duration of animation in seconds.
    y_lims -- Limits on y-axis. "static", "dynamic", or list [y_min, y_max].
                                          (dynamic won't update y-axes, sadly).
    x_axis -- Optional x-array of shape(N).
    t_axis -- Optional t-array of shape(T).
    """

    T, N = np.shape(data)

    if np.shape(x_axis) == (N,):
        pass
    elif x_axis is None:
        x_axis = np.arange(N)
    else:
        raise ValueError("Shape of x_axis doesn't match data:", np.shape(x_axis), (N,))

    if np.shape(t_axis) == (T,):
        pass
    elif t_axis is None:
        t_axis = np.arange(T)
    else:
        raise ValueError("Shape of t_axis doesn't match data:", np.shape(t_axis), (T,))

    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'r-', animated=True)

    interval = 1000*float(dur)/T

    text = ax.text(0.8,0.9,"",transform=ax.transAxes)

    def init():
        ax.set_xlim(x_axis[0], x_axis[-1])

        if type(y_lims) == list and len(y_lims) == 2:
            ax.set_ylim(y_lims[0], y_lims[1])
        elif y_lims is "static":
            ax.set_ylim(1.1*np.min(data), 1.1*np.max(data))
        elif y_lims is "dynamic":
            ax.set_autoscale_on(True)
            ax.set_ylim(1.1*np.min(data[0]), 1.1*np.max(data[0]))
        else:
            raise ValueError("Unable to recognize y_lims parameter", y_lims)
        return ln,

    def update(frame):
        i = int(frame)
        xdata = x_axis
        ydata = data[i]
        ln.set_data(xdata, ydata)
        if y_lims is "dynamic":
            ax.set_ylim(1.1*np.min(ydata), 1.1*np.max(ydata))
        text.set_text("t = %g" % t[i])
        return ln, text,

    ani = FuncAnimation(fig, update, frames=T,
        init_func=init, blit=True, interval=interval)

    plt.show()


if __name__ == "__main__":
    T = 2000
    N = 400
    x = np.linspace(-10, 10, N)
    t = np.linspace(0, 4, T)
    data = np.zeros((T, N))
    print(type(data))
    for i in range(T):
        data[i] = np.sin(2*x - 40*t[i])
    animate(data, x_axis=x, y_lims="dynamic", t_axis=t)