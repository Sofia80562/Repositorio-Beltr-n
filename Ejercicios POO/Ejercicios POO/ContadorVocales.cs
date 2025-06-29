using System;
using System.Collections.Generic;

// Clase para contar vocales en una palabra
class ContadorVocales
{
    private string palabra;

    // Constructor que recibe la palabra del usuario
    public ContadorVocales(string palabra)
    {
        this.palabra = palabra.ToLower(); // Convertir todo a minúsculas para facilitar el conteo
    }

    // Método que cuenta cuántas veces aparece cada vocal
    public void Contar()
    {
        var vocales = new Dictionary<char, int> {
            { 'a', 0 }, { 'e', 0 }, { 'i', 0 }, { 'o', 0 }, { 'u', 0 }
        };

        foreach (char c in palabra)
        {
            if (vocales.ContainsKey(c))
            {
                vocales[c]++; // Aumentar contador de vocal correspondiente
            }
        }

        // Mostrar resultados
        Console.WriteLine("Frecuencia de vocales:");
        foreach (var v in vocales)
        {
            Console.WriteLine($"{v.Key}: {v.Value}");
        }
    }
}
