using System;

namespace SingletonLab
{
    // 4. Потокобезпечна реалізація з лінивою ініціалізацією
    public sealed class SafeSingleton
    {
        private static readonly Lazy<SafeSingleton> _instance = 
            new Lazy<SafeSingleton>(() => new SafeSingleton());

        // 2. Приватний конструктор (забезпечує один екземпляр)
        private SafeSingleton() 
        {
            Console.WriteLine("[INFO] Екземпляр Singleton створено.");
        }

        // 3. Доступ до об'єкта
        public static SafeSingleton Instance => _instance.Value;

        public void DoSomething(string message)
        {
            Console.WriteLine($"[Singleton Work]: {message}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== Практична робота №19: Шаблон Singleton ===\n");

            // Перевірка єдиного екземпляра
            SafeSingleton s1 = SafeSingleton.Instance;
            SafeSingleton s2 = SafeSingleton.Instance;

            s1.DoSomething("Доступ до ресурсу через s1");
            s2.DoSomething("Доступ до ресурсу через s2");

            if (ReferenceEquals(s1, s2))
            {
                Console.WriteLine("\n[SUCCESS] Об'єкт лише один (Singleton працює).");
            }
        }
    }
}
