using System;
using System.Collections.Generic;

public static class VerificacionParentesis
{
    public static void Ejecutar()
    {
        Console.WriteLine("Ingrese una expresión matemática:");
        string? expresion = Console.ReadLine();

        if (expresion != null && EstaBalanceado(expresion))
            Console.WriteLine("Fórmula balanceada.");
        else
            Console.WriteLine("Fórmula desbalanceada.");
    }

    private static bool EstaBalanceado(string expresion)
    {
        Stack<char> pila = new Stack<char>();

        foreach (char c in expresion)
        {
            if (c == '(' || c == '{' || c == '[')
                pila.Push(c);
            else if (c == ')' || c == '}' || c == ']')
            {
                if (pila.Count == 0) return false;
                char tope = pila.Pop();
                if (!EsParCoincidente(tope, c)) return false;
            }
        }

        return pila.Count == 0;
    }

    private static bool EsParCoincidente(char apertura, char cierre)
    {
        return (apertura == '(' && cierre == ')') ||
               (apertura == '{' && cierre == '}') ||
               (apertura == '[' && cierre == ']');
    }
}

