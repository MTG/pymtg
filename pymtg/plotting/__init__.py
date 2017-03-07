COLORS = ['#FF4500', '#FFA500', '#6B8E23', '#32CD32', '#FFD700', '#008B8B', '#00008B', '#B22222', '#1E90FF', '#FF1493',
          '#008000', '#DAA520', '#2F4F4F', '#8B0000', '#FF8C00', '#8B008B', '#A9A9A9', '#B8860B', '#00FFFF', '#6495ED',
          '#FF7F50', '#D2691E', '#7FFF00', '#DEB887', '#8A2BE2', '#0000FF', '#000000']


def color_at_index(index):
    """
    Return hexadecimal color at given ``index`` from COLORS.
    ``index`` wraps if larger than the length of COLORS.
    """
    return COLORS[index % len(COLORS)]
