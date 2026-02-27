using System;
using System.IO;

namespace SingletonProject
{
    // Практична робота №20: Реалізація Singleton для Logger (Журнал подій)
    public sealed class Logger
    {
        private static readonly Lazy<Logger> _instance = new Lazy<Logger>(() => new Logger());
        private string _logFilePath = "log.txt";

        private Logger() 
        {
            Console.WriteLine("[System]: Logger ініціалізовано.");
        }

        public static Logger Instance => _instance.Value;

        public void Log(string message)
        {
            string logEntry = $"[{DateTime.Now}] : {message}";
            Console.WriteLine(logEntry);
            // Додаємо запис у файл (реальний ресурс)
            File.AppendAllText(_logFilePath, logEntry + Environment.NewLine);
        }
    }

    class Program
    {
        static void Main()
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== Практична робота №20: Використання Singleton ===\n");

            Logger logger = Logger.Instance;
            logger.Log("Програма запущена.");
            logger.Log("Користувач виконав дію у системі.");
            logger.Log("Робота №20 успішно реалізована.");

            Console.WriteLine("\n[Успіх]: Всі записи збережені в log.txt через єдиний екземпляр Logger.");
        }
    }
}
