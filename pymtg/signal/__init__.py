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
        (array): Tthe smoothed signal
        
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
