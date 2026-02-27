using System;
using System.Collections.Generic;

namespace ObjectOrientedProject
{
    // 3. Інтерфейс для стандартизації поведінки
    public interface IWorkable
    {
        void PerformWork();
    }

    // 4. Абстракція: Базовий клас
    public abstract class Employee
    {
        // 4. Інкапсуляція: Приватне поле та публічна властивість
        private string _name;
        public string Name 
        { 
            get => _name; 
            set => _name = value; 
        }

        public Employee(string name) => Name = name;

        public abstract void GetInfo();
    }

    // 3. Наслідування: Спеціалізований клас
    public class Developer : Employee, IWorkable
    {
        public string Language { get; set; }

        public Developer(string name, string lang) : base(name) => Language = lang;

        public override void GetInfo() 
        {
            Console.WriteLine($"[Developer]: {Name}, Спеціалізація: {Language}");
        }

        public void PerformWork() 
        {
            Console.WriteLine($"{Name} пише код на {Language}...");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("=== Практична робота №22: Основні класи ===\n");

            // 5. Тестування та взаємодія
            Developer dev = new Developer("Олександр", "C#");
            dev.GetInfo();
            dev.PerformWork();

            Console.WriteLine("\n[Успіх]: Класи реалізовані з дотриманням принципів ООП.");
        }
    }
}
