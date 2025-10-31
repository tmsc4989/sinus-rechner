from asyncio.format_helpers import _format_args_and_kwargs
import time
import numpy as np

def benchmark():
    return time


def split_array(arr, debug=False):
    n = len(arr)
    halb = n // 2
    zeilen_array = arr[:halb]
    spalten_array = arr[halb:]
    if len(zeilen_array) < len(spalten_array):
        zeilen_array = np.append(zeilen_array, 1)

    if debug:
        print(f"[split_array] n={n}, halb={halb}")
        print(f"[split_array] zeilen_array={zeilen_array}")
        print(f"[split_array] spalten_array={spalten_array}")

    return zeilen_array, spalten_array


def factorial(n, debug=False):
    # --- Array-Eingabe (vektorisiert) ---
    if isinstance(n, np.ndarray):
        n = n.astype(int)
        max_n = int(n.max())
        fac = np.empty(max_n + 1, dtype=float)
        fac[0] = 1.0
        if max_n >= 1:
            fac[1:] = np.cumprod(np.arange(1, max_n + 1, dtype=float))

        if debug:
            print(f"[factorial] Arrayeingabe erkannt")
            print(f"[factorial] n={n}")
            print(f"[factorial] fac(0..{max_n})={fac}")

        return fac[n]

    # --- Skalar-Eingabe (deine ursprüngliche Variante) ---
    fakueltet = 1
    if n == 0 or n == 1:
        pass
    elif n < 0:
        raise ValueError("Negative Eingabe für Fakultät nicht definiert.")
    else:
        arr = np.arange(1, n + 1)
        for i in range(10):
            zeilen_array, spalten_array = split_array(arr)
            arr = zeilen_array * spalten_array
            if len(arr) == 1:
                break
        fakueltet = arr[0]

    if debug:
        print(f"[factorial] n={n}, fakueltet={fakueltet}")

    return fakueltet


def sin(x, debug=False):
    sin_wert = None
    if debug:
        print(f"[sin] Eingabe x={x}, Rückgabe sin_wert={sin_wert}")
    return sin_wert


def cos(x, debug=False):
    n = 10
    coefficent = np.ones(n)
    coefficent[1::2] *= -1
    exponent = np.arange(0, 2*n, 2)
    zaehler = x**exponent
    nenner = factorial(exponent, debug=debug)
    cos_wert = np.sum(coefficent * zaehler / nenner)

    if debug:
        print(f"[cos] n={n}")
        print(f"[cos] coefficent={coefficent}")
        print(f"[cos] exponent={exponent}")
        print(f"[cos] zaehler={zaehler}")
        print(f"[cos] nenner={nenner}")
        print(f"[cos] cos_wert={cos_wert}")

    return cos_wert


def main():
    print(cos(5, debug=True))
    return None


if __name__ == "__main__":
    main()
