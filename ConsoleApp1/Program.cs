using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Circulo circulo = new Circulo(5);
            Rectangulo rectangulo = new Rectangulo(4, 3);

            Console.WriteLine("Círculo:");
            Console.WriteLine($"Radio: {circulo.Radio}");
            Console.WriteLine($"Área: {circulo.CalcularArea()}");
            Console.WriteLine($"Perímetro: {circulo.CalcularPerimetro()}");

            Console.WriteLine("\nRectángulo:");
            Console.WriteLine($"Base: {rectangulo.BaseRectangulo}");
            Console.WriteLine($"Altura: {rectangulo.Altura}");
            Console.WriteLine($"Área: {rectangulo.CalcularArea()}");
            Console.WriteLine($"Perímetro: {rectangulo.CalcularPerimetro()}");
        }
    }
}
