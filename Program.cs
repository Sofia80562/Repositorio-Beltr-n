using System;

namespace RegistroEstudiante
{
    class Program
    {
        static void Main(string[] args)
        {
            // Crear array de teléfonos
            string[] telefonos = new string[3] { "0991234567", "0987654321", "0976543210" };

            // Crear un objeto Estudiante
            Estudiante estudiante = new Estudiante(
                1,
                "Juan",
                "Pérez",
                "Av. Siempre Viva 123",
                telefonos
            );

            // Mostrar la información del estudiante
            estudiante.MostrarInformacion();

            // Para evitar que la consola se cierre enseguida
            Console.ReadKey();
        }
    }
}
