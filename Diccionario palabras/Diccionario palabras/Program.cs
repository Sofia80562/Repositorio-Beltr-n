using System;
using System.Collections.Generic;
using System.Globalization;

class Program
{
    // Diccionario con las palabras de español a inglés
    static Dictionary<string, string> diccionarioEspañolAIngles = new Dictionary<string, string>
    {
        { "tiempo", "Time" },
        { "persona", "Person" },
        { "año", "Year" },
        { "camino", "Way" },
        { "día", "Day" },
        { "cosa", "Thing" },
        { "hombre", "Man" },
        { "mundo", "World" },
        { "vida", "Life" },
        { "mano", "Hand" },
        { "parte", "Part" },
        { "niño", "Child" },
        { "niña", "Child" },
        { "ojo", "Eye" },
        { "mujer", "Woman" },
        { "lugar", "Place" },
        { "trabajo", "Work" },
        { "semana", "Week" },
        { "caso", "Case" },
        { "punto", "Point" },
        { "gobierno", "Government" },
        { "empresa", "Company" },
        { "compañía", "Company" }
    };

    static void Main(string[] args)
    {
        int opcion;

        do
        {
            Console.Clear();
            MostrarMenu();
            opcion = ObtenerOpcion();

            switch (opcion)
            {
                case 1:
                    TraducirFrase();
                    break;
                case 2:
                    AgregarPalabra();
                    break;
                case 0:
                    Console.WriteLine("Saliendo...");
                    break;
                default:
                    Console.WriteLine("Opción no válida.");
                    break;
            }

            if (opcion != 0)
            {
                Console.WriteLine("Presione cualquier tecla para continuar...");
                Console.ReadKey();
            }

        } while (opcion != 0);
    }

    static void MostrarMenu()
    {
        Console.WriteLine("==================== MENÚ ====================");
        Console.WriteLine("1. Traducir una frase");
        Console.WriteLine("2. Agregar palabras al diccionario");
        Console.WriteLine("0. Salir");
        Console.Write("Seleccione una opción: ");
    }

    static int ObtenerOpcion()
    {
        int opcion;
        while (!int.TryParse(Console.ReadLine(), out opcion) || opcion < 0 || opcion > 2)
        {
            Console.Write("Opción inválida. Intente nuevamente: ");
        }
        return opcion;
    }

    static void TraducirFrase()
    {
        Console.Write("Frase ingresada: ");
        string frase = Console.ReadLine();

        string[] palabras = frase.Split(' ');

        // Usamos InvariantCulture para asegurar que la comparación sea consistente en todos los casos
        for (int i = 0; i < palabras.Length; i++)
        {
            string palabra = palabras[i].ToLower(CultureInfo.InvariantCulture);  // Convertimos a minúsculas

            // Comprobar si la palabra está en el diccionario de español a inglés
            if (diccionarioEspañolAIngles.ContainsKey(palabra))
            {
                palabras[i] = diccionarioEspañolAIngles[palabra];
            }
        }

        Console.WriteLine("Traducción esperada: " + string.Join(" ", palabras));
    }

    static void AgregarPalabra()
    {
        Console.Write("Ingrese la palabra en español: ");
        string palabraEspañol = Console.ReadLine();

        Console.Write("Ingrese la traducción en inglés: ");
        string palabraIngles = Console.ReadLine();

        // Comprobar si la palabra ya existe en el diccionario
        if (!diccionarioEspañolAIngles.ContainsKey(palabraEspañol))
        {
            diccionarioEspañolAIngles.Add(palabraEspañol, palabraIngles);
            Console.WriteLine("Palabra añadida exitosamente.");
        }
        else
        {
            Console.WriteLine("La palabra ya existe en el diccionario.");
        }
    }
}
