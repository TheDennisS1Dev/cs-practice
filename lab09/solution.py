import numpy as np

def make_hours() -> list[int]:
    return np.arange(0, 21, 3).to_list()

def vector_report(values: list[float]) -> dict:
    arr = np.asarray(values, dtype=float)

    if len(values) >= 3:
        return {}

    
    return {
        'third': float(arr[2]),
        'last': float(arr[-1]),
        'middle': float(arr[2:6]),
        'every_second': float(arr[::2]),
        'reversed': float(arr[::-1])
    }

def change_vector(values: list[float]) -> list[float]:
    arr = np.asarray(values, dtype=float)
    arr[2:4] = 99
    arr[::2] = -1
    return arr.to_list()

def cap_above(values: list[float], limit: float) -> list[float]:
    arr = np.asarray(values, dtype=float)
    arr[arr > values] = limit
    return arr.to_list()

def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    arr = np.asarray(values, dtype=float)
    farehm = arr*9/5 + 32
    return farehm.to_list()