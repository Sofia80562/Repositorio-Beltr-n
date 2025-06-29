class Program
{
    static void Main()
    {
        Console.WriteLine("Seleccione un ejercicio:");
        Console.WriteLine("1 - Mostrar asignaturas");
        Console.WriteLine("2 - Números en orden inverso");
        Console.WriteLine("3 - Contar vocales");
        Console.WriteLine("4 - Mostrar menor y mayor precio");
        Console.WriteLine("5 - Lotería");
        Console.Write("Opción: ");
        
        string opcion = Console.ReadLine();

        switch (opcion)
        {
            case "1":
                var asignaturas = new Asignaturas();
                asignaturas.Mostrar();
                break;

            case "2":
                var inversos = new NumerosInversos();
                inversos.MostrarInverso();
                break;

            case "3":
                Console.Write("Ingrese una palabra: ");
                string palabra = Console.ReadLine();
                var vocales = new ContadorVocales(palabra);
                vocales.Contar();
                break;

            case "4":
                var precios = new Precios();
                precios.MostrarExtremos();
                break;

            case "5":
                var loteria = new Loteria();
                loteria.LeerNumeros();
                loteria.MostrarOrdenados();
                break;

            default:
                Console.WriteLine("Opción no válida.");
                break;
        }
    }
}

