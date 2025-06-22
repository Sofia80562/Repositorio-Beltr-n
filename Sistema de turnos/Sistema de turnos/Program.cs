using System;
using System.Collections.Generic;

namespace AgendaTurnosClinica
{
    // Aquí defino la clase Turno, que representa un turno con sus datos
    class Turno
    {
        // Propiedades para guardar los datos del paciente y del turno
        public string NombrePaciente { get; set; }
        public string Identificacion { get; set; }
        public string Telefono { get; set; }
        public string FechaTurno { get; set; }
        public string HoraTurno { get; set; }
    }

    // Esta clase maneja la lista de turnos y las operaciones que puedo hacer con ella
    class AgendaTurnos
    {
        // Creo una lista para almacenar todos los turnos que registre
        private List<Turno> turnos = new List<Turno>();

        // Método para agregar un nuevo turno pidiéndole los datos al usuario
        public void AgregarTurno()
        {
            // Creo un nuevo objeto Turno para llenarlo con los datos que me den
            Turno nuevoTurno = new Turno();

            // Pido al usuario que ingrese cada dato y los guardo en el nuevo turno
            Console.Write("Ingrese el nombre del paciente: ");
            nuevoTurno.NombrePaciente = Console.ReadLine();

            Console.Write("Ingrese la identificacion (ID): ");
            nuevoTurno.Identificacion = Console.ReadLine();

            Console.Write("Ingrese el telefono: ");
            nuevoTurno.Telefono = Console.ReadLine();

            Console.Write("Ingrese la fecha del turno (dd/mm/aaaa): ");
            nuevoTurno.FechaTurno = Console.ReadLine();

            Console.Write("Ingrese la hora del turno (hh:mm): ");
            nuevoTurno.HoraTurno = Console.ReadLine();

            // Agrego el turno que llené a la lista de turnos
            turnos.Add(nuevoTurno);

            // Confirmo que el turno se agregó correctamente
            Console.WriteLine("Turno agregado exitosamente.\n");
        }

        // Método para mostrar todos los turnos registrados
        public void MostrarTurnos()
        {
            // Si no hay turnos, aviso que la lista está vacía y salgo
            if (turnos.Count == 0)
            {
                Console.WriteLine("No hay turnos registrados.\n");
                return;
            }

            // Si hay turnos, recorro la lista y muestro cada turno con sus datos
            Console.WriteLine("Lista de turnos:");
            foreach (var turno in turnos)
            {
                Console.WriteLine($"Paciente: {turno.NombrePaciente}, ID: {turno.Identificacion}, Tel: {turno.Telefono}, Fecha: {turno.FechaTurno}, Hora: {turno.HoraTurno}");
            }
            Console.WriteLine();
        }
    }

    // Clase principal donde empieza la ejecución del programa
    class Program
    {
        static void Main(string[] args)
        {
            // Creo la agenda para administrar los turnos
            AgendaTurnos agenda = new AgendaTurnos();
            bool salir = false;

            // Hago un menú para que el usuario elija qué hacer
            while (!salir)
            {
                Console.WriteLine("1. Agregar turno");
                Console.WriteLine("2. Mostrar turnos");
                Console.WriteLine("3. Salir");
                Console.Write("Seleccione una opción: ");

                // Leo la opción que ingresa el usuario
                string opcion = Console.ReadLine();

                // Dependiendo de la opción, hago la acción correspondiente
                switch (opcion)
                {
                    case "1":
                        // Llamo al método para agregar un turno nuevo
                        agenda.AgregarTurno();
                        break;
                    case "2":
                        // Llamo al método para mostrar todos los turnos
                        agenda.MostrarTurnos();
                        break;
                    case "3":
                        // Cambio la variable para salir del ciclo y terminar el programa
                        salir = true;
                        break;
                    default:
                        // Si la opción no es válida, aviso al usuario
                        Console.WriteLine("Opción no válida. Intente de nuevo.\n");
                        break;
                }
            }
        }
    }
}
 
