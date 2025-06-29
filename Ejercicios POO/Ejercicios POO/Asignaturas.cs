using System;
using System.Collections.Generic;

// Clase que contiene la lista de asignaturas
class Asignaturas
{
    // Lista de asignaturas del curso
    private List<string> asignaturas = new List<string> { "Matemáticas", "Física", "Química", "Historia", "Lengua" };

    // Método que imprime la lista
    public void Mostrar()
    {
        Console.WriteLine("Asignaturas del curso:");
        foreach (string asignatura in asignaturas)
        {
            Console.WriteLine("- " + asignatura);
        }
    }
}
