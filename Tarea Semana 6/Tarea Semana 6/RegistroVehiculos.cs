namespace ProyectoListas
{
    public class Vehiculo
    {
        public string Placa;
        public string Marca;
        public string Modelo;
        public int Año;
        public double Precio;
        public Vehiculo Siguiente;

        public Vehiculo(string placa, string marca, string modelo, int año, double precio)
        {
            Placa = placa;
            Marca = marca;
            Modelo = modelo;
            Año = año;
            Precio = precio;
            Siguiente = null;
        }
    }

    public class ListaVehiculos
    {
        private Vehiculo cabeza;

        public void Agregar(string placa, string marca, string modelo, int año, double precio)
        {
            Vehiculo nuevo = new Vehiculo(placa, marca, modelo, año, precio);
            nuevo.Siguiente = cabeza;
            cabeza = nuevo;
        }

        public void BuscarPorPlaca(string placa)
        {
            Vehiculo actual = cabeza;
            while (actual != null)
            {
                if (actual.Placa.Equals(placa, System.StringComparison.OrdinalIgnoreCase))
                {
                    Mostrar(actual);
                    return;
                }
                actual = actual.Siguiente;
            }
            System.Console.WriteLine("Vehículo no encontrado.");
        }

        public void VerPorAño(int año)
        {
            Vehiculo actual = cabeza;
            bool encontrado = false;
            while (actual != null)
            {
                if (actual.Año == año)
                {
                    Mostrar(actual);
                    encontrado = true;
                }
                actual = actual.Siguiente;
            }
            if (!encontrado)
                System.Console.WriteLine("No hay vehículos registrados para ese año.");
        }

        public void VerTodos()
        {
            Vehiculo actual = cabeza;
            if (actual == null)
            {
                System.Console.WriteLine("No hay vehículos registrados.");
                return;
            }
            while (actual != null)
            {
                Mostrar(actual);
                actual = actual.Siguiente;
            }
        }

        public int Contar()
        {
            int contador = 0;
            Vehiculo actual = cabeza;
            while (actual != null)
            {
                contador++;
                actual = actual.Siguiente;
            }
            return contador;
        }

        private void Mostrar(Vehiculo v)
        {
            System.Console.WriteLine($"Placa: {v.Placa}, Marca: {v.Marca}, Modelo: {v.Modelo}, Año: {v.Año}, Precio: {v.Precio:C}");
        }
    }

    public static class RegistroVehiculosMenu
    {
        public static void Ejecutar()
        {
            ListaVehiculos lista = new ListaVehiculos();
            int opcion;

            do
            {
                System.Console.Clear();
                System.Console.WriteLine("=== MENÚ REGISTRO DE VEHÍCULOS ===");
                System.Console.WriteLine("1. Agregar vehículo");
                System.Console.WriteLine("2. Buscar vehículo por placa");
                System.Console.WriteLine("3. Ver vehículos por año");
                System.Console.WriteLine("4. Ver todos los vehículos");
                System.Console.WriteLine("5. Ver cantidad de vehículos");
                System.Console.WriteLine("6. Volver al menú principal");
                System.Console.Write("Opción: ");
                if (!int.TryParse(System.Console.ReadLine(), out opcion)) continue;

                switch (opcion)
                {
                    case 1:
                        System.Console.Write("Placa: ");
                        string placa = System.Console.ReadLine();
                        System.Console.Write("Marca: ");
                        string marca = System.Console.ReadLine();
                        System.Console.Write("Modelo: ");
                        string modelo = System.Console.ReadLine();
                        System.Console.Write("Año: ");
                        int año = int.Parse(System.Console.ReadLine());
                        System.Console.Write("Precio: ");
                        double precio = double.Parse(System.Console.ReadLine());
                        lista.Agregar(placa, marca, modelo, año, precio);
                        System.Console.WriteLine("Vehículo agregado.");
                        break;
                    case 2:
                        System.Console.Write("Ingrese la placa: ");
                        lista.BuscarPorPlaca(System.Console.ReadLine());
                        break;
                    case 3:
                        System.Console.Write("Ingrese el año: ");
                        lista.VerPorAño(int.Parse(System.Console.ReadLine()));
                        break;
                    case 4:
                        lista.VerTodos();
                        break;
                    case 5:
                        System.Console.WriteLine($"Cantidad de vehículos: {lista.Contar()}");
                        break;
                    case 6:
                        return;
                    default:
                        System.Console.WriteLine("Opción inválida.");
                        break;
                }

                System.Console.WriteLine("Presione Enter para continuar...");
                System.Console.ReadKey();

            } while (opcion != 6);
        }
    }
}


