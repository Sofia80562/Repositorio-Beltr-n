using System;

namespace ProyectoListas
{
    class Program
    {
        static void Main(string[] args)
        {
            int opcion;
            do
            {
                Console.Clear();
                Console.WriteLine("===== MENÚ PRINCIPAL =====");
                Console.WriteLine("1. Registro de vehículos");
                Console.WriteLine("2. Lista simple - contar elementos");
                Console.WriteLine("3. Salir");
                Console.Write("Elija una opción: ");
                
                if (!int.TryParse(Console.ReadLine(), out opcion))
                {
                    Console.WriteLine("Entrada inválida. Presione Enter para continuar.");
                    Console.ReadKey();
                    continue;
                }

                switch (opcion)
                {
                    case 1:
                        RegistroVehiculosMenu.Ejecutar();
                        break;
                    case 2:
                        ListaSimpleMenu.Ejecutar();
                        break;
                    case 3:
                        Console.WriteLine("Gracias por usar el programa.");
                        break;
                    default:
                        Console.WriteLine("Opción no válida. Intente de nuevo.");
                        break;
                }

                Console.WriteLine("\nPresione Enter para continuar...");
                Console.ReadKey();

            } while (opcion != 3);
        }
    }
}

