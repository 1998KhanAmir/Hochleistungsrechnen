"""
Modul für Aufgabe 3.1
"""
import time
import numpy as np
import cupy as cp

def make_array(array_size = None):
    """
    Erstellt ein array der größe array_size

    Args:
        array_size (int): Parameter der die Zeilen und Spalten
                        der quadratischen Matrix bestimmt
                        Standard wert 2 GB
    Return:
        cupy_array (Array): erstellte  array 
        array_size(int): Zahl der Zeilen und Spalten
        cupy_array_size(float): Größe des Arrays in MB 
    """

    if array_size is None:
        # Größe des Arrays berechnen, um ungefähr 2GB zu haben
        # 2147483648 2GB in binärer Dateneinheit
        array_size = int(np.sqrt((2147483648) / 4))  # 2GB in Bytes, 4 Bytes pro 32-Bit Float

    # NumPy Array erstellen
    numpy_array = np.random.rand(array_size, array_size).astype(np.float32)

    # Arrays Größe berechnen
    numpy_array_size = numpy_array.nbytes/2147483648  # in GB
    return numpy_array, array_size, numpy_array_size

def main():
    """
    Die Hauptfunktion für Aufgabe 3.1
    """
    # Erstellen des Arrays

    numpy_array, array_size, numpy_array_size = make_array()

    print(f"Random array: {numpy_array_size:.2f} GB; ({array_size},{array_size}) elements")

    # Numpy Zeit Messung
    start_time = time.time()
    np.linalg.slogdet(numpy_array)
    end_time = time.time()

    numpy_time = end_time-start_time
    print(f"Walltime using Numpy: {(numpy_time):.3f} s;")

    # Umwandlung in Cupy Array
    cupy_array = cp.asarray(numpy_array)

    # Cupy Zeit Messung
    start_time = time.time()
    cp.linalg.slogdet(cupy_array)
    end_time = time.time()

    cupy_time = end_time-start_time
    print(f"Walltime using CuPy: {(cupy_time):.3f} s;")

    print(f"Speedup factor for NumPy/CuPy: {(numpy_time/cupy_time):.3f}")


if __name__ == "__main__":
    main()
