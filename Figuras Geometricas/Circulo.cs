using System;

namespace FigurasGeometricas
{
    // Clase que representa un Círculo
    public class Circulo
    {
        // Radio encapsulado del círculo
        private double radio;

        // Constructor que inicializa el radio
        public Circulo(double radio)
        {
            this.radio = radio;
        }

        // Propiedad para obtener o modificar el radio
        public double Radio
        {
            get { return radio; }
            set { radio = value; }
        }

        // CalcularArea es una función que devuelve un valor double,
        // se utiliza para calcular el área de un círculo,
        // requiere como argumento el radio del círculo encapsulado
        public double CalcularArea()
        {
            return Math.PI * radio * radio;
        }

        // CalcularPerimetro es una función que devuelve un valor double,
        // se utiliza para calcular el perímetro (circunferencia) del círculo
        public double CalcularPerimetro()
        {
            return 2 * Math.PI * radio;
        }
    }
}

