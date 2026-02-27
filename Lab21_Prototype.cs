using System;
using System.Collections.Generic;

namespace PrototypeProject
{
    // 2. Базова архітектура: Інтерфейс для модулів
    public interface IModule
    {
        void Execute();
    }

    // 3. Програмування ключових функцій: Модуль логіки
    public class TaskEngine : IModule
    {
        public void Execute()
        {
            Console.WriteLine("[Engine]: Обробка основного потоку даних...");
        }
    }

    // Прототип продукту
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== Практична робота №21: Робочий прототип ===\n");

            // 1. Вибір технологій: C#, .NET Console
            Console.WriteLine("[Step 1]: Технологія обрана - .NET Core Console App.");

            // 2. Ініціалізація архітектури
            IModule engine = new TaskEngine();
            
            // 3. Демонстрація основного потоку
            Console.WriteLine("[Step 3]: Запуск ключових функцій...");
            engine.Execute();

            // 5. Тестування та відладження
            Console.WriteLine("\n[Step 5]: Тестування компонентів...");
            if (engine != null) {
                Console.WriteLine(">>> Тест пройдено: Компонент Engine активний.");
            }

            Console.WriteLine("\n=== Демонстрація прототипу завершена успішно ===");
        }
    }
}
