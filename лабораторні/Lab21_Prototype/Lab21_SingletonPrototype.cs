using System;

/*
 * Практична робота №21
 * Тема: Створення робочого прототипу програмного продукту
 * Проєкт: Прототип системи глобального логування (Singleton)
 */

namespace Lab21_Prototype
{
    // 1. Технологія: C#, .NET Console
    // 2. Архітектура: Singleton Pattern
    public sealed class LoggerPrototype
    {
        private static readonly Lazy<LoggerPrototype> _instance = 
            new Lazy<LoggerPrototype>(() => new LoggerPrototype());

        public static LoggerPrototype Instance => _instance.Value;

        // Приватний конструктор (Ключова функція прототипу)
        private LoggerPrototype() 
        {
            Console.WriteLine("[System]: Прототип ініціалізовано успішно.");
        }

        // Демонстрація функціоналу
        public void LogActivity(string action)
        {
            Console.WriteLine($"[{DateTime.Now:T}] Дія користувача: {action}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== Демонстрація прототипу (Практична №21) ===\n");

            // 3. Тестування основного потоку (Main flow)
            var logger = LoggerPrototype.Instance;
            logger.LogActivity("Запуск базової архітектури");
            logger.LogActivity("Тестування взаємодії компонентів");

            Console.WriteLine("\n[Status]: Тестування прототипу завершено без помилок.");
        }
    }
}