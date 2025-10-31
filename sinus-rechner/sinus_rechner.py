from asyncio.format_helpers import _format_args_and_kwargs
import time
import numpy as np

def benchmark():

    return time

def split_array(arr):
    n = len(arr)
    halb = n // 2

    zeilen_array = arr[:halb]
    spalten_array = arr[halb:]
    if len(zeilen_array) < len(spalten_array):
        zeilen_array = np.append(zeilen_array, 1)
    return zeilen_array, spalten_array


def factorial(n, debug=False):
    fakueltet = 1
    if n == 0 or n == 1:
        pass
    elif n < 0:
        raise ValueError(".")
    else:
        arr = np.arange(1, n + 1)
        if debug:
            print(f"arr: {arr}")
        for i in range(10):
            zeilen_array, spalten_array = split_array(arr)
            arr = zeilen_array * spalten_array
            if debug:
                print(f"i: {i}, zeilen_arr: {zeilen_array}, spalten_arr: {spalten_array}")
                print(f"i: {i}, arr: {arr}")
            if len(arr) == 1:
                break
        fakueltet = arr[0]

    return fakueltet

def sin(x):
    sin_wert = 0
    return sin_wert

def main():
    print(factorial(25, debug=True))
    return None

if __name__ == "__main__":
    main()