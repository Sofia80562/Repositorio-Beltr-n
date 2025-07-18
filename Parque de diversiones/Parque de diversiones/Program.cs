using System;
using System.Collections.Generic;

namespace ParqueDiversiones
{
    // Clase que representa a una persona que entra a la atracción
    class Persona
    {
        public string Nombre { get; set; }        // Nombre de la persona
        public int NumeroAsiento { get; set; }    // Número de asiento asignado

        // Constructor de la clase Persona
        public Persona(string nombre, int numeroAsiento)
        {
            Nombre = nombre;
            NumeroAsiento = numeroAsiento;
        }

        // Método para representar a la persona en texto
        public override string ToString()
        {
            return $"Asiento #{NumeroAsiento}: {Nombre}";
        }
    }

    // Clase que gestiona la atracción y la asignación de asientos
    class Atraccion
    {
        private Queue<Persona> filaEspera = new Queue<Persona>();   // Cola de espera FIFO
        private List<Persona> asientosAsignados = new List<Persona>(); // Lista de personas con asiento
        private int totalAsientos = 30;  // Capacidad máxima

        // Método para ingresar una persona a la fila
        public void IngresarPersona(string nombre)
        {
            if (asientosAsignados.Count < totalAsientos)
            {
                // Se crea una nueva persona con el próximo número de asiento
                Persona nueva = new Persona(nombre, asientosAsignados.Count + 1);
                filaEspera.Enqueue(nueva);  // Se agrega a la cola
                Console.WriteLine($"{nombre} ingresó a la fila.");
            }
            else
            {
                // Si ya no hay asientos disponibles
                Console.WriteLine("Lo sentimos, todos los asientos han sido ocupados.");
            }
        }

        // Método para asignar asientos a las personas en la fila
        public void AsignarAsientos()
        {
            while (filaEspera.Count > 0 && asientosAsignados.Count < totalAsientos)
            {
                // Se retira una persona de la cola y se le asigna un asiento
                Persona persona = filaEspera.Dequeue();
                asientosAsignados.Add(persona);
                Console.WriteLine($"Asiento asignado a {persona.Nombre}: #{persona.NumeroAsiento}");
            }
        }

        // Método para mostrar un reporte de todos los asientos asignados
        public void ReporteAsientos()
        {
            Console.WriteLine("\n--- Reporte de Asientos Asignados ---");
            foreach (var persona in asientosAsignados)
            {
                Console.WriteLine(persona.ToString());
            }
        }
    }

    // Clase principal que contiene el método Main (punto de entrada del programa)
    class Program
    {
        static void Main(string[] args)
        {
            Atraccion atraccion = new Atraccion();  // Se crea una instancia de la atracción

            // Simula el ingreso de 35 personas a la atracción
            for (int i = 1; i <= 35; i++)
            {
                atraccion.IngresarPersona($"Persona{i}");
            }

            // Se asignan los asientos disponibles
            atraccion.AsignarAsientos();

            // Se muestra un reporte final de asignación
            atraccion.ReporteAsientos();
        }
    }
}

