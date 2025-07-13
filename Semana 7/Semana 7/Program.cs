using System;

class Program
{
    static void Main()
    {
        int opcion;

        do
        {
            Console.Clear();
            Console.WriteLine("=== MENÚ PRINCIPAL ===");
            Console.WriteLine("1. Verificar paréntesis balanceados");
            Console.WriteLine("2. Resolver Torres de Hanoi");
            Console.WriteLine("0. Salir");
            Console.Write("Seleccione una opción: ");
            
            if (!int.TryParse(Console.ReadLine(), out opcion))
            {
                Console.WriteLine("Entrada inválida.");
                opcion = -1;
            }

            Console.Clear();

            switch (opcion)
            {
                case 1:
                    VerificacionParentesis.Ejecutar();
                    break;
                case 2:
                    TorresDeHanoi.Ejecutar();
                    break;
                case 0:
                    Console.WriteLine("¡Hasta luego!");
                    break;
                default:
                    Console.WriteLine("Opción no válida.");
                    break;
            }

            if (opcion != 0)
            {
                Console.WriteLine("\nPresiona una tecla para continuar...");
                Console.ReadKey();
            }

        } while (opcion != 0);
    }
}

