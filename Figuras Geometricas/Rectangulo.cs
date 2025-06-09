using System;

namespace FigurasGeometricas
{
    // Clase que representa un Rectángulo
    public class Rectangulo
    {
        // Base y altura encapsulados del rectángulo
        private double baseRectangulo;
        private double altura;

        // Constructor que inicializa base y altura
        public Rectangulo(double baseRectangulo, double altura)
        {
            this.baseRectangulo = baseRectangulo;
            this.altura = altura;
        }

        // Propiedades para obtener o modificar base y altura
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

        // CalcularArea devuelve un valor double,
        // calcula el área del rectángulo usando base y altura encapsulados
        public double CalcularArea()
        {
            return baseRectangulo * altura;
        }

        // CalcularPerimetro devuelve un valor double,
        // calcula el perímetro del rectángulo
        public double CalcularPerimetro()
        {
            return 2 * (baseRectangulo + altura);
        }
    }
}

