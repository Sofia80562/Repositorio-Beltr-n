using System;
using FigurasGeometricas;

namespace FigurasGeometricasApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Programa Figuras Geométricas ===");

            // Crear un círculo y calcular área y perímetro
            Console.WriteLine("\nCreando un círculo...");
            Console.Write("Ingrese el radio del círculo: ");
            double radio = Convert.ToDouble(Console.ReadLine());
            Circulo circulo = new Circulo(radio);
            Console.WriteLine($"Área del círculo: {circulo.CalcularArea():F2}");
            Console.WriteLine($"Perímetro del círculo: {circulo.CalcularPerimetro():F2}");

            // Crear un rectángulo y calcular área y perímetro
            Console.WriteLine("\nCreando un rectángulo...");
            Console.Write("Ingrese la base del rectángulo: ");
            double baseRect = Convert.ToDouble(Console.ReadLine());
            Console.Write("Ingrese la altura del rectángulo: ");
            double altura = Convert.ToDouble(Console.ReadLine());
            Rectangulo rectangulo = new Rectangulo(baseRect, altura);
            Console.WriteLine($"Área del rectángulo: {rectangulo.CalcularArea():F2}");
            Console.WriteLine($"Perímetro del rectángulo: {rectangulo.CalcularPerimetro():F2}");

            Console.WriteLine("\nPresione cualquier tecla para salir...");
            Console.ReadKey();
        }
    }
}

