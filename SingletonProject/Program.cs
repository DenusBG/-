using System;

/*
 * Практична робота №20
 * Тема: Розробка графіку виконання проєкту конструювання ПЗ
 */

namespace SingletonApp
{
    public sealed class Singleton
    {
        private static readonly Lazy<Singleton> _instance = 
            new Lazy<Singleton>(() => new Singleton());

        public static Singleton Instance => _instance.Value;

        private Singleton() => Console.WriteLine("[System]: Сервіс активовано для роботи №20");

        public void ShowStatus() => Console.WriteLine("[Status]: Графік проекту завантажено в репозиторій.");
    }

    class Program
    {
        static void Main()
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Singleton.Instance.ShowStatus();
        }
    }
}