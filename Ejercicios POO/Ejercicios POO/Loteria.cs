using System;
using System.Collections.Generic;

// Clase para capturar y ordenar números ganadores
class Loteria
{
    private List<int> numeros;

    // Método para pedir los números al usuario
    public void LeerNumeros()
    {
        numeros = new List<int>();
        Console.WriteLine("Ingrese 6 números ganadores de la lotería:");

        // Ciclo para capturar 6 números
        while (numeros.Count < 6)
        {
            Console.Write($"Número {numeros.Count + 1}: ");
            if (int.TryParse(Console.ReadLine(), out int n)) // Validación de número
                numeros.Add(n);
            else
                Console.WriteLine("Entrada inválida. Intente nuevamente.");
        }
    }

    // Método para mostrar los números ordenados
    public void MostrarOrdenados()
    {
        numeros.Sort(); // Ordenar la lista
        Console.WriteLine("Números ganadores ordenados:");
        Console.WriteLine(string.Join(", ", numeros));
    }
}
