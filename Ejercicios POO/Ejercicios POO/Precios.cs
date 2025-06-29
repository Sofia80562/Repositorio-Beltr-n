using System;
using System.Collections.Generic;
using System.Linq;

// Clase para analizar precios
class Precios
{
    // Lista de precios
    private List<int> precios = new List<int> { 50, 75, 46, 22, 80, 65, 8 };

    // Método que encuentra el menor y mayor
    public void MostrarExtremos()
    {
        int menor = precios.Min(); // Función que obtiene el menor
        int mayor = precios.Max(); // Función que obtiene el mayor

        Console.WriteLine($"El precio menor es: {menor}");
        Console.WriteLine($"El precio mayor es: {mayor}");
    }
}
