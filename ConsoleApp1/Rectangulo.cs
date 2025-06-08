using System;

namespace ConsoleApp1
{
    public class Rectangulo
    {
        private double baseRectangulo;
        private double altura;

        public Rectangulo(double baseRectangulo, double altura)
        {
            this.baseRectangulo = baseRectangulo;
            this.altura = altura;
        }

        public double BaseRectangulo
        {
            get { return baseRectangulo; }
            set { baseRectangulo = value; }
        }

        public double Altura
        {
            get { return altura; }
            set { altura = value; }
        }

        public double CalcularArea()
        {
            return baseRectangulo * altura;
        }

        public double CalcularPerimetro()
        {
            return 2 * (baseRectangulo + altura);
        }
    }
}
