using System;
using System.Windows.Forms;

namespace Forensic_Eng
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            // Sadece bu satır Form1'i başlatır
            Application.Run(new Form1());
        }
    }
}
