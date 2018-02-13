import numpy as np


def smooth(x, window_len=11, window='hanning', preserve_length=True):
    """Smooth the data using a window with requested size.

    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal 
    (with the window size) in both ends so that transient parts are minimized
    in the beginning and end part of the output signal.

    The code here is an adaptation of the smoothing code from Scipy Cookbook:
    http://scipy-cookbook.readthedocs.io/items/SignalSmooth.html
    
    Args:
        x (array): The input signal 
        window_len (int): The dimension of the smoothing window. Should be an odd integer.
        window (string): The type of window from 'flat', 'hanning', 'hamming', 'bartlett', 
            'blackman'. Flat window will produce a moving average smoothing.
        preserve_length (bool): Whether the length oh the output signal should be the same
            as the length of the input signal (default=True).

    Returns:
        (array): The smoothed signal
        
    Examples:
        >>> smooth([0, 1, 0, 1, 0, 1], 4)
        array([ 0.5,  0.5,  0.5,  0.5,  0.5,  0.5])
    """
    if type(x) != np.array:
        x = np.array(x)
    if x.ndim != 1:
        raise (ValueError, "Smooth only accepts 1 dimension arrays.")
    if x.size < window_len:
        raise (ValueError, "Input vector needs to be bigger than window size.")
    if window_len<3:
        return x
    if window not in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise (ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")

    s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
    if window == 'flat': #moving average
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')
    y=np.convolve(w/w.sum(),s,mode='valid')
    if preserve_length:
        return y[(window_len//2-1):-(window_len//2)][:x.size]
    return y


def linear_approximation(x, include_coeffs=False):
    """Compute the least squares polynomial fit of first degree of x (linear approximation).

    This function returns the linear approximation as a signal of the same length of x.
    If requested, the function can also return the linear approximation coefficients as
    returned by Numpy's 'polyfit' function. For more details in the method used for the linear
    approximation, see https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html.

    Args:
        x (array): The input signal 
        include_coeffs (bool): Whether to return the computed linear approximation coefficients 
            along with the approximated signal (default=False).

    Returns:
        (array): The linear approximation of then input signal
        
    Examples:
        >>> linear_approximation([1, 1, 1])
        array([ 1.,  1.,  1.])
        >>> linear_approximation([0, 1, 2, 3, 4, 5])
        array([ 0.,  1.,  2.,  3.,  4.,  5.])
        >>> linear_approximation([1, 2, 4, 8, 16])
        array([ -1. ,   2.6,   6.2,   9.8,  13.4])
        >>> linear_approximation([1, 2, 4, 8, 16], include_coeffs=True)
        (array([ -1. ,   2.6,   6.2,   9.8,  13.4]), (3.6000000000000001, -0.99999999999999778))
    """
    a, b = np.polyfit(range(0, len(x)), x, 1)
    x_fit = np.array([a*i + b for i in range(0, len(x))])
    if not include_coeffs:
        return x_fit
    else:
        return x_fit, (a, b)


