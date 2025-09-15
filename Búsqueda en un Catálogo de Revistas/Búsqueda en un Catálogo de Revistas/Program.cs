using System;
using System.Collections.Generic;

namespace CatalogoRevistas
{
    class Program
    {
        // Lista que contiene los títulos del catálogo
        static List<string> catalogo = new List<string>
        {
            "National Geographic",
            "Time",
            "Scientific American",
            "Nature",
            "Forbes",
            "The Economist",
            "Vogue",
            "People",
            "Reader's Digest",
            "Popular Science"
        };

        static void Main(string[] args)
        {
            int opcion;

            do
            {
                Console.Clear();
                Console.WriteLine("=== Catálogo de Revistas ===");
                Console.WriteLine("1. Buscar título de revista");
                Console.WriteLine("2. Salir");
                Console.Write("Seleccione una opción: ");

                // Validar entrada
                if (!int.TryParse(Console.ReadLine(), out opcion))
                {
                    Console.WriteLine("Opción inválida. Presione una tecla para continuar...");
                    Console.ReadKey();
                    continue;
                }

                switch (opcion)
                {
                    case 1:
                        BuscarRevista();
                        break;
                    case 2:
                        Console.WriteLine("Saliendo...");
                        break;
                    default:
                        Console.WriteLine("Opción inválida. Presione una tecla para continuar...");
                        Console.ReadKey();
                        break;
                }

            } while (opcion != 2);
        }

        /// <summary>
        /// Solicita al usuario un título y realiza la búsqueda en el catálogo
        /// </summary>
        static void BuscarRevista()
        {
            Console.Clear();
            Console.WriteLine("=== Buscar Revista ===");
            Console.Write("Ingrese el título de la revista a buscar: ");
            string titulo = Console.ReadLine();

            // Llamada a búsqueda recursiva
            bool encontrado = BuscarRecursiva(catalogo, titulo, 0);

            if (encontrado)
                Console.WriteLine("\nResultado: Encontrado");
            else
                Console.WriteLine("\nResultado: No encontrado");

            Console.WriteLine("\nPresione una tecla para volver al menú...");
            Console.ReadKey();
        }

        /// <summary>
        /// Búsqueda recursiva en la lista
        /// </summary>
        /// <param name="lista">Lista de revistas</param>
        /// <param name="titulo">Título a buscar</param>
        /// <param name="indice">Índice actual en la recursión</param>
        /// <returns>True si se encuentra, False si no</returns>
        static bool BuscarRecursiva(List<string> lista, string titulo, int indice)
        {
            // Caso base: se terminó la lista
            if (indice >= lista.Count)
                return false;

            // Comparación (ignorando mayúsculas/minúsculas)
            if (string.Equals(lista[indice], titulo, StringComparison.OrdinalIgnoreCase))
                return true;

            // Llamada recursiva
            return BuscarRecursiva(lista, titulo, indice + 1);
        }
    }
}

