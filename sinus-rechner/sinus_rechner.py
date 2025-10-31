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
            zeilen_array, spalten_array = split_array(arr, debug=debug)
            arr = zeilen_array * spalten_array
            if len(arr) == 1:
                break
        fakueltet = arr[0]

    if debug:
        print(f"[factorial] n={n}, fakueltet={fakueltet}")

    return fakueltet


def sin(x, debug=False):
    sin_wert = None
    x %= (2 * np.pi)      # Reduziere x auf den Bereich [0, 2π]

    if x < np.pi / 4:
        # Taylor-Reihe um 0:
        # sin(x) = Σ (-1)^k * x^(2k+1) / (2k+1)!
        n = 6
        coefficent = np.ones(n)
        coefficent[1::2] *= -1                 # (+1, -1, +1, -1, ...)
        exponent = np.arange(1, 2*n, 2)        # 1, 3, 5, ..., (2n-1)
        zaehler = x ** exponent                # x^(2k+1)
        nenner = factorial(exponent, debug=debug)
        sin_wert = np.sum(coefficent * zaehler / nenner)

        if debug:
            print(f"[sin] Bereich: 0 .. π/4")
            print(f"[sin] n={n}")
            print(f"[sin] coefficent={coefficent}")
            print(f"[sin] exponent={exponent}")
            print(f"[sin] zaehler={zaehler}")
            print(f"[sin] nenner={nenner}")
            print(f"[sin] sin_wert={sin_wert}")

    elif np.pi/4 <= x < 3*np.pi/4:
        # sin(x) = cos(π/2 - x)
        sin_wert = cos(np.pi/2 - x, debug=debug)
        if debug:
            print(f"[sin] Bereich: π/4 .. 3π/4")
            print(f"[sin] sin(x) = cos(π/2 - x) -> {sin_wert}")

    elif 3*np.pi/4 <= x < 5*np.pi/4:
        # sin(x) = -sin(x - π)
        sin_wert = -sin(x - np.pi, debug=debug)
        if debug:
            print(f"[sin] Bereich: 3π/4 .. 5π/4")
            print(f"[sin] sin(x) = -sin(x - π) -> {sin_wert}")

    else:
        # 5π/4 <= x < 2π
        # sin(x) = -cos(x - 3π/2)
        sin_wert = -cos(x - 3*np.pi/2, debug=debug)
        if debug:
            print(f"[sin] Bereich: 5π/4 .. 2π")
            print(f"[sin] sin(x) = -cos(x - 3π/2) -> {sin_wert}")

    return round(sin_wert, 10)

def cos(x, debug=False):
    cos_wert = None
    x %= (2 * np.pi)  # Reduziere x auf den Bereich [0, 2π]
    if x < np.pi / 4:
        n = 6  # Anzahl der Terme in der Taylor-Reihe
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

    elif np.pi/4 <= x < np.pi/2:
        cos_wert = sin(np.pi/2 - x, debug=debug)
    elif np.pi/2 <= x < 3*np.pi/4:
        cos_wert = -sin(x - np.pi/2, debug=debug)
    else: 
        # 3π/4 <= x < 2π
        cos_wert = -cos(x - np.pi, debug=debug)

    return round(cos_wert, 10)


def main():
    print(sin(1000, debug=True))
    return None


if __name__ == "__main__":
    main()
