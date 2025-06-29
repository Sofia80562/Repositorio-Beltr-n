using System;
using System.Collections.Generic;
using System.Linq;

// Clase para invertir y mostrar los números
class NumerosInversos
{
    // Lista con números del 1 al 10
    private List<int> numeros = Enumerable.Range(1, 10).ToList();

    // Método que invierte y muestra la lista
    public void MostrarInverso()
    {
        numeros.Reverse(); // Invertir el orden de los elementos
        Console.WriteLine("Números del 1 al 10 en orden inverso:");
        Console.WriteLine(string.Join(", ", numeros)); // Imprimir separados por coma
    }
}
