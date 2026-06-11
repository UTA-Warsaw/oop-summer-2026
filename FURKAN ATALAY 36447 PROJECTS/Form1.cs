using System;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace Forensic_Eng
{
    public class Form1 : Form
    {
        public Form1()
        {
            InitializeForensicInterface();
        }

        private void InitializeForensicInterface()
        {
            this.Text = "DIGITAL FORENSICS ANALYZER v1.0";
            this.BackColor = Color.FromArgb(12, 12, 12);
            this.Size = new Size(550, 450);
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            this.StartPosition = FormStartPosition.CenterScreen;

            Label lblHeader = new Label
            {
                Text = "FORENSIC DATA WIPER",
                ForeColor = Color.Cyan,
                Font = new Font("Consolas", 18, FontStyle.Bold),
                Location = new Point(120, 50),
                AutoSize = true
            };
            this.Controls.Add(lblHeader);

            Button btnExecute = new Button
            {
                Text = "START WIPING SEQUENCE",
                Size = new Size(320, 70),
                Location = new Point(115, 180),
                BackColor = Color.FromArgb(0, 40, 0),
                ForeColor = Color.Lime,
                FlatStyle = FlatStyle.Flat,
                Font = new Font("Segoe UI", 12, FontStyle.Bold),
                Cursor = Cursors.Hand
            };
            btnExecute.FlatAppearance.BorderSize = 2;
            btnExecute.FlatAppearance.BorderColor = Color.Lime;
            btnExecute.Click += (s, e) => RunForensicScript();
            this.Controls.Add(btnExecute);

            Label lblConsole = new Label
            {
                Text = "SOURCE: Desktop\\EXIF  |  DEST: Desktop\\Exif_Removed",
                ForeColor = Color.White,
                Font = new Font("Consolas", 8),
                Location = new Point(115, 330),
                AutoSize = true
            };
            this.Controls.Add(lblConsole);
        }

        private void RunForensicScript()
        {
            try
            {
                string desktop = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
                string inputPath = Path.Combine(desktop, "EXIF");
                string outputPath = Path.Combine(desktop, "Exif_Removed");

                // Eğer Exif_Removed yoksa oluşturur
                if (!Directory.Exists(outputPath)) Directory.CreateDirectory(outputPath);

                string pythonExe = @"C:/Users/Furkan/PycharmProjects/PythonProject/.venv/Scripts/python.exe";
                string pythonScript = @"C:/Users/Furkan/Desktop/cleaner.py";

                ProcessStartInfo startInfo = new ProcessStartInfo
                {
                    FileName = pythonExe,
                    Arguments = $"\"{pythonScript}\" \"{inputPath}\" \"{outputPath}\"",
                    UseShellExecute = false,
                    CreateNoWindow = true,
                    RedirectStandardOutput = true
                };

                Process.Start(startInfo);
                MessageBox.Show("Forensic sequence initiated.\nCheck Exif_Removed folder.", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message, "Alert");
            }
        }
    }
}
