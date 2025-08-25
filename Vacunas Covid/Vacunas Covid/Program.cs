using System;
using System.Collections.Generic;
using System.Linq;

class Programa
{
    static void Main()
    {
        // Crear un conjunto de 500 ciudadanos a los cuales nombraremos "personitas"
        var personitas = new HashSet<string>();
        for (int i = 1; i <= 500; i++)
        {
            personitas.Add($"Personita {i}");
        }

        // Crear un conjunto de "personitas" vacunadas con Pfizer (75 personas)
        var vacunadosPfizer = new HashSet<string>();
        for (int i = 1; i <= 75; i++)
        {
            vacunadosPfizer.Add($"Personita {i}");
        }

        // Crear un conjunto de "personitas" vacunadas con AstraZeneca (75 personas)
        var vacunadosAstraZeneca = new HashSet<string>();
        for (int i = 50; i <= 125; i++)
        {
            vacunadosAstraZeneca.Add($"Personita {i}");
        }

        // Personitas que no se han vacunado (diferencia)
        var noVacunados = personitas.Except(vacunadosPfizer.Union(vacunadosAstraZeneca)).ToList();

        // Personitas que han recibido ambas dosis (intersección de Pfizer y AstraZeneca)
        var ambosVacunados = vacunadosPfizer.Intersect(vacunadosAstraZeneca).ToList();

        // Personitas que solo han recibido Pfizer (diferencia entre Pfizer y AstraZeneca)
        var soloPfizer = vacunadosPfizer.Except(vacunadosAstraZeneca).ToList();

        // Personitas que solo han recibido AstraZeneca (diferencia entre AstraZeneca y Pfizer)
        var soloAstraZeneca = vacunadosAstraZeneca.Except(vacunadosPfizer).ToList();

        // Mostrar resultados
        Console.WriteLine($"Personitas que no se han vacunado: {noVacunados.Count}");
        Console.WriteLine($"Personitas que han recibido ambas dosis: {ambosVacunados.Count}");
        Console.WriteLine($"Personitas que solo han recibido Pfizer: {soloPfizer.Count}");
        Console.WriteLine($"Personitas que solo han recibido AstraZeneca: {soloAstraZeneca.Count}");

        // Opcional: Ver los resultados
        Console.WriteLine("\nPersonitas que no se han vacunado: ");
        noVacunados.ForEach(Console.WriteLine);

        Console.WriteLine("\nPersonitas que han recibido ambas dosis: ");
        ambosVacunados.ForEach(Console.WriteLine);

        Console.WriteLine("\nPersonitas que solo han recibido Pfizer: ");
        soloPfizer.ForEach(Console.WriteLine);

        Console.WriteLine("\nPersonitas que solo han recibido AstraZeneca: ");
        soloAstraZeneca.ForEach(Console.WriteLine);
    }
}

