def slices(series, length):
    if not series:
        raise ValueError('Series cannot be empty. Series: {series}')
    if length <= 0:
        raise ValueError(f'Length cannot be negative or zero. Length: {length}')
    if length > len(series):
        raise ValueError(f'Length cannot be longer then series. L:{length} S:{len(series)}')
    
    return [''.join(series[i:i+length]) for i in range(len(series)-length+1)]
