namespace ProyectoListas
{
    public class Nodo
    {
        public int Dato;
        public Nodo Siguiente;

        public Nodo(int dato)
        {
            Dato = dato;
            Siguiente = null;
        }
    }

    public class ListaSimple
    {
        private Nodo cabeza;

        public void Agregar(int dato)
        {
            Nodo nuevo = new Nodo(dato);
            nuevo.Siguiente = cabeza;
            cabeza = nuevo;
        }

        public int Contar()
        {
            int contador = 0;
            Nodo actual = cabeza;
            while (actual != null)
            {
                contador++;
                actual = actual.Siguiente;
            }
            return contador;
        }

        public void Mostrar()
        {
            Nodo actual = cabeza;
            if (actual == null)
            {
                System.Console.WriteLine("La lista está vacía.");
                return;
            }

            System.Console.WriteLine("Lista:");
            while (actual != null)
            {
                System.Console.WriteLine($"- {actual.Dato}");
                actual = actual.Siguiente;
            }
        }
    }

    public static class ListaSimpleMenu
    {
        public static void Ejecutar()
        {
            ListaSimple lista = new ListaSimple();
            int opcion;

            do
            {
                System.Console.Clear();
                System.Console.WriteLine("=== MENÚ LISTA SIMPLE ===");
                System.Console.WriteLine("1. Agregar número");
                System.Console.WriteLine("2. Mostrar lista");
                System.Console.WriteLine("3. Contar elementos");
                System.Console.WriteLine("4. Volver al menú principal");
                System.Console.Write("Opción: ");
                if (!int.TryParse(System.Console.ReadLine(), out opcion)) continue;

                switch (opcion)
                {
                    case 1:
                        System.Console.Write("Ingrese número: ");
                        int dato = int.Parse(System.Console.ReadLine());
                        lista.Agregar(dato);
                        System.Console.WriteLine("Número agregado.");
                        break;
                    case 2:
                        lista.Mostrar();
                        break;
                    case 3:
                        System.Console.WriteLine($"Cantidad de elementos: {lista.Contar()}");
                        break;
                    case 4:
                        return;
                    default:
                        System.Console.WriteLine("Opción inválida.");
                        break;
                }

                System.Console.WriteLine("Presione Enter para continuar...");
                System.Console.ReadKey();

            } while (opcion != 4);
        }
    }
}
